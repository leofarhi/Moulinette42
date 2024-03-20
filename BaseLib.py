import os,sys
import subprocess
import shutil
from shutil import rmtree
import random
import json
import importlib
import time

class ValgrindConfig:
    def __init__(self):
        self.active = False
        self.print = False

class ConfigClass:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.temp_path = os.path.join(self.base_path,"temp")
        self.normeflag = ["-R","CheckForbiddenSourceHeader"]
        self.project_path = None
        self.output_name = "Output"
        self.valgrind = ValgrindConfig()
Config = ConfigClass()

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'

def PrintColor(text,color):
    print(color+text+'\033[0m')

def IfValid(valid,title=""):
    if valid :
        PrintColor("OK ! "+title,Colors.GREEN)
    else:
        PrintColor("Error ! "+title,Colors.RED)

def Join(path1,*paths):
    return os.path.join(path1,*paths)

def MakeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def DelDir(path):
    if os.path.exists(path):
        try:
            rmtree(path)
        except:
            if get_os() == "Windows":
                os.system(f"rmdir /S /Q {path}")

def ResetTempDir():
    path = Join(Config.base_path,"temp")
    DelDir(path)
    MakeDir(path)
    return path

def CopyToTemp(path, subfolder=""):
    direc = Config.temp_path
    if subfolder!="":
        direc = Join(direc,subfolder)
        MakeDir(direc)
    new_path = Join(direc,os.path.basename(path))
    shutil.copyfile(path,Join(Config.temp_path,new_path))
    return new_path

ResetTempDir()

def get_os():
    if sys.platform == "win32":
        return "Windows"
    elif sys.platform == "linux":
        return "Linux"
    elif sys.platform == "darwin":
        return "Mac"
    else:
        return "Other"

def CheckNorme(path):
    if os.path.isdir(path):
        res = Process(["norminette"]+Config.normeflag,cwd=path)
    else:
        res = Process(["norminette"]+Config.normeflag+[path])
    result = res.stdout.rstrip()
    print(result)
    for line in result.split("\n"):
        if not ": OK!" in line:
            return False
    return True

class Stdout:
    def __init__(self):
        self.stdout = ""
        self.stderr = ""
        self.valgrindError = False

    def __str__(self):
        return self.stdout

def Exec(string):
    os.system(string)

def Process(cmd_list,stderr=False,**args):
    if stderr:
        result = subprocess.run(cmd_list, stdout=subprocess.PIPE,stderr=subprocess.PIPE,**args)
    else:
        result = subprocess.run(cmd_list, stdout=subprocess.PIPE,**args)
    stdout = Stdout()
    stdout.stdout = result.stdout.decode('utf-8')
    if stderr:
        stdout.stderr = result.stderr.decode('utf-8')
    return stdout

def PrintTree(cwd=Config.temp_path):
    res = str(Process(["tree"],cwd=cwd))
    PrintColor(res,Colors.BLUE)
    return res

def LoadConfig():
    path = Join(Config.base_path,"config.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def SaveConfig(config):
    path = Join(Config.base_path,"config.json")
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)

def GetGitPath(project_id, force=False):
    config = LoadConfig()
    path = config.get("Projects_path",{}).get(get_os(),{}).get(project_id,None)
    if path == None or force:
        path = None
        while path==None or not os.path.exists(path):
            print("Le chemin n'existe pas")
            path = input("taper le chemin du repo "+project_id+":")
    elif not os.path.exists(path):
        print("Le chemin n'existe pas")
        quit()
    config["Projects_path"] = config.get("Projects_path",{})
    config["Projects_path"][get_os()] = config["Projects_path"].get(get_os(),{})
    config["Projects_path"][get_os()][project_id] = path
    SaveConfig(config)
    return path


def GetIdProject(file_path):
    return os.path.relpath(os.path.dirname(os.path.realpath(file_path)),Join(Config.base_path,"Projects")).replace("\\","/").replace("/",".")



def Pause():
    input()

def AutoMain(path,textH,textMain):
    if path != None and textH != None:
        h_file = Join(Config.temp_path,os.path.splitext(os.path.basename(path))[0]+".h")
        with open(h_file,"w") as fic:
            fic.write(textH)
    else:
        h_file = None

    main_file = Join(Config.temp_path,"main.c")
    with open(main_file,"w") as fic:
        fic.write(textMain)
    return h_file,main_file

def CheckValgrind(result, Print=True):
    if Print:
        print(result.stderr)
    a = "LEAK SUMMARY" in result.stderr
    if a:
        PrintColor("Fuite de memoire",Colors.RED)
    b = "Conditional jump".lower() in result.stderr.lower()
    if b:
        PrintColor("Jump error",Colors.RED)
    c = not "== ERROR SUMMARY: 0 errors from 0 contexts" in result.stderr
    if c:
        PrintColor("valgrind error",Colors.RED)
    res = (not a) and (not b) and (not c)
    result.valgrindError = res
    return res

def CreateFileInTemp(name,text):
    file = Join(Config.temp_path,name)
    with open(file,"w") as fic:
        fic.write(text)
    return file

def CompileTemp(lib=""):
    if Config.valgrind.active:
        lib = "-g3 "+lib
    if lib!="":
        lib+=" "
    os.chdir(Config.temp_path)
    if get_os() == "Linux":
        cmd = "cc -Wall -Wextra -Werror "+lib+"*.c -o "+Config.output_name
    elif get_os() == "Windows":
        cmd = "gcc -Wall -Wextra -Werror "+lib+"*.c -o "+Config.output_name+".exe"
    result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
    print(result.stdout)
    if result.stderr:
        PrintColor(result.stderr,Colors.RED)
        return False
    return True

def ExecuteCode(exc=[], args=[],canPrint=True,cat_e = False,returnAll = False):
    if Config.valgrind.active:
        exc = ["valgrind"]+exc
    os.chdir(Config.temp_path)
    cmd = "chmod +x "+Config.output_name
    Process(cmd,shell=True,cwd=Config.temp_path)
    cmd = exc+["./"+Config.output_name]+args
    result = Process(cmd,cwd=Config.temp_path, stderr=True)
    #replace all return by \n
    result.stdout = result.stdout.replace("\r\n","\n").replace("\r","\n")
    if canPrint:
        res = result.stdout
        if (cat_e):
            res = res.replace("\n","$\n")
        print(res, end="")
        PrintColor("%",'\033[4m')
    if returnAll:
        res = result
    else:
        res = result.stdout
    if Config.valgrind.active:
        CheckValgrind(result, Config.valgrind.print)
    return res
