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
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex06")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex07")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="ex08")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files[".c"],)
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0
