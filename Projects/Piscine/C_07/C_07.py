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
        Config.valgrind.active = True

    def Compile(self):
        AutoMain(self.files["ft_strdup.c"],"char *ft_strdup(char *src);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strdup.h"
int main(void)
{
    char *a0 = strdup("Test");
    char *a1 = ft_strdup("Test");
    char *b0 = strdup("484df41hdy1h111fs1fsd15sf15sdf115d15fdgs15gfd4sg1615df156g1515g4erg4561esg156gr15156g15eg15eg15e51e51g1515ge156e156eg156e15156ge516e1551eg51eg15g1551eg15e516eg15e15eg1515e55eg51e15e51g5151eg15eg1515egr515151erg51er51e51e551ee5eg51egr51er51er5er5eg51e5r1e51rg5egr5eg51erg5e1r51e6rg51egr516ee5g15e1g5e1g5e1g51ger51egr51erg55reg5er55er55");
    char *b1 = ft_strdup("484df41hdy1h111fs1fsd15sf15sdf115d15fdgs15gfd4sg1615df156g1515g4erg4561esg156gr15156g15eg15eg15e51e51g1515ge156e156eg156e15156ge516e1551eg51eg15g1551eg15e516eg15e15eg1515e55eg51e15e51g5151eg15eg1515egr515151erg51er51e51e551ee5eg51egr51er51er5er5eg51e5r1e51rg5egr5eg51erg5e1r51e6rg51egr516ee5g15e1g5e1g5e1g51ger51egr51erg55reg5er55er55");
    printf("%s\\n", strcmp(a0, a1) == 0 ?
			"OK" :
			"Fail");
	printf("%s\\n", strcmp(b0, b1) == 0 ?
			"OK" :
			"Fail");
    free(a0);
    free(a1);
    free(b0);
    free(b1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().stdout.count("OK") == 2
    
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

