from BaseLib import *
Config.PATH_git = GetGitPath("C_07")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")


######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_strdup.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strdup(char *src);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strdup.h"
int main(void)
{
    char *a0 = strdup("Test");
    char *a1 = ft_strdup("Test");
    char *b0 = strdup("484df41hdy1h111fs1fsd15sf15sdf115d15fdgs15gfd4sg1615df156g1515g4erg4561esg156gr15156g15eg15eg15e51e51g1515ge156e156eg156e15156ge516e1551eg51eg15g1551eg15e516eg15e15eg1515e55eg51e15e51g5151eg15eg1515egr515151erg51er51e51e551ee5eg51egr51er51er5er5eg51e5r1e51rg5egr5eg51erg5e1r51e6rg51egr516ee5g15e1g5e1g5e1g51ger51egr51erg55reg5er55er55");
    char *b1 = ft_strdup("484df41hdy1h111fs1fsd15sf15sdf115d15fdgs15gfd4sg1615df156g1515g4erg4561esg156gr15156g15eg15eg15e51e51g1515ge156e156eg156e15156ge516e1551eg51eg15g1551eg15e516eg15e15eg1515e55eg51e15e51g5151eg15eg1515egr515151erg51er51e51e551ee5eg51egr51er51er5er5eg51e5r1e51rg5egr5eg51erg5e1r51e6rg51egr516ee5g15e1g5e1g5e1g51ger51egr51erg55reg5er55er55");
    printf("%s\\n", strcmp(a0, a1) == 0 ?
			"OK" :
			"Fail");
	printf("%s\\n", strcmp(b0, b1) == 0 ?
			"OK" :
			"Fail");
    free(a0);
    free(a1);
    free(b0);
    free(b1);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
res = ExecuteCode(exc=["valgrind"],returnAll = True)
v2 = CheckMemory(res.stderr) and res.stdout.count("OK") == 2

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
path_c = Join(Config.PATH_git,"ex01/ft_range.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int *ft_range(int min, int max);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_range.h"

void draw(int *range, int size)
{
    for(int i=0; i < size; i++)
        printf("%d, ", range[i]);
    printf("\\n");
}

int main(void)
{
    int *range;

	range = ft_range(0, 5);
	printf("0, 1, 2, 3, 4 : ");
    draw(range,5);
	free(range);
	range = ft_range(3, 3);
    if (range == NULL)
    {
        printf("NULL\\n");
    }
	
	range = ft_range(-1, 1);
	printf("-1, 0 :");
    draw(range,2);
    free(range);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
res = ExecuteCode(exc=["valgrind"],returnAll = True)
v2 = CheckMemory(res.stderr) and res.stdout == """0, 1, 2, 3, 4 : 0, 1, 2, 3, 4, 
NULL
-1, 0 :-1, 0, 
"""

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
path_c = Join(Config.PATH_git,"ex02/ft_ultimate_range.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_ultimate_range(int **range, int min, int max);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_ultimate_range.h"

void draw(int *range, int size)
{
    for(int i=0; i < size; i++)
        printf("%d, ", range[i]);
    printf("\\n");
}

int main(void)
{
    int *range;
    int res;

	res = ft_ultimate_range(&range,0, 5);
    printf("5 : %d\\n",res);
	printf("0, 1, 2, 3, 4 : ");
    draw(range,5);
	free(range);
	res = ft_ultimate_range(&range,3, 3);
    printf("0 : %d\\n",res);
    if (range == NULL)
    {
        printf("NULL\\n");
    }
	
	res = ft_ultimate_range(&range,-1, 1);
    printf("2 : %d\\n",res);
	printf("-1, 0 :");
    draw(range,2);
    free(range);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
res = ExecuteCode(exc=["valgrind"],returnAll = True)
v2 = CheckMemory(res.stderr) and res.stdout == """5 : 5
0, 1, 2, 3, 4 : 0, 1, 2, 3, 4, 
0 : 0
NULL
2 : 2
-1, 0 :-1, 0, 
"""

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
path_c = Join(Config.PATH_git,"ex03/ft_strjoin.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char *ft_strjoin(int size, char **strs, char *sep);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strjoin.h"

int main(int argc, char **argv)
{
    if (argc < 3)
        return (0);
    char *res = ft_strjoin(argc - 2, argv + 2, argv[1]);
    printf("#%s#\\n",res);
    free(res);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
tests = [
    [", ", "aaa", "bb","cc"],
    ["a",""],
    ["a","",""],
    ["", "aaa", "bb","cc"],
    ["", "",""]
]
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == """#aaa, bb, cc#
##
#a#
#aaabbcc#
##
"""
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
path_c = Join(Config.PATH_git,"ex04/ft_convert_base.c")
valid = CheckNorme( Join(Config.PATH_git,"ex04"), 2)
IfValid(valid)
temp_c = CopyToTemp(path_c)
CopyToTemp(Join(Config.PATH_git,"ex04/ft_convert_base2.c"))
AutoMain(temp_c,"char	*ft_convert_base(char *nbr, char *base_from, char *base_to);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_convert_base.h"

int main(int argc, char **argv)
{
    if (argc < 5)
        return (0);
    char *res = ft_convert_base(argv[2],argv[3],argv[4]);
    printf("#%s:%s#\\n",argv[1],res);
    free(res);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
tests = [
    ["42", "--2a", "0123456789abcdef", "0123456789"],
    ["-2a", "-42", "0123456789", "0123456789abcdef"],
    ["-10000000000000000000000000000000", "-2147483648", "0123456789", "01"],
    ["1111111111111111111111111111111", "2147483647", "0123456789", "01"],
    ["(null)", "1", "0123456789", "1"],
    ["(null)", "1", "0123456789", ""],
    ["(null)", "1", "", "0123456789"],
    ["0", "", "0123456789", "0123456789"],
]
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == """#42:42#
#-2a:-2a#
#-10000000000000000000000000000000:-10000000000000000000000000000000#
#1111111111111111111111111111111:1111111111111111111111111111111#
#(null):(null)#
#(null):(null)#
#(null):(null)#
#0:0#
"""
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
path_c = Join(Config.PATH_git,"ex05/ft_split.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"char **ft_split(char *str, char *charset);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_split.h"

int main(int argc, char **argv)
{
    if (argc < 3)
        return (0);
    char **res = ft_split(argv[1],argv[2]);
    printf("###############\\n");
    int i = 0;
    while (res[i] != 0)
        printf("#%s#\\n",res[i++]);
    printf("###############\\n");
    i = 0;
    while (res[i] != 0)
        free(res[i++]);
    free(res);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
tests = [
    ["aa,bb,cc", ","],
    ["aa", ","],
    ["aa,,,,,b,b,c", ","],
    ["dd,e:e f", ",: "],
    ["Yaa!", ""],
    ["HelloYaa!World", "Yaa!"],
    ["", ",: "],
    ["Ya;a!", ";;"],
    ["", ""],
]
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout

v2 = v2 and resTXT == """###############
#aa#
#bb#
#cc#
###############
###############
#aa#
###############
###############
#aa#
#b#
#b#
#c#
###############
###############
#dd#
#e#
#e#
#f#
###############
###############
#Yaa!#
###############
###############
#Hello#
#World#
###############
###############
###############
###############
#Ya#
#a!#
###############
###############
###############
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")
