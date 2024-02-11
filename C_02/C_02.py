from BaseLib import *
Config.PATH_git = GetGitPath("C_02")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")


######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_strcpy.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strcpy(char *dest, char *src);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="Hello World"
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 0")
print("#"*40)
print("")


######################
#Exo 1
######################
ResetTempDir()
print("#"*15,"Exo 1 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex01/ft_strncpy.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strncpy(char *dest, char *src, unsigned int n);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="OK"
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 1")
print("#"*40)
print("")



######################
#Exo 2
######################
ResetTempDir()
print("#"*15,"Exo 2 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex02/ft_str_is_alpha.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_str_is_alpha(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("\n") == 6
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 2")
print("#"*40)
print("")



######################
#Exo 3
######################
ResetTempDir()
print("#"*15,"Exo 3 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex03/ft_str_is_numeric.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_str_is_numeric(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("\n") == 6
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 3")
print("#"*40)
print("")


######################
#Exo 4
######################
ResetTempDir()
print("#"*15,"Exo 4 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex04/ft_str_is_lowercase.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_str_is_lowercase(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("\n") == 7
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 4")
print("#"*40)
print("")



######################
#Exo 5
######################
ResetTempDir()
print("#"*15,"Exo 5 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex05/ft_str_is_uppercase.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_str_is_uppercase(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("\n") == 7
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")


######################
#Exo 6
######################
ResetTempDir()
print("#"*15,"Exo 6 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex06/ft_str_is_printable.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_str_is_printable(char *str);",
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
    if (valid)printf("127 OK\\n");
    val[0] = 127;
    valid = valid && !ft_str_is_printable(val);
    if (valid)printf("127 OK\\n");
    val[0] = '\\0';
    valid = valid && ft_str_is_printable(val);
    if (valid)printf("0 OK\\n");

    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("\n") == 5
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 6")
print("#"*40)
print("")



######################
#Exo 7
######################
ResetTempDir()
print("#"*15,"Exo 7 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex07/ft_strupcase.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strupcase(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res == "asfg546564#$%$@2ASDDSFaz".upper()
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 7")
print("#"*40)
print("")


######################
#Exo 8
######################
ResetTempDir()
print("#"*15,"Exo 8 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex08/ft_strlowcase.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strlowcase(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res == "asfg546564#$%$@2ASDDSFaz".lower()
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 8")
print("#"*40)
print("")


######################
#Exo 9
######################
ResetTempDir()
print("#"*15,"Exo 9 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex09/ft_strcapitalize.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strcapitalize(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res == "Salut, Comment Tu Vas ? 42mots Quarante-Deux; Cinquante+Et+Un Ahhh! 42ahh"
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 9")
print("#"*40)
print("")


######################
#Exo 10
######################
ResetTempDir()
print("#"*15,"Exo 10 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex10/ft_strlcpy.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"unsigned int ft_strlcpy(char *dest, char *src, unsigned int size);",
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
        printf("OK");

    char destinationCheck2[] = "ABCDEFGHIJKLMNOPQRSTUV";
    res2 = ft_strlcpy(destinationCheck2, source, len+5);
    valid = valid && (strcmp(source,destinationCheck2)==0) && len==res2;
    if (valid)
        printf("OK");

    char destinationCheck3[] = "ABC";
    unsigned int len2 = strlen(destinationCheck3);
    res2 = ft_strlcpy(destinationCheck3, source, len2+1);
    valid = valid && (strcmp("Hel",destinationCheck3)==0) && len==res2;
    if (valid)
        printf("OK");

    char destinationCheck4[] = "";
    unsigned int len3 = strlen(destinationCheck4);
    res2 = ft_strlcpy(destinationCheck4, source, len3);
    valid = valid && (strcmp("",destinationCheck4)==0) && len==res2;
    if (valid)
        printf("OK");

    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="OK"*4
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 10")
print("#"*40)
print("")



######################
#Exo 11
######################

def charToHex(char):
    return "\\{0:02x}".format(ord(char))
def intToHex(nb):
    return "\\{0:02x}".format(nb)
ResetTempDir()
print("#"*15,"Exo 11 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex11/ft_putstr_non_printable.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_putstr_non_printable(char *str);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
want = intToHex(255)+intToHex(1)+intToHex(254)+intToHex(127)+"Coucou"+charToHex('\n')+charToHex('\t')+charToHex('\r')+"tu vas bien ?"
print("want","%"+want+"%")
res = ExecuteCode()
v2 = res == want
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 11")
print("#"*40)
print("")



######################
#Exo 12
######################

def charToHex(char):
    return "\\{0:02x}".format(ord(char))
ResetTempDir()
print("#"*15,"Exo 12 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex12/ft_print_memory.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void *ft_print_memory(void *addr, unsigned int size);",
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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
ExecuteCode()
PrintColor("Cet exercice n'a pas la solution dans la moulinette",color_red)
print("#"*40)
print("")