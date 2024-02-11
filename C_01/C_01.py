from BaseLib import *
Config.PATH_git = GetGitPath("C_01")
Config.normeflag = "-R CheckForbiddenSourceHeader"


###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_ft.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_ft(int *nbr);",
"""
#include <unistd.h>
#include "ft_ft.h"
int main(void)
{
    int v;
    ft_ft(&v);
    if (v==42)
        write(1,"42",2);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="42"
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
path_c = Join(Config.PATH_git,"ex01/ft_ultimate_ft.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_ultimate_ft(int *********nb);",
"""
#include <unistd.h>
#include "ft_ultimate_ft.h"
int main(void)
{
    int v1;
    int *v2 = &v1;
    int **v3 = &v2;
    int ***v4 = &v3;
    int ****v5 = &v4;
    int *****v6 = &v5;
    int ******v7 = &v6;
    int *******v8 = &v7;
    int ********v9 = &v8;
    int *********v10 = &v9;
    ft_ultimate_ft(v10);
    if (v1==42)
        write(1,"42",2);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="42"
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
path_c = Join(Config.PATH_git,"ex02/ft_swap.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_swap(int *a, int *b);",
"""
#include <unistd.h>
#include "ft_swap.h"
int main(void)
{
    int a = 750;
    int b = -55;
    ft_swap(&a,&b);
    if (b==750 && a==-55)
        write(1,"OK",2);
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
path_c = Join(Config.PATH_git,"ex03/ft_div_mod.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_div_mod(int a, int b, int *div, int *mod);",
"""
#include <unistd.h>
#include "ft_div_mod.h"
int main(void)
{
    int a = 9;
    int b = 2;
    int div;
    int mod;
    ft_div_mod(a,b,&div,&mod);
    if (div == 4 && mod == 1)
        write(1,"OK",2);
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
IfValid(valid,"Exo 3")
print("#"*40)
print("")


######################
#Exo 4
######################
ResetTempDir()
print("#"*15,"Exo 4 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex04/ft_ultimate_div_mod.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_ultimate_div_mod(int *a, int *b);",
"""
#include <unistd.h>
#include "ft_ultimate_div_mod.h"
int main(void)
{
    int a = 9;
    int b = 2;
    ft_ultimate_div_mod(&a,&b);
    if (a == 4 && b == 1)
        write(1,"OK",2);
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
IfValid(valid,"Exo 4")
print("#"*40)
print("")


######################
#Exo 5
######################
ResetTempDir()
print("#"*15,"Exo 5 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex05/ft_putstr.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_putstr(char *str);",
"""
#include <unistd.h>
#include "ft_putstr.h"
int main(void)
{
    ft_putstr("Hello World");
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
IfValid(valid,"Exo 5")
print("#"*40)
print("")


######################
#Exo 6
######################
ResetTempDir()
print("#"*15,"Exo 6 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex06/ft_strlen.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_strlen(char *str);",
"""
#include <unistd.h>
#include "ft_strlen.h"
int main(void)
{
    int len = ft_strlen("Hello World");
    if (len==11)
        write(1,"OK",2);
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
IfValid(valid,"Exo 6")
print("#"*40)
print("")


######################
#Exo 7
######################
ResetTempDir()
print("#"*15,"Exo 7 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex07/ft_rev_int_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
tests = [
    [0],
    [i-15 for i in range (30)],
    []
]
for vals in tests:
    AutoMain(temp_c,"void ft_rev_int_tab(int *tab, int size);",
    """
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include "ft_rev_int_tab.h"
    int main(void)
    {
        static int len = """+str(len(vals))+""";
        int temp["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";
        int* vals = malloc(len*sizeof(int));
        for (int i = 0; i < len; i++)
            vals[i] = temp[i];
        ft_rev_int_tab(vals,len);
        for (int i = 0; i < len; i++)
        {
            printf("%d,",vals[i]);
        }
        return (0);
    }
    """
    )
    CompileTemp()
    print("#"*15,"Exec","#"*15)
    want = ",".join([str(i) for i in vals])+","
    print("Check with :\n"+want+"%")
    want = ",".join(([str(i) for i in vals])[::-1])
    if want != "": want+=","
    print("Check want :\n"+want+"%")
    print("#"*30)
    res = ExecuteCode()
    v2 = res==want
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
path_c = Join(Config.PATH_git,"ex08/ft_sort_int_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
tests = [
    [0],
    [0]+[-2147483648]+[random.randint(-100,100) for i in range (10)],
    []
]
for vals in tests:
    temp_c = CopyToTemp(path_c)
    AutoMain(temp_c,"void ft_sort_int_tab(int *tab, int size);",
    """
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include "ft_sort_int_tab.h"
    int main(void)
    {
        static int len = """+str(len(vals))+""";
        int temp["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";
        int* vals = malloc(len*sizeof(int));
        for (int i = 0; i < len; i++)
            vals[i] = temp[i];
        ft_sort_int_tab(vals,len);
        for (int i = 0; i < len; i++)
        {
            printf("%d,",vals[i]);
        }
        return (0);
    }
    """
    )
    CompileTemp()
    print("#"*15,"Exec","#"*15)
    want = ",".join([str(i) for i in vals])+","
    print("Check with :\n"+want+"%")
    want = [i for i in vals]
    want.sort()
    want = ",".join([str(i) for i in want])
    if want != "": want+=","
    print("Check want :\n"+want+"%")
    print("#"*30)
    res = ExecuteCode()
    v2 = res==want
    IfValid(v2)
    valid = valid and v2
IfValid(valid,"Exo 8")
print("#"*40)
print("")