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
		#include <stdio.h>
        
		int main(void)
		{
			//ft_printf("", "Hello","yaa");
            //ft_putnbr_fd(42, 1);
            //ft_printf("Hello\\n");
            /*int res = ft_printf("Hello %s %% %c\\n", "World", '!');
            if (res == -1)
                printf("Error in ft_printf (-1)\\n");
            else
				printf("ft_printf returned %d\\n", res);
            ft_printf("\\n", 0, 0);
            char *str = "Hello";
            ft_printf("# %p %p #\\n", 0, 0);
            ft_printf("# %p %p #\\n", str, 0);
            ft_printf("# %p %p #\\n", (void *)5645564564, 0);
            printf("# %p %p #\\n", NULL, NULL);
            printf("# %p %p #\\n", str, NULL);
            printf("# %p %p #\\n", (void *)5645564564, NULL);*/
            char *str = NULL;
            ft_printf("%23s#\\n", str);
            printf("%23s#\\n", str);
			return (0);
		}
		""")
        #add libftprintf.a to the compilation
        cmd = "gcc -Wall -Wextra -Werror -I./includes -o Output main.c -L. -lftprintf"
        print(cmd)
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        print(result.stdout+"\n"+result.stderr)
        return 'Output' in os.listdir(Config.temp_path)

    def Execute(self):
        return ExecuteCode()==0