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
        Config.valgrind.active = True
        #Config.valgrind.print = True
        print(Process(["make"],cwd=Config.temp_path))
        AutoMain(None, None,"""
		#include <ft_printf.h>
		#include <stdio.h>
		#include <limits.h>
        
		int main(void)
		{
			return (0);
		}
		""")
        #add libftprintf.a to the compilation
        cmd = "gcc -Wall -Wextra -Werror -I./includes -o Output main.c -L. -lftprintf"
        print(cmd)
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        print(result.stdout+"\n"+result.stderr)
        return 'Output' in os.listdir(Config.temp_path)
    
    def check(self,format,args = []):
        txt_args = ""
        for arg in args:
            txt_args += str(arg)+","
        txt_args = txt_args[:-1]
        line = "format"
        if len(args) > 0:
            line += ","+txt_args
        AutoMain(None, None,"""
		#include <ft_printf.h>
		#include <stdio.h>
		#include <limits.h>
        
		int main(void)
		{
            char *format = "#"""+format+"""#\\n";
            int res1 = ft_printf("""+line+""");
            int res2 = printf("""+line+""");
            printf("ft_printf = %d, printf = %d\\n",res1,res2);
            printf("format = %s",format);
			return (0);
		}
		""")
        cmd = "rm -f Output"
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        #print(result.stdout+"\n"+result.stderr)
        cmd = "gcc -Wall -Wextra -Werror -I./includes -o Output main.c -L. -lftprintf"
        result = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        #print(result.stdout+"\n"+result.stderr)
        ExecuteCode()
        print("#################")

    def Execute(self):
        tests = [
            ("%s",['"Hello World"']),
            ("% s",['"Hel"']),
            ("%.03s",['"Hello"']),
            ("%.3s",['"Hello"']),
            ("%03s",['"Hello"']),
            ("%.03s",['NULL']),
            ("%.3s",['NULL']),
            ("%03s",['NULL']),
            ("%-8.03s",['"Hello"']),
            ("%-8.03s",['NULL']),
            ("%.0s",['NULL']),


            ("%.03s",['NULL']),
            ("%.05s",['NULL']),
            ("%.06s",['NULL']),
            ("%.09s",['NULL']),
            ("%3.6s",['NULL']),
            ("%-3.8s",['NULL']),

        ]
        tests = [
            ("%8.5i",['34']),
            ("%10.5i",['-216']),
            ("%08.5i",['34']),
            ("%.0i",['0']),
            ("%.i",['0']),
            ("%5.0i",['0']),
            ("%-5.0i",['0']),
            ("%-5.0i",['3']),
            ("%-5.0i",['-1']),
        ]
        tests = [
            ("%8.5x",['34']),
            ("%8.5x",['0']),
            ("%08.5x",['34']),
            ("%08.3x",['8375']),
            ("%.0x",['0']),
            ("%.x",['0']),
            ("%5.0x",['0']),
            ("%-5.0x",['0']),
            ("%-5.0x",['3']),
            ("%-5.0x",['-1']),
        ]
        tests = [
            (" %#X ",['-1']),
            (" %#x ",['-1']),
        ]
        tests = [
            ("%70p%70p",['(void*)5454','(void*)9898','(void*)1100']),
            ("%-153p%0110.8x%110p",['(void*)17240180584784891087lu','2705171059u','(void*)1312307382483808423lu']),
        ]
        tests = [
            ("%8p%8p",['(void*)5454','(void*)9898','(void*)1100']),
            ("%-153p%0110.8x%110p",['(void*)17240180584784891087lu','2705171059u','(void*)1312307382483808423lu']),
            ("%197c%12p%013.i%--147.185x%-1c",['7','(void*)18229185041105221837lu','-1488496170','703835510u','120']),
            ("%013.i",['-1488496170']),
            ("%013.i",['1488496170']),
            ("%013.u",['1488496170']),
            ("%.c",["'A'"]),
            ("%.0c",["'A'"]),
            ("%.1c",["'A'"]),
        ]
        tests = [
            ("%#3X",['2']),
            (" %#x ",['-1']),
            ("%014u",['ULONG_MAX']),
            ("%!% 4.2d!",['11']),
            ("%!% 4.2d!",['-11']),
            ("!% 52.11d!",['-1186448278']),
            ("!% 52.11d!",['1186448278']),
            ("42%+48.42d42",['0']),
            ("42%+48.42d42",['-5']),
            ("42%+48.42d42",['5']),
            ("42%+48.42u42",['0']),
            ("% 06d",['0']),
            ("%+06d",['0']),
            ("%06d",['0']),
            ("% 06d",['1']),
            ("%+06d",['1']),
            ("%06d",['1']),
            ("^.^/% .18d^.^/",['0']),
            ("^.^/%- 8.3d^.^/",['0']),
            ("42%- 16.54d42",['0']),
            ("^.^/%0 4.2d^.^/",['0']),
            ("%0 62d",['0']),
        ]
        tests = [
            ("%!% 4.2u!",['11']),
            ("%!% 4.2u!",['-11']),
            ("!% 52.11u!",['-1186448278']),
            ("!% 52.11u!",['1186448278']),
            ("42%+48.42u42",['0']),
            ("42%+48.42u42",['-5']),
            ("42%+48.42u42",['5']),
            ("42%+48.42u42",['0']),
            ("% 06u",['0']),
            ("%+06u",['0']),
            ("%06u",['0']),
            ("% 06u",['1']),
            ("%+06u",['1']),
            ("%06u",['1']),
            ("^.^/% .18u^.^/",['0']),
            ("^.^/%- 8.3u^.^/",['0']),
            ("42%- 16.54u42",['0']),
            ("^.^/%0 4.2u^.^/",['0']),
            ("%0 62u",['0']),
        ]
        tests = [
            ("\\\\!/%#12.9x\\\\!/",['-2140980178']),
            ("\\\\!/%#12.11x\\\\!/",['-2140980178']),
            ("\\\\!/%#15.11x\\\\!/",['-2140980178']),
            ("\\\\!/%#18.13x\\\\!/",['-2140980178']),
            ("^.^/%#10.2x^.^/",['-837177716']),
            ("^.^/%#10.3x^.^/",['-837177716']),
            ("42%0#14x42",['886255058']),
            ("%0#14x",['886255058']),
            ("%0#14.14x",['886255058']),
            ("%0#14.17x",['886255058']),
            ("%0#17.14x",['886255058']),
            ("%014x",['886255058']),
            ("%#014x",['886255058']),
        ]
        for test in tests:
            self.check(*test)
        PrintColor("Cette fonctionnalité n'est pas encore disponible",Colors.RED)
        return False