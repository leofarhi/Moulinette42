from BaseLib import *
from BaseExercise import *
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]

@AddExercise(id="ex00")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="./Output\n"
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        v = ExecuteCode(args=["test1","test2","test3"])=="test1\ntest2\ntest3\n"
        v2 = ExecuteCode()==""
        return v and v2

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        v = ExecuteCode(args=["test1","test2","test3"])=="test3\ntest2\ntest1\n"
        v2 = ExecuteCode()==""
        return v and v2

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        v = ExecuteCode(args=["a","B","C","AA","A","D","","12","1","123"])=="\n1\n12\n123\nA\nAA\nB\nC\nD\na\n"
        v2 = ExecuteCode()==""
        return v and v2
