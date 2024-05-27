from BaseLib import *
from BaseExercise import *
from random import randint
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]

PrintColor("Cette moulinette n'est pas encore disponible",Colors.RED)

class GNL_BaseExercise(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        self.path = Config.project_path
        
    def Init_GNL(self):
        self.BUFFER_SIZE = None
        self.main = """
        int main(void)
		{
			return (0);
		}
        """
        
    def Compile(self):
        self.Init_GNL()
        Config.valgrind.active = True
        Config.valgrind.print = True
        AutoMain(None, None,"""
		#include "get_next_line.h"
		#include <stdio.h>
		#include <stdlib.h>
		#include <limits.h>
		#include <fcntl.h>
		""" + self.main)
        if self.BUFFER_SIZE == None:
            buff_txt = ""
        else:
            buff_txt = " -D BUFFER_SIZE="+str(self.BUFFER_SIZE)
        cmd = "gcc -Wall -Werror -Wextra"+buff_txt+" -o Output main.c get_next_line.c get_next_line_utils.c"
        print(cmd)
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        print(result.stdout+"\n"+result.stderr)
        return 'Output' in os.listdir(Config.temp_path)

    def Execute(self):
        return "OK" in ExecuteCode()
    
@AddExercise(id="test1")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        with open(self.path+"/file.txt","w") as f:
            f.write("Hello World\nI am a test\nThis is a test file")
        self.BUFFER_SIZE = None
        self.main = """
        int main(void)
		{
            int fd = open("file.txt",O_RDONLY);
            char *line = (void *)1;
            while (fd != -1 && line != NULL)
            {
                line = get_next_line(fd);
                if (line != NULL)
                {
                    printf("%s\\n",line);
                    free(line);
                }
            }
            if (fd != -1)
                close(fd);
			return (0);
		}
        """