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

def GetGitPath(exo):
    path = LoadConfig(exo+"PATH_git")
    if path == None:
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

def CheckNorme(path):
    result = Process(["norminette",Config.normeflag,path]).rstrip()
    print(result)
    return result==path+": OK!"

def Exec(string):
    os.system(string)

def Process(cmd_list,**args):
    result = subprocess.run(cmd_list, stdout=subprocess.PIPE,**args)
    result = result.stdout.decode('utf-8')
    return result

def CopyToTemp(path):
    new_path = Join(tempDir,os.path.basename(path))
    shutil.copyfile(path,Join(tempDir,new_path))
    return new_path

def Pause():
    input()

def AutoMain(path,textH,textMain):
    h_file = Join(tempDir,os.path.splitext(os.path.basename(path))[0]+".h")
    with open(h_file,"w") as fic:
        fic.write(textH)

    main_file = Join(tempDir,"main.c")
    with open(main_file,"w") as fic:
        fic.write(textMain)
    return h_file,main_file

def CompileTemp(lib=""):
    if lib!="":
        lib+=" "
    os.chdir(tempDir)
    cmd = "cc -Wall -Wextra -Werror "+lib+"*.c -o Output"
    Process(cmd,shell=True,cwd=tempDir)

def ExecuteCode(args="",canPrint=True):
    os.chdir(tempDir)
    cmd = "chmod +x Output"
    Process(cmd,shell=True,cwd=tempDir)
    if args!="":
        args = " "+args
    cmd = "./Output"+args
    result = Process(cmd,cwd=tempDir)
    if canPrint:
        print(result, end="")
        PrintColor("%",'\033[4m')
    return result

color_red='\033[93m'
color_green='\033[92m'

def PrintColor(text,color):
    print(color+text+'\033[0m')

def IfValid(valid,title=""):
    if valid :
        PrintColor("OK ! "+title,color_green)
    else:
        PrintColor("Error ! "+title,color_red)

tempDir = ResetTempDir()