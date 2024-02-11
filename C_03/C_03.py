from BaseLib import *
Config.PATH_git = GetGitPath("C_03")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")


######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_strcmp.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_strcmp(char *s1, char *s2);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strcmp.h"
int main(void)
{
    if (strcmp("a","a") == ft_strcmp("a","a"))
        printf("OK");
    if (strcmp("a","b") == ft_strcmp("a","b"))
        printf("OK");
    if (strcmp("ad","b") == ft_strcmp("ad","b"))
        printf("OK");
    if (strcmp("bd","b") == ft_strcmp("bd","b"))
        printf("OK");
    if (strcmp("b","bd") == ft_strcmp("b","bd"))
        printf("OK");
    if (strcmp("bd","bqq") == ft_strcmp("bd","bqq"))
        printf("OK");
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="OK"*6
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
path_c = Join(Config.PATH_git,"ex01/ft_strncmp.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_strncmp(char *s1, char *s2, unsigned int n);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strncmp.h"
int main(void)
{

    char s1_0[] = "a";
	char s2_0[] = "aaa";
	char s3_0[] = "ddd";
	char s4_0[] = "ad";
	char s5_0[] = "c";
	char s6_0[] = "bd";
	char s7_0[] = "b";
	char s8_0[] = "bqq";

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
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("Success") == 17
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
path_c = Join(Config.PATH_git,"ex02/ft_strcat.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strcat(char *dest, char *src);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strcat.h"
int main(void)
{
    char src[50] = "World !";
    char dest[50] = "Hello ";
    char dest2[50] = "Hello ";
    if (strcmp(strcat(dest,src),ft_strcat(dest2,src))==0)
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
IfValid(valid,"Exo 2")
print("#"*40)
print("")


######################
#Exo 3
######################
ResetTempDir()
print("#"*15,"Exo 3 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex03/ft_strncat.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strncat(char *dest, char *src, unsigned int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strncat.h"
int main(void)
{
    char src[50] = "World !";
    char dest[50] = "Hello ";
    char dest2[50] = "Hello ";
    if (strcmp(strncat(dest,src,8),ft_strncat(dest2,src,8))==0)
        printf("OK");
    
    if (strcmp(strncat(dest,src,3),ft_strncat(dest2,src,3))==0)
        printf("OK");
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="OKOK"
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
path_c = Join(Config.PATH_git,"ex04/ft_strstr.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strstr(char *str, char *to_find);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strstr.h"
int main(void)
{
    char a[100] = "Hello World !";
    char b[100] = "World";
    char c[100] = "ababcdabc";
    char d[100] = "abc";
    char e[100] = "efj";
    if (strstr(a,b)==ft_strstr(a,b))
        printf("Success\\n");
    if (strstr(c,d)==ft_strstr(c,d))
        printf("Success\\n");
    if (strstr(c,e)==ft_strstr(c,e))
        printf("Success\\n");



    char s1a[] = "This is OK for now";
	char s2a[] = "OK";
	char s1b[] = "This is OK for now";
	char s2b[] = "OK";
	char s3a[] = "Same";
	char s4a[] = "";
	char s3b[] = "Same";
	char s4b[] = "";
	char s5a[] = "Shorter";
	char s6a[] = "Than";
	char s5b[] = "Shorter";
	char s6b[] = "Than";

    char s7a[] = "";
	char s8a[] = "";
	char s7b[] = "";
	char s8b[] = "";

	printf("%s:%s\\n", ft_strstr(s1a, s2a), strstr(s1b, s2b));
    printf("%s\\n", ft_strstr(s1a, s2a) == strstr(s1a, s2a) ? "Success" : "Fail");
	printf("%s\\n", strcmp(s1a, s1b) == 0 && strcmp(s2a, s2b) == 0 ? "Success" : "Fail");
	printf("%s:%s\\n", ft_strstr(s3a, s4a), strstr(s3b, s4b));
    printf("%s\\n", ft_strstr(s3a, s4a) == strstr(s3a, s4a) ? "Success" : "Fail");
	printf("%s\\n", strcmp(s3a, s3b) == 0 && strcmp(s4a, s4b) == 0 ? "Success" : "Fail");
	printf("%s:%s\\n", ft_strstr(s5a, s6a), strstr(s5b, s6b));
    printf("%s\\n", ft_strstr(s5a, s6a) == strstr(s5a, s6a) ? "Success" : "Fail");
	printf("%s\\n", strcmp(s5a, s5b) == 0 && strcmp(s6a, s6b) == 0 ? "Success" : "Fail");
    printf("%s:%s\\n", ft_strstr(s7a, s8a), strstr(s7b, s8b));
    printf("%s\\n", ft_strstr(s7a, s8a) == strstr(s7a, s8a) ? "Success" : "Fail");
	printf("%s\\n", strcmp(s7a, s7b) == 0 && strcmp(s8a, s8b) == 0 ? "Success" : "Fail");
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("Success")==11
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
path_c = Join(Config.PATH_git,"ex05/ft_strlcat.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"unsigned int ft_strlcat(char *dest, char *src, unsigned int size);",
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
"""
)
CompileTemp(lib="-lbsd")
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("Success") == 8
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")