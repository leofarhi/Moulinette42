from BaseLib import *
from BaseExercise import *
from random import randint
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
	printf("#0# %s\\n", ft_strncmp(s1_0,s1_0,0)== strncmp(s1_0,s1_0,0) ? "Success" : "Fail");

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

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        ExecuteCode(canPrint=False)
        Config.valgrind.active = False
        return ExecuteCode().count("Success") == 19

@AddExercise(id="strnstr", file=["ft_strnstr.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

@AddExercise(id="strrchr", file=["ft_strrchr.c"])
class Exo(BaseExerciseLibft):

    def Compile(self):
        #AutoMain(self.files["ft_.c"],"",)
        #return CompileTemp()
        return False

    def Execute(self):
        return ExecuteCode()==0

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
