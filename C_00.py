from Moulinette import *
Config.PATH_git = "/mnt/nfs/homes/lfarhi/Desktop/piscine/day3_C_00/"
Config.normeflag = "-R CheckForbiddenSourceHeader"


###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_putchar.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_putchar(char c);",
"""
#include "ft_putchar.h"
int main(void)
{
    ft_putchar('a');
    ft_putchar('b');
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
valid = valid and res=="ab"
IfValid(valid,"Exo 0")
print("#"*40)
print("")


######################
#Exo 1
######################
ResetTempDir()
print("#"*15,"Exo 1 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex01/ft_print_alphabet.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_alphabet(void);",
"""
#include "ft_print_alphabet.h"
int main(void)
{
    ft_print_alphabet();
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
res = res=="abcdefghijklmnopqrstuvwxyz"
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 1")
print("#"*40)
print("")

######################
#Exo 2
######################
ResetTempDir()
print("#"*15,"Exo 2 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex02/ft_print_reverse_alphabet.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_reverse_alphabet(void);",
"""
#include "ft_print_reverse_alphabet.h"
int main(void)
{
    ft_print_reverse_alphabet();
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
res = res=="abcdefghijklmnopqrstuvwxyz"[::-1]
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 2")
print("#"*40)
print("")

######################
#Exo 3
######################
ResetTempDir()
print("#"*15,"Exo 3 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex03/ft_print_numbers.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_numbers(void);",
"""
#include "ft_print_numbers.h"
int main(void)
{
    ft_print_numbers();
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
res = res=="0123456789"
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 3")
print("#"*40)
print("")


######################
#Exo 4
######################
ResetTempDir()
print("#"*15,"Exo 4 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex04/ft_is_negative.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_is_negative(int n);",
"""
#include "ft_is_negative.h"
int main(void)
{
    ft_is_negative(-1);
    ft_is_negative(0);
    ft_is_negative(1);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
res = res=="NPP"
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 4")
print("#"*40)
print("")


######################
#Exo 5
######################
ResetTempDir()
print("#"*15,"Exo 5 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex05/ft_print_comb.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_comb(void);",
"""
#include "ft_print_comb.h"
int main(void)
{
    ft_print_comb();
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
res = res=="012, 013, 014, 015, 016, 017, 018, 019, 023, 024, 025, 026, 027, 028, 029, 034, 035, 036, 037, 038, 039, 045, 046, 047, 048, 049, 056, 057, 058, 059, 067, 068, 069, 078, 079, 089, 123, 124, 125, 126, 127, 128, 129, 134, 135, 136, 137, 138, 139, 145, 146, 147, 148, 149, 156, 157, 158, 159, 167, 168, 169, 178, 179, 189, 234, 235, 236, 237, 238, 239, 245, 246, 247, 248, 249, 256, 257, 258, 259, 267, 268, 269, 278, 279, 289, 345, 346, 347, 348, 349, 356, 357, 358, 359, 367, 368, 369, 378, 379, 389, 456, 457, 458, 459, 467, 468, 469, 478, 479, 489, 567, 568, 569, 578, 579, 589, 678, 679, 689, 789"
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 5")
print("#"*40)
print("")


######################
#Exo 6
######################
ResetTempDir()
def tempExo():
    s = ""
    i = 0
    j = 1
    while i < 99:
        if j < 100:
            s+="{:02}".format(i)+" "+"{:02}".format(j)
            s+=", "
        j+=1
        if j >= 100:
            i+=1
            j = i +1
    s=s[:-2]
    return s
print("#"*15,"Exo 6 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex06/ft_print_comb2.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_comb2(void);",
"""
#include "ft_print_comb2.h"
int main(void)
{
    ft_print_comb2();
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(canPrint=False)
print(res[:40]," ... ",res[-40:], end="")
PrintColor("%",'\033[4m')
res2 = tempExo()
res = res==res2
res = res and "00 99, 01 02" in res2
if not "00 99, 01 02" in res2:
    PrintColor("00 99, 01 02 not in result",color_red)
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 6")
print("#"*40)
print("")



######################
#Exo 7
######################
ResetTempDir()
print("#"*15,"Exo 7 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex07/ft_putnbr.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
vals = [random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
AutoMain(temp_c,"void ft_putnbr(int nb);",
"""
#include <unistd.h>
#include "ft_putnbr.h"
int main(void)
{
    static int len = """+str(len(vals))+""";
    int vals["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";
    for(int i = 0; i < len; i++)
    {
        ft_putnbr(vals[i]);
        write(1,",",1);
    }
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
want = ",".join([str(i) for i in vals])+","
print("Check with :\n"+want)
print("#"*30)
res = ExecuteCode()
res = res==want
IfValid(res)
valid = valid and res 
IfValid(valid,"Exo 7")
print("#"*40)
print("")


######################
#Exo 8
######################
ResetTempDir()
print("#"*15,"Exo 8 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex08/ft_print_combn.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_print_combn(int n);",
"""
#include <unistd.h>
#include "ft_print_combn.h"
int main(void)
{
    write(1,"size = 2\\n",9);
    ft_print_combn(2);
    write(1, "\\n", 1);
    write(1,"size = 3\\n",9);
    ft_print_combn(3);
    write(1, "\\n", 1);
    write(1,"size = 9\\n",9);
    ft_print_combn(9);
    return 0;
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
ExecuteCode()
PrintColor("Cet exercice n'a pas la solution dans la moulinette",color_red)
print("#"*40)
print("")