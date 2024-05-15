from BaseLib import *
class BaseExercise:
    def __init__(self, id, *args, **kargs):
        self.id = id
        self.path = Join(Config.project_path,self.id)
        self.files = {}

    def CopyToTemp(self, file,*args, **kwargs):
        return CopyToTemp(Join(self.path,file),*args, **kwargs)
    
    def Init(self):
        global Config
        Config.normeflag = ["-R","CheckForbiddenSourceHeader"]
        Config.output_name = "Output"
        Config.valgrind = ValgrindConfig()
        for file in os.listdir(self.path):
            if os.path.isfile(Join(self.path,file)):
                self.files[file] = self.CopyToTemp(file)
        return True
    
    def Norme(self):
        return CheckNorme(self.path)
    
    def Compile(self):
        return True
    
    def Execute(self):
        return True

Exercises = {}

def AddExercise(id, *args, **kargs):
    def decorator(classType):
        Exercises[id] = classType(id, *args, **kargs)
        return classType
    return decorator

def BetterId(id):
    #detect if id as ex00 etc...
    id = str(id)
    string = ""
    i = 0
    while i < len(id) and id[i].isalpha():
        string += id[i]
        i += 1
    string += " "
    string += id[i:].replace("_"," ")
    string = string[0].upper() + string[1:]
    return string

def ExecExercise(id):
    if id in Exercises:
        exo = Exercises[id]
        PrintColor("#"*15+" "+BetterId(exo.id)+" "+"#"*15,Colors.YELLOW)
        ResetTempDir()
        valid = exo.Init()
        if valid:
            print("#"*15,"Norme","#"*15)
            valid_norme = exo.Norme()
            IfValid(valid_norme,"Norme")
            print("#"*15,"Compile","#"*15)
            valid_compile = exo.Compile()
            IfValid(valid_compile,"Compile")
            if valid_compile:
                print("#"*15,"Exec","#"*15)
                valid_exec = exo.Execute()
                IfValid(valid_exec,"Execution")
            else:
                valid_exec = False
            valid = valid and valid_norme and valid_compile and valid_exec
        IfValid(valid,BetterId(exo.id))
        PrintColor("#"*40,Colors.YELLOW if valid else Colors.RED)
    else:
        print(f"Exercise {id} not found")
    print("")

def ExecExercises():
    for id in Exercises:
        ExecExercise(id)