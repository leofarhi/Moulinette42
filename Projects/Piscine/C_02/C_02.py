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

    def Compile(self):
        AutoMain(self.files["ft_strcpy.c"],"char *ft_strcpy(char *dest, char *src);",
"""
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strcpy.h"
int main(void)
{
    char *dest = malloc(100*sizeof(char));
    ft_strcpy(dest,"Hello World");
    printf("%s",dest);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="Hello World"
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strncpy.c"],"char *ft_strncpy(char *dest, char *src, unsigned int n);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strncpy.h"
int main(void)
{
    char source[] = "Hello, world!";
    char destinationTrue[] = "ABCDEFGHIJKLMNOPQRSTUV";
    char destinationCheck[] = "ABCDEFGHIJKLMNOPQRSTUV";
    int valid = 1;

    strncpy(destinationTrue, source, 5);
    ft_strncpy(destinationCheck, source, 5);
    valid = valid && (strcmp(destinationTrue,destinationCheck)==0);
    //printf("%s\\n",destinationTrue);
    //printf("%s\\n",destinationCheck);

    strncpy(destinationTrue, source, 20);
    ft_strncpy(destinationCheck, source, 20);
    valid = valid && (strcmp(destinationTrue,destinationCheck)==0);
    //printf("%s\\n",destinationTrue);
    //printf("%s\\n",destinationCheck);

    strncpy(destinationTrue, source, 0);
    ft_strncpy(destinationCheck, source, 0);
    valid = valid && (strcmp(destinationTrue,destinationCheck)==0);
    //printf("%s\\n",destinationTrue);
    //printf("%s\\n",destinationCheck);

    strncpy(destinationTrue, source, 13);
    ft_strncpy(destinationCheck, source, 13);
    valid = valid && (strcmp(destinationTrue,destinationCheck)==0);
    //printf("%s\\n",destinationTrue);
    //printf("%s\\n",destinationCheck);
    if (valid)
        printf("OK");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="OK"

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_str_is_alpha.c"],"int ft_str_is_alpha(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_str_is_alpha.h"
int main(void)
{
    int valid = 1;

    valid = valid && ft_str_is_alpha("abscdAGHD");
    if (valid)printf("abscdAGHD OK\\n");
    valid = valid && !ft_str_is_alpha("w45trt");
    if (valid)printf("w45trt OK\\n");
    valid = valid && !ft_str_is_alpha("*5rer");
    if (valid)printf("*5rer OK\\n");
    valid = valid && ft_str_is_alpha("abscdz");
    if (valid)printf("abscdz OK\\n");
    valid = valid && ft_str_is_alpha("AREFZ");
    if (valid)printf("AREFZ OK\\n");
    valid = valid && ft_str_is_alpha("");
    if (valid)printf(" OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 6

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_str_is_numeric.c"],"int ft_str_is_numeric(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_str_is_numeric.h"
int main(void)
{
    int valid = 1;

    valid = valid && !ft_str_is_numeric("abscdAGHD");
    if (valid)printf("abscdAGHD OK\\n");
    valid = valid && !ft_str_is_numeric("w45trt");
    if (valid)printf("w45trt OK\\n");
    valid = valid && !ft_str_is_numeric("*5rer");
    if (valid)printf("*5rer OK\\n");
    valid = valid && ft_str_is_numeric("0123456789");
    if (valid)printf("abscdz OK\\n");
    valid = valid && !ft_str_is_numeric("AREFZ");
    if (valid)printf("AREFZ OK\\n");
    valid = valid && ft_str_is_numeric("");
    if (valid)printf(" OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 6

@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_str_is_lowercase.c"],"int ft_str_is_lowercase(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_str_is_lowercase.h"
int main(void)
{
    int valid = 1;

    valid = valid && !ft_str_is_lowercase("abscdAGHD");
    if (valid)printf("abscdAGHD OK\\n");
    valid = valid && !ft_str_is_lowercase("w45trt");
    if (valid)printf("w45trt OK\\n");
    valid = valid && !ft_str_is_lowercase("*5rer");
    if (valid)printf("*5rer OK\\n");
    valid = valid && !ft_str_is_lowercase("0123456789");
    if (valid)printf("abscdz OK\\n");
    valid = valid && !ft_str_is_lowercase("AREFZ");
    if (valid)printf("abscdz OK\\n");
    valid = valid && ft_str_is_lowercase("adfdfz");
    if (valid)printf("adfdfz OK\\n");
    valid = valid && ft_str_is_lowercase("");
    if (valid)printf(" OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 7

@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_str_is_uppercase.c"],"int ft_str_is_uppercase(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_str_is_uppercase.h"
int main(void)
{
    int valid = 1;

    valid = valid && !ft_str_is_uppercase("abscdAGHD");
    if (valid)printf("abscdAGHD OK\\n");
    valid = valid && !ft_str_is_uppercase("w45trt");
    if (valid)printf("w45trt OK\\n");
    valid = valid && !ft_str_is_uppercase("*5rer");
    if (valid)printf("*5rer OK\\n");
    valid = valid && !ft_str_is_uppercase("0123456789");
    if (valid)printf("abscdz OK\\n");
    valid = valid && ft_str_is_uppercase("AREFZ");
    if (valid)printf("AREFZ OK\\n");
    valid = valid && !ft_str_is_uppercase("adfdfz");
    if (valid)printf("adfdfz OK\\n");
    valid = valid && ft_str_is_uppercase("");
    if (valid)printf(" OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 7

@AddExercise(id="ex06")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_str_is_printable.c"],"int ft_str_is_printable(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_str_is_printable.h"
int main(void)
{
    int valid = 1;

    char val[2] = {31,'\\0'};

    valid = valid && !ft_str_is_printable(val);
    if (valid)printf("31 OK\\n");
    val[0] = 32;
    valid = valid && ft_str_is_printable(val);
    if (valid)printf("32 OK\\n");
    val[0] = 126;
    valid = valid && ft_str_is_printable(val);
    if (valid)printf("126 OK\\n");
    val[0] = 127;
    valid = valid && !ft_str_is_printable(val);
    if (valid)printf("127 OK\\n");
    val[0] = '\\0';
    valid = valid && ft_str_is_printable(val);
    if (valid)printf("0 OK\\n");

    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 5

@AddExercise(id="ex07")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strupcase.c"],"char *ft_strupcase(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strupcase.h"
int main(void)
{
    char e[4] = "";
    char f[100] = "asfg546564#$%$@2ASDDSFaz";
    printf("%s",ft_strupcase(e));
    printf("%s",ft_strupcase(f));
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="asfg546564#$%$@2ASDDSFaz".upper()

@AddExercise(id="ex08")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strlowcase.c"],"char *ft_strlowcase(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strlowcase.h"
int main(void)
{
    char e[4] = "";
    char f[100] = "asfg546564#$%$@2ASDDSFaz";
    printf("%s",ft_strlowcase(e));
    printf("%s",ft_strlowcase(f));
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="asfg546564#$%$@2ASDDSFaz".lower()


@AddExercise(id="ex09")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strcapitalize.c"],"char *ft_strcapitalize(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strcapitalize.h"
int main(void)
{
    char e[4] = "";
    char f[200] = "salut, comment tu vas ? 42mots quarante-deux; cinquante+et+un AHHH! 42AHH";
    printf("%s",ft_strcapitalize(e));
    printf("%s",ft_strcapitalize(f));
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="Salut, Comment Tu Vas ? 42mots Quarante-Deux; Cinquante+Et+Un Ahhh! 42ahh"

@AddExercise(id="ex10")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

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
        return ExecuteCode().count("OK") == 4


def charToHex(char):
    return "\\{0:02x}".format(ord(char))
def intToHex(nb):
    return "\\{0:02x}".format(nb)

@AddExercise(id="ex11")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_putstr_non_printable.c"],"void ft_putstr_non_printable(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putstr_non_printable.h"
int main(void)
{
    unsigned char f[100] = "XXXXCoucou\\n\\t\\rtu vas bien ?";
    f[0] = 255;
    f[1] = 1;
    f[2] = 254;
    f[3] = 127;
    ft_putstr_non_printable((char *)f);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        want = intToHex(255)+intToHex(1)+intToHex(254)+intToHex(127)+"Coucou"+charToHex('\n')+charToHex('\t')+charToHex('\r')+"tu vas bien ?"
        PrintColor("want : %"+want+"%",Colors.YELLOW)
        print("#"*30)
        return ExecuteCode()==want

@AddExercise(id="ex12")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_memory.c"],"void *ft_print_memory(void *addr, unsigned int size);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_print_memory.h"
int main(void)
{
    char f[] = "Bonjour les aminches\\t\\n\\rc. est fou.tout.ce qu on peut faire avec...print_memory....lol.lol. .";
    unsigned int len = strlen(f);
    ft_print_memory((void *)f,len);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        ExecuteCode()
        PrintColor("Cet exercice n'a pas la solution dans la moulinette",Colors.YELLOW)
        return True
