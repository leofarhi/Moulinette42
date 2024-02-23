import os,sys
import subprocess
import shutil
from shutil import rmtree
import random
import json

class Config:
    def __init__(self):
        self.PATH_main = ""
        self.PATH_git = ""
        self.normeflag = ""
Config = Config()

def LoadConfig(key):
    j = Join(Config.PATH_main,"config.json")
    if not os.path.exists(j):
        with open(j,"w") as fic:
            fic.write(json.dumps(dict()))
    with open(j,"r") as fic:
        text = fic.read()
    data = json.loads(text)
    return data.get(key,None)

def SaveConfig(key,value):
    j = Join(Config.PATH_main,"config.json")
    if not os.path.exists(j):
        with open(j,"w") as fic:
            fic.write(json.dumps(dict()))
    with open(j,"r") as fic:
        text = fic.read()
    data = json.loads(text)
    data[key] = value
    with open(j,"w") as fic:
        fic.write(json.dumps(data, sort_keys=True, indent=4))

def GetGitPath(exo, force=False):
    path = LoadConfig(exo+"PATH_git")
    if path == None or force:
        path = input("taper le chemin du repo "+exo+":")
    if not os.path.exists(path):
        print("Le chemin n'existe pas")
        quit()
    SaveConfig(exo+"PATH_git",path)
    return path

def MakeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def DelDir(path):
    if os.path.exists(path):
        rmtree(path)

def ResetTempDir():
    path = Join(os.path.dirname(os.path.realpath(__file__)),"temp")
    DelDir(path)
    MakeDir(path)
    return path

def Join(path1,*paths):
    return os.path.join(path1,*paths)

def CheckNorme(path, count=1):
    flags = []
    if Config.normeflag != "":
        flags = Config.normeflag.split(" ")
    result = Process(["norminette"]+flags+[path]).stdout.rstrip()
    print(result)
    return result.count(": OK!") == count

def Exec(string):
    os.system(string)

class Stdout:
    def __init__(self):
        self.stdout = ""
        self.stderr = ""

    def __str__(self):
        return self.stdout

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

def CopyToTemp(path, subfolder=""):
    direc = tempDir
    if subfolder!="":
        direc = Join(direc,subfolder)
        MakeDir(direc)
    new_path = Join(direc,os.path.basename(path))
    shutil.copyfile(path,Join(tempDir,new_path))
    return new_path

def CheckValgrind(result, Print=True):
    if Print:
        print(result)
    a = "LEAK SUMMARY" in result
    if a:
        PrintColor("Fuite de memoire",color_red)
    b = "Conditional jump".lower() in result.lower()
    if b:
        PrintColor("Jump error",color_red)
    c = not "== ERROR SUMMARY: 0 errors from 0 contexts" in result
    if c:
        PrintColor("valgrind error",color_red)
    return (not a) and (not b) and (not c)

#ancienne version
def CheckMemory(*arg,**args):
    return CheckValgrind(*arg,**args)

def Pause():
    input()

def AutoMain(path,textH,textMain):
    if path != None and textH != None:
        h_file = Join(tempDir,os.path.splitext(os.path.basename(path))[0]+".h")
        with open(h_file,"w") as fic:
            fic.write(textH)
    else:
        h_file = None

    main_file = Join(tempDir,"main.c")
    with open(main_file,"w") as fic:
        fic.write(textMain)
    return h_file,main_file


def CreateFileInTemp(name,text):
    file = Join(tempDir,name)
    with open(file,"w") as fic:
        fic.write(text)
    return file

def CompileTemp(lib=""):
    if lib!="":
        lib+=" "
    os.chdir(tempDir)
    cmd = "cc -Wall -Wextra -Werror "+lib+"*.c -o Output"
    result = Process(cmd,shell=True,cwd=tempDir)

def ExecuteCode(exc=[], args=[],canPrint=True,cat_e = False,returnAll = False):
    os.chdir(tempDir)
    cmd = "chmod +x Output"
    Process(cmd,shell=True,cwd=tempDir)
    cmd = exc+["./Output"]+args
    result = Process(cmd,cwd=tempDir, stderr=True)
    if canPrint:
        res = result.stdout
        if (cat_e):
            res = res.replace("\n","$\n")
        print(res, end="")
        PrintColor("%",'\033[4m')
    if returnAll:
        return result
    return result.stdout


color_red='\033[93m'
color_green='\033[92m'
color_blue = '\033[94m'

def PrintColor(text,color):
    print(color+text+'\033[0m')

def IfValid(valid,title=""):
    if valid :
        PrintColor("OK ! "+title,color_green)
    else:
        PrintColor("Error ! "+title,color_red)

tempDir = ResetTempDir()

def PrintTree(cwd=tempDir):
    res = str(Process(["tree"],cwd=cwd))
    PrintColor(res,color_blue)
    return res