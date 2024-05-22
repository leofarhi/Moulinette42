from BaseLib import *
from BaseExercise import *
from random import randint
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]

#PrintColor("Cette correction est cours de creation !", Colors.RED)

from . import man

def IsPartResetDico(part):
    global IsPartResetDico
    if len(sys.argv) > 2:
        if sys.argv[2].startswith("part"):
            Exercises.clear()
        if part == sys.argv[2]:
            IsPartResetDico = lambda *args: None

IsPartResetDico('part1')

class BaseExerciseLibft(BaseExercise):
    def __init__(self, id, file=None):
        super().__init__(id)
        self.path = Config.project_path
        if file==None:
            lst = []
            for i in os.listdir(Config.project_path):
                if (os.path.isfile(Join(Config.project_path,i))):
                #if i.endswith((".c",".h")):
                    lst.append(i)
            self.base_files = lst
        else:
            self.base_files = ['libft.h']+file
    
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
            else:
                PrintColor(file + " not exist",Colors.RED)
                return False
        return True


from . import ResTree as ResTree

@AddExercise(id="Makefile")
class Exo(BaseExerciseLibft):
    
    def GetFiles(self, path):
        return os.listdir(path)
    
    def eq_lst(self,lst1,lst2):
        return sorted(lst1) == sorted(lst2)
    
    def Norme(self):
        v = True
        for file in self.base_files:
            if "Makefile" == file: continue
            v = CheckNorme(Join(self.path,file)) and v
        return v

    def Compile(self):
        v = True
        with_bonus = True in ['_bonus' in i for i in os.listdir(Config.temp_path)]
        PrintColor('Bonus: '+(['Non','Oui'][with_bonus]),Colors.PURPLE)
        if with_bonus:
            resTree = ResTree.ResTreeBonus
        else:
            resTree = ResTree.ResTreeBase
        print("#"*5,"make","#"*5)
        print(Process(["make"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make,self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make fclean","#"*5)
        print(Process(["make","fclean"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make_fclean,self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make all","#"*5)
        print(Process(["make","all"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make_all,self.GetFiles(Config.temp_path))) and v
    
        print("#"*5,"make clean","#"*5)
        print(Process(["make","clean"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make_clean,self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make re","#"*5)
        print(Process(["make","re"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make_re,self.GetFiles(Config.temp_path))) and v
    
        print("#"*5,"make fclean","#"*5)
        print(Process(["make","fclean"],cwd=Config.temp_path))

        print("#"*5,"make libft.a","#"*5)
        print(Process(["make","libft.a"],cwd=Config.temp_path))
        PrintTree()
        #print(self.GetFiles(Config.temp_path))  
        v = IfValid(self.eq_lst(resTree.make_libft_a,self.GetFiles(Config.temp_path))) and v

        if with_bonus:
            print("#"*5,"make fclean","#"*5)
            print(Process(["make","fclean"],cwd=Config.temp_path))

            print("#"*5,"make bonus","#"*5)
            print(Process(["make","bonus"],cwd=Config.temp_path))
            PrintTree()
            #print(self.GetFiles(Config.temp_path))  
            v = IfValid(self.eq_lst(resTree.make_bonus,self.GetFiles(Config.temp_path))) and v

            print("#"*5,"make clean bonus","#"*5)
            print(Process(["make","clean"],cwd=Config.temp_path))
            PrintTree()
            #print(self.GetFiles(Config.temp_path))  
            v = IfValid(self.eq_lst(resTree.make_clean_bonus,self.GetFiles(Config.temp_path))) and v

        #print(self.GetFiles(Config.temp_path))    
        return v
        return "libft.a" in os.listdir(Config.temp_path)

    def Execute(self):
        return True
    
@AddExercise(id="atoi", file=["ft_atoi.c"])
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
    else
        printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [" \t\v\n\r\f9","     -5","125", "", "-5","+-5","-+5", "--8","+9","++9","a38",'12f5g9','-0','2147483647','2147483648',"-2147483648","-2147483649"]
        v = True
        for test in tests:
            print(test)
            r = "OK" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v
    
@AddExercise(id="bzero", file=["ft_bzero.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_bzero.c"],"void	ft_bzero(void *s, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_bzero.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char *str1 = strdup(argv[1]);
    char *str2 = strdup(argv[1]);
    size_t len = strlen(argv[1]);
    ft_bzero(str1,len);
    bzero(str2,len);
    printf("res: %s\\n",str1);
    if (memcmp(str1,str2,len) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(str1);
    free(str2);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [""]
        for i in range(10):
            t = ""
            for o in range(randint(0,80)):
                t+=chr(randint(32,126))
            tests.append(t)
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="calloc", file=["ft_calloc.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_calloc.c"],"void	*ft_calloc(size_t nmemb, size_t size);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_calloc.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    size_t nmemb = (size_t)atoll(argv[1]);
    size_t size = (size_t)atoll(argv[2]);
    printf("%lu %lu\\n",nmemb, size);
    void *tab = ft_calloc(nmemb,size);
    printf("%p\\n", tab);
    void *tab2 = calloc(nmemb,size);
    printf("%p\\n", tab2);
    /*if ((tab == NULL || tab2 == NULL) && (tab != NULL || tab2 != NULL))
    {
        printf("Not same behavior Calloc");
        return (0);
    }*/
    if (tab == NULL)
        printf("NULL");
    else if (size*nmemb > 0)
        printf(memcmp(tab,tab2,size*nmemb) == 0 ? "OK" : "WRONG");
    else
        printf("OK");
    if (tab != NULL) free(tab);
    if (tab2 != NULL) free(tab2);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        #Config.valgrind.active = False
        #Config.valgrind.print = True
        tests= [
            ["0","0"],
            ["1","0"],
            ["0","1"],
            ["1","1"],
            ["10","4"],
            ["4","10"],
            ["65536","2"],
            ["2","4294967295"],
            ["4294967295","2"],
            ["4294967295","4294967295"],
        ]
        res=[
            "OK",
            "OK",
            "OK",
            "OK",
            "OK",
            "OK",
            "OK",
            "NULL",
            "NULL",
            "NULL",
        ]
        v = True
        for idx,test in enumerate(tests):
            print(test)
            r = res[idx] in ExecuteCode(args=test)
            if r:
                PrintColor("OK", Colors.GREEN)
            else:
                PrintColor("WRONG", Colors.RED)
            v = v and r
            print("-"*10)
        return v

@AddExercise(id="isalnum", file=["ft_isalnum.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_isalnum.c"],"int	ft_isalnum(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_isalnum.h"
                 
int main(void)
{
    for (int i = -128; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_isalnum %d,",ft_isalnum(c));
		printf("isalnum %d,",isalnum(c));
		if ((ft_isalnum(c) > 0) == (isalnum(c) > 0))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 256


@AddExercise(id="isalpha", file=["ft_isalpha.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_isalpha.c"],"int	ft_isalpha(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_isalpha.h"
                 
int main(void)
{
    for (int i = -128; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_isalpha %d,",ft_isalpha(c));
		printf("isalpha %d,",isalpha(c));
		if ((ft_isalpha(c) > 0) == (isalpha(c) > 0))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 256

@AddExercise(id="isascii", file=["ft_isascii.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_isascii.c"],"int	ft_isascii(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_isascii.h"
                 
int main(void)
{
    for (int i = -128; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_isascii %d,",ft_isascii(c));
		printf("isascii %d,",isascii(c));
		if ((ft_isascii(c) > 0) == (isascii(c) > 0))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 256

@AddExercise(id="isdigit", file=["ft_isdigit.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_isdigit.c"],"int	ft_isdigit(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_isdigit.h"
                 
int main(void)
{
    for (int i = -128; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_isdigit %d,",ft_isdigit(c));
		printf("isdigit %d,",isdigit(c));
		if ((ft_isdigit(c) > 0) == (isdigit(c) > 0))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 256

@AddExercise(id="isprint", file=["ft_isprint.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_isprint.c"],"int	ft_isprint(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_isprint.h"
                 
int main(void)
{
    for (int i = -128; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_isprint %d,",ft_isprint(c));
		printf("isprint %d,",isprint(c));
		if ((ft_isprint(c) > 0) == (isprint(c) > 0))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 256

@AddExercise(id="memchr", file=["ft_memchr.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_memchr.c"],"void	*ft_memchr(const void *s, int c, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_memchr.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    unsigned char *str = (unsigned char *)argv[1];
    int c = (int)argv[2][0];
    size_t n = strlen(argv[1]);
    long int res = (unsigned char *)ft_memchr(str,c,n) - str;
    printf("ft_memchr %ld\\n",res < 0 ? -1 : res);
    if (memchr(str,c,n) == ft_memchr(str,c,n))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [["","a"],["b","a"],["a","a"]]
        for i in range(10):
            t = ""
            for o in range(randint(40,80)):
                t+=chr(randint(32,126))
            tests.append([t,chr(randint(32,126))])
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="memcmp", file=["ft_memcmp.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_memcmp.c"],"int	ft_memcmp(const void *s1, const void *s2, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_memcmp.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    unsigned char *str = (unsigned char *)argv[1];
    unsigned char *str2 = (unsigned char *)argv[2];
    size_t n = strlen(argv[1]);
    printf("ft_memcmp %d\\n",ft_memcmp(str,str2,n));
    if (memcmp(str,str2,n) == ft_memcmp(str,str2,n))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [["","a"],["b","a"],["a","a"],["a","b"],["aa","a"],["a","aa"],["aA","aa"],["aa","aA"]]
        for i in range(10):
            t = ""
            for o in range(randint(40,80)):
                t+=chr(randint(32,126))
            t2 = ""
            for o in range(randint(40,80)):
                t2+=chr(randint(32,126))
            tests.append([t,t2])
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="memcpy", file=["ft_memcpy.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_memcpy.c"],"void	*ft_memcpy(void *dest, const void *src, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_memcpy.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    unsigned char *str = (unsigned char *)argv[1];
    size_t n = strlen(argv[1]);
    unsigned char *cp1 = malloc(n);
    unsigned char *cp2 = malloc(n);
    ft_memcpy(cp1,str,n);
    memcpy(cp2,str,n);
    if (memcmp(cp1,cp2,n) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(cp1);
    free(cp2);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [""]
        for i in range(10):
            t = ""
            for o in range(randint(40,80)):
                t+=chr(randint(32,126))
            tests.append(t)
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="memmove", file=["ft_memmove.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_memmove.c"],"void	*ft_memmove(void *dest, const void *src, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_memmove.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    unsigned char *str = (unsigned char *)argv[1];
    size_t n = strlen(argv[1]);
    int decal = atoi(argv[2]);
    int size = n*2 + abs(decal) + 1;
    unsigned char *cp1 = malloc(size);
    unsigned char *cp2 = malloc(size);
    memset(cp1,'#',size); memset(cp2,'#',size);
    cp1[size-1] = 0; cp2[size-1] = 0;
    memcpy((char *)cp1 + (decal < 0 ? abs(decal) : 0),(char *)str,n);
    memcpy((char *)cp2 + (decal < 0 ? abs(decal) : 0),(char *)str,n);
    printf("mem:       %s\\n",cp1);
    if (decal < 0)
    {
        ft_memmove(cp1,cp1+abs(decal),n);
        memmove(cp2,cp2+abs(decal),n);
    }
    else
    {
        ft_memmove(cp1+abs(decal),cp1,n);
        memmove(cp2+abs(decal),cp2,n);
    }
    printf("ft_memmove %s\\n",cp1);
    printf("memmove    %s\\n",cp2);
    if (memcmp(cp1,cp2,size) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(cp1);
    free(cp2);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [["","-5"],["","5"],["a","1"],["a","-1"],["a","0"], ["aBC","1"],["aBC","-1"],["aBC","0"],["aBC","5"],["aBC","-5"]]
        for i in range(10):
            t = ""
            for o in range(randint(0,20)):
                t+=chr(randint(36,126))
            tests.append([t,str(randint(-10,10))])
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="memset", file=["ft_memset.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_memset.c"],"void	*ft_memset(void *s, int c, size_t n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_memset.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char *str = argv[1];
    size_t n = strlen(str);
    char *cp1 = strdup(str);
    char *cp2 = strdup(str);
    int c = argv[2][0];
    printf("str:      %s\\n",str);
    printf("c:        %c\\n",c);
    ft_memset(cp1,c,n);
    memset(cp2,c,n);
    printf("ft_memset %s\\n",cp1);
    printf("memset    %s\\n",cp2);
    if (memcmp(cp1,cp2,n) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(cp1);
    free(cp2);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [["","*"],["Hello","*"],["Hello","a"]]
        for i in range(10):
            t = ""
            for o in range(randint(0,80)):
                t+=chr(randint(32,126))
            tests.append([t,chr(randint(32,126))])
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="strchr", file=["ft_strchr.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strchr.c"],"char	*ft_strchr(const char *s, int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_strchr.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char c = (char)atoi(argv[2]);
    char *str = argv[1];
    printf("ft_strchr %p\\n",ft_strchr(str,c));
    printf("strchr    %p\\n",strchr(str,c));
    if (ft_strchr(str,c) == strchr(str,c))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [["",str(ord(" "))],["","0"],["abcde",str(ord("A"))],["abcdeA",str(ord("A"))],["AabcdeA",str(ord("A"))],["AabcdeA","0"]]
        for i in range(10):
            t = ""
            for o in range(randint(40,80)):
                t+=chr(randint(32,126))
            tests.append([t,str(randint(-1,128))])
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="strdup", file=["ft_strdup.c","ft_strlen.c","ft_strlcpy.c","ft_memcpy.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strdup.c"],"char	*ft_strdup(const char *s);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strdup.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char *str = argv[1];
    char *cp1 = strdup(str);
    printf("str:      %s\\n",str);
    printf("ft_strdup %s\\n",cp1);
    int n = strlen(str);
    if (memcmp(cp1,str,n+1) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(cp1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= ["", "Hello"]
        for i in range(10):
            t = ""
            for o in range(randint(0,80)):
                t+=chr(randint(32,126))
            tests.append(t)
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="strlcat", file=["ft_strlcat.c","ft_strlen.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strlcat.c"],"unsigned int ft_strlcat(char *dest, char *src, unsigned int size);",
"""
#include <stdio.h>
#include <bsd/string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strlcat.h"
int main(void)
{
    char s1a[20] = "Test1";
	char s2a[] = "OK";
	char s1b[20] = "Test1";
	char s2b[] = "OK";
	char s3a[20] = "Same";
	char s4a[] = "Size";
	char s3b[20] = "Same";
	char s4b[] = "Size";
	char s5a[20] = "Shorter";
	char s6a[] = "ThanMyself";
	char s5b[20] = "Shorter";
	char s6b[] = "ThanMyself";
	char s7a[20] = "Shorter";
	char s8a[] = "ThanMyself";
	char s7b[20] = "Shorter";
	char s8b[] = "ThanMyself";

	printf("#1# %s\\n", ft_strlcat(s1a, s2a, 6) == strlcat(s1b, s2b, 6) ? "Success" : "Fail");
	printf("#2# %s\\n", strcmp(s1a, s1b) == 0 && strcmp(s2a, s2b) == 0 ? "Success" : "Fail");
	printf("#3# %s\\n", ft_strlcat(s3a, s4a, 10) == strlcat(s3b, s4b, 10) ? "Success" : "Fail");
	printf("#4# %s\\n", strcmp(s3a, s3b) == 0 && strcmp(s4a, s4b) == 0 ? "Success" : "Fail");
    unsigned int a = ft_strlcat(s5a, s6a, 4);
    unsigned int b = strlcat(s5b, s6b, 4);
	printf("#5# %s\\n", a == b ? "Success" : "Fail");
	printf("#6# %s\\n", strcmp(s5a, s5b) == 0 && strcmp(s6a, s6b) == 0 ? "Success" : "Fail");
	printf("#7# %s\\n", ft_strlcat(s7a, s8a, 0) == strlcat(s7b, s8b, 0) ? "Success" : "Fail");
	printf("#8# %s\\n", strcmp(s7a, s7b) == 0 && strcmp(s8a, s8b) == 0 ? "Success" : "Fail");
    return (0);
}
""")
        return CompileTemp(lib="-lbsd")

    def Execute(self):
        ExecuteCode(canPrint=False)
        Config.valgrind.active = False
        return ExecuteCode().count("Success") == 8

@AddExercise(id="strlcpy", file=["ft_strlcpy.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strlcpy.c"],"unsigned int ft_strlcpy(char *dest, char *src, unsigned int size);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strlcpy.h"
int main(void)
{
    char source[] = "Hello, world!";
    char destinationCheck[] = "ABCDEFGHIJKLMNOPQRSTUV";
    int valid = 1;
    unsigned int len = strlen(source);
    unsigned int res2 = 0;

    res2 = ft_strlcpy(destinationCheck, source, len+1);
    valid = valid && (strcmp(source,destinationCheck)==0) && len==res2;
    if (valid)
        printf("OK\\n");

    char destinationCheck2[] = "ABCDEFGHIJKLMNOPQRSTUV";
    res2 = ft_strlcpy(destinationCheck2, source, len+5);
    valid = valid && (strcmp(source,destinationCheck2)==0) && len==res2;
    if (valid)
        printf("OK\\n");

    char destinationCheck3[] = "ABC";
    unsigned int len2 = strlen(destinationCheck3);
    res2 = ft_strlcpy(destinationCheck3, source, len2+1);
    valid = valid && (strcmp("Hel",destinationCheck3)==0) && len==res2;
    if (valid)
        printf("OK\\n");

    char destinationCheck4[] = "";
    unsigned int len3 = strlen(destinationCheck4);
    res2 = ft_strlcpy(destinationCheck4, source, len3);
    valid = valid && (strcmp("",destinationCheck4)==0) && len==res2;
    if (valid)
        printf("OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        ExecuteCode(canPrint=False)
        Config.valgrind.active = False
        return ExecuteCode().count("OK") == 4

@AddExercise(id="strlen", file=["ft_strlen.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strlen.c"],"size_t	ft_strlen(const char *s);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strlen.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    printf("ft_strlen %zu\\n",ft_strlen(argv[1]));
    printf("strlen %lu\\n",strlen(argv[1]));
    if (ft_strlen(argv[1])==(size_t)strlen(argv[1]))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [""]
        for i in range(10):
            t = ""
            for o in range(randint(0,80)):
                t+=chr(randint(32,126))
            tests.append(t)
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="strncmp", file=["ft_strncmp.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strncmp.c"],"int	ft_strncmp(const char *s1, const char *s2, size_t n);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strncmp.h"
int main(void)
{
	char s0_0[5] = "";
    char s1_0[] = "a";
	char s2_0[] = "aaa";
	char s3_0[] = "ddd";
	char s4_0[] = "ad";
	char s5_0[] = "c";
	char s6_0[] = "bd";
	char s7_0[] = "b";
	char s8_0[] = "bqq";

	printf("%d, %d\\n", ft_strncmp(s0_0,s1_0,1), strncmp(s0_0,s1_0,1));
	printf("#0# %s\\n", ft_strncmp(s0_0,s1_0,1)== strncmp(s0_0,s1_0,1) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s1_0,s1_0,0), strncmp(s1_0,s1_0,0));
	printf("#0 bis# %s\\n", ft_strncmp(s1_0,s1_0,0)== strncmp(s1_0,s1_0,0) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s1_0,s1_0,1), strncmp(s1_0,s1_0,1));
	printf("#1# %s\\n", ft_strncmp(s1_0,s1_0,1)== strncmp(s1_0,s1_0,1) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s2_0,s3_0,1), strncmp(s2_0,s3_0,1));
	printf("#2# %s\\n", ft_strncmp(s2_0,s3_0,1)== strncmp(s2_0,s3_0,1) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s4_0,s5_0,2), strncmp(s4_0,s5_0,2));
	printf("#3# %s\\n", ft_strncmp(s4_0,s5_0,2)== strncmp(s4_0,s5_0,2) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s6_0,s7_0,1), strncmp(s6_0,s7_0,1));
	printf("#4# %s\\n", ft_strncmp(s6_0,s7_0,1)== strncmp(s6_0,s7_0,1) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s6_0,s8_0,2), strncmp(s6_0,s8_0,2));
	printf("#5# %s\\n", ft_strncmp(s6_0,s8_0,2)== strncmp(s6_0,s8_0,2) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s6_0,s8_0,0), strncmp(s6_0,s8_0,0));
	printf("#6# %s\\n", ft_strncmp(s6_0,s8_0,0)== strncmp(s6_0,s8_0,0) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s6_0,s7_0,3), strncmp(s6_0,s7_0,3));
	printf("#7# %s\\n", ft_strncmp(s6_0,s7_0,3)== strncmp(s6_0,s7_0,3) ? "Success" : "Fail");

    printf("%d, %d\\n", ft_strncmp(s7_0,s6_0,3), strncmp(s7_0,s6_0,3));
	printf("#8# %s\\n", ft_strncmp(s7_0,s6_0,3)== strncmp(s7_0,s6_0,3) ? "Success" : "Fail");

    char s1[] = "Test1";
	char s2[] = "OK";
	char s3[] = "Same";
	char s4[] = "Size";
	char s5[] = "Shorter";
	char s6[] = "ThanMyself";
	char s7[] = "ShorterTest";

	printf("%d, %d\\n", ft_strncmp(s1, s2, 4), strncmp(s1, s2, 4));
	printf("#9# %s\\n", ft_strncmp(s1, s2, 4)== strncmp(s1, s2, 4) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s1, s2, 2), strncmp(s1, s2, 2));
	printf("#10# %s\\n", ft_strncmp(s1, s2, 2)== strncmp(s1, s2, 2) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s3, s4, 4), strncmp(s3, s4, 4));
	printf("#11# %s\\n", ft_strncmp(s3, s4, 4)== strncmp(s3, s4, 4) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s3, s4, 1), strncmp(s3, s4, 1));
	printf("#12# %s\\n", ft_strncmp(s3, s4, 1)== strncmp(s3, s4, 1) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s5, s6, 3), strncmp(s5, s6, 3));
	printf("#13# %s\\n", ft_strncmp(s5, s6, 3)== strncmp(s5, s6, 3) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s5, s5, 10), strncmp(s5, s5, 10));
	printf("#14# %s\\n", ft_strncmp(s5, s5, 10)== strncmp(s5, s5, 10) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s5, s5, 5), strncmp(s5, s5, 5));
	printf("#15# %s\\n", ft_strncmp(s5, s5, 5)== strncmp(s5, s5, 5) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s5, s7, 7), strncmp(s5, s7, 7));
	printf("#16# %s\\n", ft_strncmp(s5, s7, 7)== strncmp(s5, s7, 7) ? "Success" : "Fail");

	printf("%d, %d\\n", ft_strncmp(s5, s7, 8), strncmp(s5, s7, 8));
	printf("#17# %s\\n", ft_strncmp(s5, s7, 8)== strncmp(s5, s7, 8) ? "Success" : "Fail");
    
    
    char s1_1[] = "abcdef";
    char s2_1[] = "abc\\375xx";
    char s3_1[] = "\\200";
    char s4_1[] = "\\0";
    char s5_1[] = "\\x12\\xff\\x65\\x12\\xbd\\xde\\xad";
    char s6_1[] = "\\x12\\x02";
    
    printf("%d, %d\\n", ft_strncmp(s1_1, s2_1, 5), strncmp(s1_1, s2_1, 5));
	printf("#18# %s\\n", ft_strncmp(s1_1, s2_1, 5)== strncmp(s1_1, s2_1, 5) ? "Success" : "Fail");
    
    printf("%d, %d\\n", ft_strncmp(s3_1, s4_1, 1), strncmp(s3_1, s4_1, 1));
	printf("#19# %s\\n", ft_strncmp(s3_1, s4_1, 1)== strncmp(s3_1, s4_1, 1) ? "Success" : "Fail");
    
    printf("%d, %d\\n", ft_strncmp(s5_1, s6_1, 6), strncmp(s5_1, s6_1, 6));
	printf("#20# %s\\n", ft_strncmp(s5_1, s6_1, 6)== strncmp(s5_1, s6_1, 6) ? "Success" : "Fail");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        ExecuteCode(canPrint=False)
        Config.valgrind.active = False
        return ExecuteCode().count("Success") == 22

@AddExercise(id="strnstr", file=["ft_strnstr.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strnstr.c"],"char	*ft_strnstr(const char *big, const char *little, size_t len);","""
#include <stdio.h>
#include <bsd/string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_strnstr.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char* big = argv[1];
    char* little = argv[2];
    size_t len = atoi(argv[3]);
    printf("ft_strnstr %s\\n",ft_strnstr(big,little,len));
    printf("strnstr    %s\\n",strnstr(big,little,len));
    if (ft_strnstr(big,little,len) == strnstr(big,little,len))
		printf("%s","OK\\n");
	else
		printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp(lib="-lbsd -lc")

    def Execute(self):
        tests= [
            ["","",0],
            ["","",5],
            ["","aa",5],
            ["aa","",5],
            ["aa","a",5],
            ["aa","a",0],
            ["aafgbsfgfdghjhrgghbsd","9",10],
            ["aafgbsfgfdghjhrgghbsd","gfdg",4],
            ["aafgbsfgfdghjhrgghbsd","gfdg",40],
            ["aafgbsfgfdghjhrgghbsd","gfdg",2],
            ["aafgbsfgfdghjhrgghbsd","afg",2],
                ]
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[str(i) for i in test])
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="strrchr", file=["ft_strrchr.c","ft_strlen.c",])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strrchr.c"],"char	*ft_strrchr(const char *s, int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_strrchr.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    char* str = argv[1];
    if (strcmp(str,"NULL")==0)
        str = NULL;
    int c = atoi(argv[2]);
    int int_res = atoi(argv[3]);
    printf("%s %c %d\\n",str,c,int_res);
    char* res = (int_res >= 0)? str+int_res : NULL;
    printf("ft_strrchr %s\\n",ft_strrchr(str, c));
    printf("res        %s\\n",res);
    if (ft_strrchr(str, c) == res)
		printf("%s","OK\\n");
	else
		printf("%s","WRONG\\n");
    return (0);
}
""")
        return CompileTemp()
    
    def solve(self,test):
        if test[0] == "NULL":
            test[0] = ""
        txt = str((test[0])[::-1])
        txt = [ord(i) for i in txt]
        idx = len(txt) - txt.index(test[1]) - 1 if test[1] in txt else -1
        if test[1] == 0:
            idx = len(txt)
        test.append(idx)
        test = [str(i) for i in test]
        return test
    def Execute(self):
        #Config.valgrind.print = True
        tests= [
            ["",0],
            ["AAAA",0],
            ["",ord('A')],
            ["AAAA",ord('B')],
            ["BAAAA",ord('B')],
            ["AABAA",ord('B')],
            ["AABjhdBjhfdBAA",ord('B')],
            ["AABjhdBjhfdBAAB",ord('B')],
            ["NULL",0],
            ["NULL",ord('A')],
                ]
        tests = [self.solve(i) for i in tests]
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=test)
            v =  r and v
            print("-"*10)
        return v

@AddExercise(id="tolower", file=["ft_tolower.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_tolower.c"],"int	ft_tolower(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_tolower.h"
                 
int main(void)
{
    for (int i = 0; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_tolower %d,",ft_tolower(c));
		printf("tolower %d,",tolower(c));
		if (ft_tolower(c)==tolower(c))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 128

@AddExercise(id="toupper", file=["ft_toupper.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_toupper.c"],"int	ft_toupper(int c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include "ft_toupper.h"
                 

int main(void)
{
    for (int i = 0; i < 128; i++)
    {
        char c = (char)i; 
		printf("ft_toupper %d,",ft_toupper(c));
		printf("toupper %d,",toupper(c));
		if (ft_toupper(c)==toupper(c))
			printf("%s","OK | ");
        else
            printf("%s","WRONG | ");
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count('OK') == 128













IsPartResetDico('part2')





@AddExercise(id="itoa", file=["ft_itoa.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_itoa.c"],"char	*ft_itoa(int n);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_itoa.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    int nb = atoi(argv[1]);
    printf("nb:      $%d$\\n",nb);
    char *res = ft_itoa(nb);
    printf("ft_itoa  $%s$\\n",res);
    if (strcmp(res,argv[1]) == 0)
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(res);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [0, -1 , 1, 20, 2147483647, -2147483648]
        for i in range(10):
            t = randint(-2147483648,2147483647)
            tests.append(t)
        v = True
        tests = [str(i) for i in tests]
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[test])
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="putchar_fd", file=["ft_putchar_fd.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_putchar_fd.c"],"void	ft_putchar_fd(char c, int fd);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putchar_fd.h"
                 
int main(void)
{
    ft_putchar_fd('O',1);
    ft_putchar_fd('K',1);
    ft_putchar_fd('\\n',1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return "OK\n" in ExecuteCode()


@AddExercise(id="putendl_fd", file=["ft_putendl_fd.c","ft_putstr_fd.c","ft_putchar_fd.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_putendl_fd.c"],"void	ft_putendl_fd(char *s, int fd);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putendl_fd.h"
                 
int main(void)
{
    ft_putendl_fd("OK",1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return "OK\n" in ExecuteCode()


@AddExercise(id="putnbr_fd", file=["ft_putnbr_fd.c","ft_putchar_fd.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_putnbr_fd.c"],"void	ft_putnbr_fd(int n, int fd);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putnbr_fd.h"
                 
int main(int argc, char **argv)
{
    (void)argc;
    int nb = atoi(argv[1]);
    ft_putnbr_fd(nb, 1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests= [0, -1 , 1, 20, 2147483647, -2147483648, 147483647, -147483647]
        for i in range(10):
            t = randint(-2147483648,2147483647)
            tests.append(t)
        v = True
        tests = [str(i) for i in tests]
        for test in tests:
            print(test)
            r = test == ExecuteCode(args=[test])
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="putstr_fd", file=["ft_putstr_fd.c","ft_putchar_fd.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_putstr_fd.c"],"void	ft_putstr_fd(char *s, int fd);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putstr_fd.h"
                 
int main(void)
{
    ft_putstr_fd("OK\\n",1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return "OK\n" in ExecuteCode()


@AddExercise(id="split", file=["ft_split.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_split.c"],"char	**ft_split(char const *s, char c);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_split.h"

int main(int argc, char **argv)
{
    if (argc < 3)
        return (0);
    char **res = ft_split(argv[1],argv[2][0]);
    printf("###############\\n");
    int i = 0;
    while (res[i] != 0)
        printf("#%s#\\n",res[i++]);
    printf("###############\\n");
    i = 0;
    printf("#");
    while (res[i] != 0)
        printf("%s|",res[i++]);
    printf("#\\n");
    i = 0;
    while (res[i] != 0)
        free(res[i++]);
    free(res);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests = [
    ["aa,bb,cc", ","],
    ["aa", ","],
    ["aa,,,,,b,b,c", ","],
    ["dd,e,e f", ","],
    ["Yaa!", "!"],
    ["HelloYaa!World", "a"],
    ["", ","],
    ["Ya;a!", ";"],
    ["Ya;a!", "Y"],
    ["", ","],
    ["hello!", " "],
        ]
        v = True
        for test in tests:
            print(test)
            expected = "|".join([x for x in test[0].split(test[1][0]) if x])
            expected = "#"+expected+("|" if len(expected) > 0 else "")+"#"
            print("expected :", expected)
            r = expected in ExecuteCode(args=test)
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="striteri", file=["ft_striteri.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_striteri.c"],"void	ft_striteri(char *s, void (*f)(unsigned int, char*));","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_striteri.h"
                 
void cesar(unsigned int idx, char* c)
{
    *c = ((*c + idx) % 26) + 'a';
}

int main(int argc, char **argv)
{
    (void)argc;
    char *str = strdup(argv[1]);
    ft_striteri(str,&cesar);
    printf("%s\\n",str);
    free(str);
    return (0);
}
""")
        return CompileTemp()
    
    def cesar(self, txt):
        nexTxt = ""
        for idx,c in enumerate(txt):
            nexTxt += chr(((ord(c) + idx) % 26) + ord('a'))
        return nexTxt

    def Execute(self):
        tests= ["azAZyywtgefgsdgfgshfgAIUISDShhgeryrgyer56565645"]
        v = True
        tests = [str(i) for i in tests]
        for test in tests:
            print(test)
            expected = self.cesar(test)
            PrintColor("expected :\n"+expected,Colors.YELLOW)
            r = expected+"\n" == ExecuteCode(args=[test])
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="strjoin", file=["ft_strjoin.c","ft_strlen.c","ft_strlcpy.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strjoin.c"],"char	*ft_strjoin(char const *s1, char const *s2);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strjoin.h"

int main(int argc, char **argv)
{
    (void)argc;
    char *res = ft_strjoin(argv[1],argv[2]);
    printf("%s\\n",res);
    free(res);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests = [
    [", ", "aaa"],
    ["Hello ", "World"],
    ["a",""],
    ["a","",""],
    ["", "aaa"],
    ["", ""]
]
        v = True
        for test in tests:
            print(test)
            expected = ''.join(test)
            PrintColor("expected :\n"+expected,Colors.YELLOW)
            r = expected+"\n" == ExecuteCode(args=test)
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="strmapi", file=["ft_strmapi.c","ft_strlen.c","ft_strlcpy.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strmapi.c"],"char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strmapi.h"
                 
char cesar(unsigned int idx, char c)
{
    return ((c + idx) % 26) + 'a';
}

int main(int argc, char **argv)
{
    (void)argc;
    char *str = ft_strmapi(argv[1],&cesar);
    printf("%s\\n",str);
    free(str);
    return (0);
}
""")
        return CompileTemp()
    
    def cesar(self, txt):
        nexTxt = ""
        for idx,c in enumerate(txt):
            nexTxt += chr(((ord(c) + idx) % 26) + ord('a'))
        return nexTxt

    def Execute(self):
        tests= ["azAZyywtgefgsdgfgshfgAIUISDShhgeryrgyer56565645"]
        v = True
        tests = [str(i) for i in tests]
        for test in tests:
            print(test)
            expected = self.cesar(test)
            PrintColor("expected :\n"+expected,Colors.YELLOW)
            r = expected+"\n" == ExecuteCode(args=[test])
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v


@AddExercise(id="strtrim", file=["ft_strtrim.c","ft_strlcpy.c","ft_strlen.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_strtrim.c"],"char	*ft_strtrim(char const *s1, char const *set);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strtrim.h"
                 
void Check(char *s1, char *want, char *trim)
{
    char *ret = ft_strtrim(s1, trim);
                 
    printf("-s1:#%s#\\n-want:#%s#\\n-res:#%s#\\n",s1,want,ret);
 
 	if (!strcmp(ret, want))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(ret);
}

int main(void)
{
 	Check("   \\t  \\n\\n \\t\\t  \\n\\n\\nHello \\t  Please\\n Trim me ! !\\n   \\n \\n \\t\\t\\n  ",
          "Hello \\t  Please\\n Trim me ! !",
          " \\n\\t");
    Check("",
          "",
          "");
    Check("&&&&&&",
          "",
          "&");
    Check("&*&*&*&*HELLO*&*&*&*",
          "HELLO",
          "&*");
    Check("&HELLO*",
          "HELLO",
          "&*");
    Check("&HELLO*",
          "&HELLO*",
          "");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK\n") == 6


@AddExercise(id="substr", file=["ft_substr.c","ft_strlcpy.c","ft_memcpy.c","ft_strlen.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        AutoMain(self.files["ft_substr.c"],"char	*ft_substr(char const *s, unsigned int start, size_t len);","""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_substr.h"
                 
void Check()
{
    
}

int main(int argc, char **argv)
{
    (void)argc;
    char *str = argv[1];
    unsigned int start = atoll(argv[2]);
    size_t size = atoll(argv[3]);
    char *want = argv[4];
 	char *ret = ft_substr(str, start, size);
    printf("-str:#%s#\\t-start:%u\\t-size:%lu\\n",str,start,size);
    printf("-want:#%s#\\n-res :#%s#\\n",want,ret);
 
 	if (!strcmp(ret, want))
        printf("%s","OK\\n");
    else
        printf("%s","WRONG\\n");
    free(ret);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests = [
    ["",0,0,""],
    ["abc",1,1,"b"],
    ["i just want this part $$$$$$$$$$$$$",0,22,"i just want this part "],
    ["abcd",2,10,"cd"],
    ["abcd",4,10,""],
    ["hola",4294967295,0,""],
    ["hola",0,18446744073709551615,"hola"],
]
        v = True
        for test in tests:
            print(test)
            r = "OK\n" in ExecuteCode(args=[str(i) for i in test])
            PrintColor(*([('Wrong',Colors.RED),('OK',Colors.GREEN)][int(r)]))
            v =  r and v
            print("-"*10)
        return v

IsPartResetDico('part3')


if len(sys.argv) > 2 and sys.argv[2].startswith("part"):
    sys.argv = sys.argv[:2]