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
        print(Process(["make"],cwd=Config.temp_path))
        AutoMain(None, None,"""
		#include <ft_printf.h>
		int main(void)
		{
			//ft_printf("", "Hello","yaa");
            //ft_putnbr_fd(42, 1);
            ft_printf("Hello\\n");
            ft_printf("Hello % %\\n", "World", "!");
			return (0);
		}
		""")
        #add libftprintf.a to the compilation
        cmd = "gcc -Wall -Wextra -Werror -I./includes -o Output main.c -L. -lftprintf"
        print(cmd)
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        print(result)
        return 'Output' in os.listdir(Config.temp_path)

    def Execute(self):
        return ExecuteCode()==0