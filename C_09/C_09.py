from BaseLib import *
import C_09.ResultDir as ResTree
Config.PATH_git = GetGitPath("C_09")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")


######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 strcmp","#"*15)
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
    printf("%d\\t%d\\n",strcmp("a","a"),ft_strcmp("a","a"));
    printf("%d\\t%d\\n",strcmp("a","b"),ft_strcmp("a","b"));
    printf("%d\\t%d\\n",strcmp("ad","b"),ft_strcmp("ad","b"));
    printf("%d\\t%d\\n",strcmp("bd","b"),ft_strcmp("bd","b"));
    printf("%d\\t%d\\n",strcmp("b","bd"),ft_strcmp("b","bd"));
    printf("%d\\t%d\\n",strcmp("bd","bqq"),ft_strcmp("bd","bqq"));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res== \
"""0	0
-1	-1
-1	-1
1	100
-1	-100
-1	-13
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 0")
print("#"*40)
print("")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
files = os.listdir(Join(Config.PATH_git,"ex00"))
if str(files) != "['ft_swap.c', 'ft_putchar.c', 'ft_strcmp.c', 'ft_putstr.c', 'ft_strlen.c', 'libft_creator.sh']":
    PrintColor("Error number of files",color_red)
valid = CheckNorme(Join(Config.PATH_git,"ex00"), 5)
IfValid(valid)
for file in files:
    CopyToTemp(Join(Join(Config.PATH_git,"ex00"), file))
print("#"*15,"Exec","#"*15)
Process("chmod +x libft_creator.sh",shell=True,cwd=tempDir)
Process(["sh","libft_creator.sh"],cwd=tempDir)
print(os.listdir(tempDir))
v2 = 'libft.a' in os.listdir(tempDir)
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 0")
print("#"*40)
print("")


######################
#Exo 1
######################
ResetTempDir()
print("#"*15,"Exo 1 ","#"*15)
files = os.listdir(Join(Config.PATH_git,"ex00"))
for file in files:
    if file != "libft_creator.sh":
        CopyToTemp(Join(Join(Config.PATH_git,"ex00"), file),"srcs")
textH = \
"""
#ifndef FT_H
#define FT_H

void ft_putchar(char c);
void ft_swap(int *a, int *b);
void ft_putstr(char *str);
int ft_strlen(char *str);
int ft_strcmp(char *s1, char *s2);

#endif
"""
MakeDir(Join(tempDir,"includes"))
h_file = Join(Join(tempDir,"includes"),"ft.h")
with open(h_file,"w") as fic:
    fic.write(textH)
CopyToTemp(Join(Config.PATH_git,"ex01/Makefile"))
print("#"*5,"make","#"*5)
print(Process(["make"],cwd=tempDir))
IfValid(ResTree.make==PrintTree())

print("#"*5,"make fclean","#"*5)
print(Process(["make","fclean"],cwd=tempDir))
IfValid(ResTree.make_fclean==PrintTree())

print("#"*5,"make all","#"*5)
print(Process(["make","all"],cwd=tempDir))
IfValid(ResTree.make_all==PrintTree())

print("#"*5,"make clean","#"*5)
print(Process(["make","clean"],cwd=tempDir))
IfValid(ResTree.make_clean==PrintTree())

print("#"*5,"make re","#"*5)
print(Process(["make","re"],cwd=tempDir))
IfValid(ResTree.make_re==PrintTree())

print("#"*5,"make fclean","#"*5)
print(Process(["make","fclean"],cwd=tempDir))

print("#"*5,"make libft.a","#"*5)
print(Process(["make","libft.a"],cwd=tempDir))
IfValid(ResTree.make_libft_a==PrintTree())

print("#"*40)
print("")


######################
#Exo 2
######################
ResetTempDir()
print("#"*15,"Exo 2 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex02/ft_split.c")
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
IfValid(valid,"Exo 2")
print("#"*40)
print("")
