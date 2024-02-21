from BaseLib import *
Config.PATH_git = GetGitPath("C_08")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft.h")
valid = CheckNorme(path_c)
IfValid(valid,"Exo 0")
print("#"*40)
print("")

Config.normeflag = "-R CheckDefine"

######################
#Exo 1
######################
ResetTempDir()
print("#"*15,"Exo 1 Norme","#"*15)
path_h = Join(Config.PATH_git,"ex01/ft_boolean.h")
valid = CheckNorme(path_h)
IfValid(valid)
temp_c = CopyToTemp(path_h)
AutoMain(None, None,
"""
#include "ft_boolean.h"

void ft_putstr(char *str)
{
    while (*str)
        write(1, str++, 1);
}

t_bool ft_is_even(int nbr)
{
    return ((EVEN(nbr)) ? TRUE : FALSE);
}

int main(int argc, char **argv)
{
    (void)argv;
    if (ft_is_even(argc - 1) == TRUE)
        ft_putstr(EVEN_MSG);
    else
        ft_putstr(ODD_MSG);
    return (SUCCESS);
}
"""
)
CompileTemp()
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
    res = ExecuteCode(args=i)
    resTXT += res
v2 = resTXT=="""I have an even number of arguments.
I have an even number of arguments.
I have an odd number of arguments.
I have an even number of arguments.
I have an odd number of arguments.
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 1")
print("#"*40)
print("")


Config.normeflag = "-R CheckDefine"

######################
#Exo 2
######################
ResetTempDir()
print("#"*15,"Exo 2 Norme","#"*15)
path_h = Join(Config.PATH_git,"ex02/ft_abs.h")
valid = CheckNorme(path_h)
IfValid(valid)
temp_c = CopyToTemp(path_h)
AutoMain(None, None,
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include "ft_abs.h"

int main(int argc, char **argv)
{
    (void)argc;
    printf("%d\\n",ABS(atoi(argv[1])));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
tests = [
    ["-123"],
    ["-2147483647"],
    ["2147483647"],
    ["0"]
]
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(args=i)
    resTXT += res
v2 = resTXT=="""123
2147483647
2147483647
0
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
path_h = Join(Config.PATH_git,"ex03/ft_point.h")
valid = CheckNorme(path_h)
IfValid(valid)
temp_c = CopyToTemp(path_h)
AutoMain(None, None,
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include "ft_point.h"

void set_point(t_point *point)
{
    point->x = 42;
    point->y = 21;
}

int main(void)
{
    t_point point;
    set_point(&point);
    printf("%d,%d", point.x, point.y);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(args=i)
v2 = res == "42,21"
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 3")
print("#"*40)
print("")

Config.normeflag = "-R CheckForbiddenSourceHeader"

######################
#Exo 4
######################
ResetTempDir()
print("#"*15,"Exo 4 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex04/ft_strs_to_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(Join(Config.PATH_git,"ex04/ft_stock_str.h"),
"""
typedef struct s_stock_str
{
    int size;
    char *str;
    char *copy;
} t_stock_str;
""",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_stock_str.h"

struct s_stock_str *ft_strs_to_tab(int ac, char **av);

int main(int ac, char **av)
{
    struct s_stock_str * lst = ft_strs_to_tab(ac, av);
    for(int i = 0; i < ac; i++)
    {
        printf("index %d:\\n\\t size :%d\\n\\t str  :%s\\n\\t copy :%s\\n\\t ptr diff :%d\\n\\n",
        i, lst[i].size, lst[i].str, lst[i].copy, lst[i].str != lst[i].copy);
        free(lst[i].copy);
    }
    free(lst);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
tests = [
    [],
    ["-2a", "-42"],
]
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == """index 0:
	 size :8
	 str  :./Output
	 copy :./Output
	 ptr diff :1

index 0:
	 size :8
	 str  :./Output
	 copy :./Output
	 ptr diff :1

index 1:
	 size :3
	 str  :-2a
	 copy :-2a
	 ptr diff :1

index 2:
	 size :3
	 str  :-42
	 copy :-42
	 ptr diff :1

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
CopyToTemp(Join(Config.PATH_git,"ex04/ft_strs_to_tab.c"))
path_c = Join(Config.PATH_git,"ex05/ft_show_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(Join(Config.PATH_git,"ex05/ft_stock_str.h"),
"""
typedef struct s_stock_str
{
    int size;
    char *str;
    char *copy;
} t_stock_str;
""",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_stock_str.h"

struct s_stock_str *ft_strs_to_tab(int ac, char **av);

void ft_show_tab(struct s_stock_str *par);

int main(int ac, char **av)
{
    struct s_stock_str * lst = ft_strs_to_tab(ac, av);
    lst[0].copy[2] = 'M';
    lst[0].copy[3] = 'o';
    lst[0].copy[4] = 'd';
    lst[0].copy[5] = 'i';
    lst[0].copy[6] = 'f';
    lst[0].copy[7] = '\\0';
    ft_show_tab(lst);
    for(int i = 0; i < ac; i++)
        free(lst[i].copy);
    free(lst);
    return (0);
}
"""
)
CompileTemp("-g")
print("#"*15,"Exec","#"*15)
tests = [
    [],
    ["-2a", "-42"],
]
v2 = True
resTXT = ""
for i in tests:
    print("#"*10)
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    print("#"*10)
    v2 = v2 and CheckValgrind(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == """./Output
8
./Modif
./Output
8
./Modif
-2a
3
-2a
-42
3
-42
"""

valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")