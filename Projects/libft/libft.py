from BaseLib import *
from BaseExercise import *
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]

PrintColor("Cette correction est cours de creation !", Colors.RED)


class BaseExerciseLibft(BaseExercise):
    def __init__(self, id, file=None):
        super().__init__(id)
        self.path = Config.project_path
        if file==None:
            lst = []
            for i in os.listdir(Config.project_path):
                if i.endswith(("ft_.c",".h")):
                    lst.append(i)
            self.base_files = lst
        else:
            self.base_files = [file,'libft.h']
    
    def Norme(self):
        v = True
        for file in self.base_files:
            v = CheckNorme(Join(self.path,file)) and v
        return v

    def Init(self):
        global Config
        Config.normeflag = ["-R","CheckForbiddenSourceHeader"]
        Config.output_name = "Output"
        Config.valgrind = ValgrindConfig()
        Config.valgrind.active = True
        for file in self.base_files:
            if os.path.isfile(Join(self.path,file)):
                self.files[file] = self.CopyToTemp(file)
        return True


@AddExercise(id="Makefile")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],)
        #return CompileTemp()
        print(self.files)
        return True

    def Execute(self):
        #return ExecuteCode()==0
        return True
    
@AddExercise(id="atoi", file="ft_atoi.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_atoi.c"],"int	ft_atoi(const char *nptr);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_atoi.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    printf("ft_atoi %d\\n",ft_atoi(argv[1]));
    printf("atoi %d\\n",atoi(argv[1]));
    if (ft_atoi(argv[1])==atoi(argv[1]))
        printf("%s","OK\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= ["125", "", "-5", "--8","+9","++9","a38",'12f5g9','-0','2147483647','2147483648',"-2147483648","-2147483649"]
        v = True
        for test in tests:
            print(test)
            r = "OK" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v
    
@AddExercise(id="bzero", file="ft_bzero.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="calloc", file="ft_calloc.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="isalnum", file="ft_isalnum.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="isalpha", file="ft_isalpha.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="isascii", file="ft_isascii.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="isdigit", file="ft_isdigit.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="isprint", file="ft_isprint.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="memchr", file="ft_memchr.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="memcmp", file="ft_memcmp.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="memcpy", file="ft_memcpy.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="memmove", file="ft_memmove.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="memset", file="ft_memset.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strchr", file="ft_strchr.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strdup", file="ft_strdup.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strlcat", file="ft_strlcat.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strlcpy", file="ft_strlcpy.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strlen", file="ft_strlen.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strncmp", file="ft_strncmp.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strnstr", file="ft_strnstr.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strrchr", file="ft_strrchr.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="tolower", file="ft_tolower.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_tolower.c"],"int	ft_tolower(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_tolower.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char c = argv[1][0];
    printf("ft_tolower %c\\n",ft_tolower(c));
    printf("tolower %c\\n",tolower(c));
    if (ft_tolower(c)==tolower(c))
        printf("%s","OK\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= ["1","a","A","z","Z"," ","+"]
        v = True
        for test in tests:
            print(test)
            r = "OK" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="toupper", file="ft_toupper.c")
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_toupper.c"],"int	ft_toupper(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_toupper.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char c = argv[1][0];
    printf("ft_toupper %c\\n",ft_toupper(c));
    printf("toupper %c\\n",toupper(c));
    if (ft_toupper(c)==toupper(c))
        printf("%s","OK\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= ["1","a","A","z","Z"," ","+"]
        v = True
        for test in tests:
            print(test)
            r = "OK" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v
