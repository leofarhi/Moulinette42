from BaseLib import *
from BaseExercise import Exercises
Commandes = {}

def AddCommande(name, func):
    Commandes[name] = func

def ExecCommande(name, *args, **kwargs):
    if name in Commandes:
        Commandes[name](*args, **kwargs)
    else:
        print(f"Commande {name} not found")

def Commande(name):
    def decorator(func):
        AddCommande(name, func)
        return func
    return decorator

##################################################

@Commande("print")
def Print(project_id):
    Exec("clear")
    if os.path.exists(os.path.join(Config.base_path,"Projects",project_id.replace(".","/"))):
        if get_os() == "Linux":
            Exec("bat "+os.path.join(Config.base_path,"Projects",project_id.replace(".","/"))+"/*")
        elif get_os() == "Windows":
            path = os.path.abspath(os.path.join(Config.base_path,"Projects",project_id.replace(".","/")))
            for file in os.listdir(path):
                print("#"*10,file,"#"*10)
                Exec("type "+os.path.join(path,file))
    else:
        print("Project not found")

@Commande("all")
def all(name=""):
    Exec("clear")
    path = os.path.abspath(os.path.join(Config.base_path,"Projects"))
    files = []
    for r, d, f in os.walk(path):
        p = str(os.path.relpath(r, path))
        if "__pycache__" in p or p=='.': continue
        if name == "" or name.lower() in p.lower():
            if os.path.basename(r)+".py" in f:
                files.append(p.replace("/","."))
    for i in files:
        PrintColor(i,Colors.YELLOW)
        
@Commande("exo")
def Print(project_id):
    Exec("clear")
    spec = importlib.import_module(f"Projects.{project_id}.{project_id.split('.')[-1]}")
    print('#'*5)
    for i in Exercises:
        PrintColor(i,Colors.YELLOW)

@Commande("path")
def Path(project_id):
    GetGitPath(project_id, True)

@Commande("git")
def Git(project_id):
    path = GetGitPath(project_id)
    if path == None:
        print("Project not found")
    else:
        PrintTree(path)
        print("path :",path)
        cmt_name = input("commit name :")
        print(Process(["git","add","."],cwd=path))
        print(Process(["git","commit","-m",cmt_name],cwd=path))
        print(Process(["git","push"],cwd=path))

@Commande("cd")
def Cd(project_id):
    if project_id=='temp':
        path = Config.temp_path
    else:
        path = GetGitPath(project_id)
    print("path :",path)
    if path == None:
        print("Project not found")
    else:
        if get_os() == "Linux":
            Exec(f'bash -c "cd {path}; exec bash"')
        elif get_os() == "Windows":
            Exec(f'cmd /k "cd {path}"')
            
@Commande("norme")
def Norme(project_id):
    path = GetGitPath(project_id)
    if path == None:
        print("Project not found")
    else:
        print("path :",path)
        IfValid(CheckNorme(path))