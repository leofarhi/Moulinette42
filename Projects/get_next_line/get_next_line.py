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
        Config.valgrind.active = True
        #Config.valgrind.print = True
        self.Init_GNL()
        AutoMain(None, None,"""
		#include "get_next_line.h"
		#include <stdio.h>
		#include <stdlib.h>
		#include <limits.h>
		#include <fcntl.h>
                 
        int print_line(char *line)
		{
			printf("#%s",line);
            if (line != NULL)
				free(line);
            return (line != NULL);
		}
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
        with open(Config.temp_path+"/file.txt","w") as f:
            f.write("Hello World\nI am a test\nThis is a test file!\nYaay\nYaay")
        self.BUFFER_SIZE = None
        self.main = """
        int main(void)
		{
            int fd = open("file.txt",O_RDONLY);
            printf("fd = %d\\n",fd);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """

@AddExercise(id="test2")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        with open(Config.temp_path+"/file.txt","w") as f:
            f.write("Hello World\nI am a test\nThis is a test file!\nYaay\nYaay\n")
        self.BUFFER_SIZE = None
        self.main = """
        int main(void)
		{
            int fd = open("file.txt",O_RDONLY);
            printf("fd = %d\\n",fd);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """	
        
#@AddExercise(id="test3")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        CopyToTemp(os.path.dirname(__file__)+"/read_error.txt")
        self.BUFFER_SIZE = 10
        self.main = """
        int main(void)
		{
            int fd = open("read_error.txt",O_RDONLY);
            printf("fd = %d\\n",fd);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """
        
#@AddExercise(id="test4")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        Config.valgrind.print = True
        CopyToTemp(os.path.dirname(__file__)+"/read_error.txt")
        self.BUFFER_SIZE = 10
        self.main = """
        int main(void)
		{
            int fd = open("read_error.txt",O_RDONLY);
            print_line(get_next_line(fd));
            print_line(get_next_line(fd));
            char temp[1000];
            read(fd,temp,1000);
            printf("fd = %d\\n",fd);
            printf("BUFFER_SIZE = %d\\n",BUFFER_SIZE);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """
        
@AddExercise(id="test5")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        Config.valgrind.print = True
        CopyToTemp(os.path.dirname(__file__)+"/giant_line.txt")
        self.BUFFER_SIZE = 10
        self.main = """
        int main(void)
		{
            int fd = open("giant_line.txt",O_RDONLY);
            print_line(get_next_line(fd));
            print_line(get_next_line(fd));
            char temp[1000];
            read(fd,temp,1000);
            printf("fd = %d\\n",fd);
            printf("BUFFER_SIZE = %d\\n",BUFFER_SIZE);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """
        
@AddExercise(id="test6")
class Exo(GNL_BaseExercise):
    def Init_GNL(self):
        Config.valgrind.print = True
        with open(Config.temp_path+"/file.txt","w") as f:
            f.write("0")
        self.BUFFER_SIZE = 1000
        self.main = """
        int main(void)
		{
            int fd = open("file.txt",O_RDONLY);
            printf("fd = %d\\n",fd);
            while(print_line(get_next_line(fd)))
            {}
            if (fd != -1)
                close(fd);
			return (0);
		}
        """	