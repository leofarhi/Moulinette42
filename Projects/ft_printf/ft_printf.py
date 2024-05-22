from BaseLib import *
from BaseExercise import *
from random import randint
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]


@AddExercise(id="ft_printf")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        self.path = Config.project_path

    def Compile(self):
        AutoMain(None, None,"""
#include "ft_printf.h"
int main(void)
{
    ft_printf("", "Hello","yaa");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==0