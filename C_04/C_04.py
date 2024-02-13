from BaseLib import *
Config.PATH_git = GetGitPath("C_04")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_strlen.c")
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
IfValid(valid,"Exo 0")
print("#"*40)
print("")


######################
#Exo 1
######################
ResetTempDir()
print("#"*15,"Exo 1 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex01/ft_putstr.c")
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
IfValid(valid,"Exo 1")
print("#"*40)
print("")


######################
#Exo 2
######################
ResetTempDir()
print("#"*15,"Exo 2 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex02/ft_putnbr.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
vals = [0]+[-2147483648]+[random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
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
IfValid(valid,"Exo 2")
print("#"*40)
print("")


######################
#Exo 3
######################
ResetTempDir()
print("#"*15,"Exo 3 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex03/ft_atoi.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_atoi(char *str);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_atoi.h"
int main(void)
{
    printf("%d\\n",ft_atoi(" ---+--+1234ab567"));// -1234
    printf("%d\\n",ft_atoi("    \\t\\n--+--+2147483647#ab567"));// 2147483647
    printf("%d\\n",ft_atoi(" +-+--+2147483648"));//

    printf("%d\\n", ft_atoi("  \\n  42t4457"));// 42
	printf("%d\\n", ft_atoi(" --+-42sfs:f545"));// -42
	printf("%d\\n", ft_atoi("\\0 1337"));// 0
	printf("%d\\n", ft_atoi("-0"));// 0
	printf("%d\\n", ft_atoi(" - 1 3 2 5 6 3 2 1 6 7"));// 0
    printf("%d\\n", ft_atoi(" -a1 3 2 5 6 3 2 1 6 7"));// 0
	printf("%d\\n", ft_atoi("-1325632167"));// -1325632167
	printf("%d\\n", ft_atoi("-100"));// -100
	printf("%d\\n", ft_atoi("\\t---+2147483648"));// -2147483648
	printf("%d\\n", ft_atoi("\\v2147483647"));// 2147483647
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="-1234\n2147483647\n-2147483648\n42\n-42\n0\n0\n0\n0\n-1325632167\n-100\n-2147483648\n2147483647\n"
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
path_c = Join(Config.PATH_git,"ex04/ft_putnbr_base.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_putnbr_base(int nbr, char *base);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_putnbr_base.h"
int main(void)
{
    //write(1, "42:", 3);
	ft_putnbr_base(42, "0123456789");
    write(1, "\\n", 1);
	//write(1, "\\n2a:", 4);
	ft_putnbr_base(42, "0123456789abcdef");
    write(1, "\\n", 1);
	//write(1, "\\n-2a:", 5);
	ft_putnbr_base(-42, "0123456789abcdef");
    write(1, "\\n", 1);
	//write(1, "\\n:", 2);
	ft_putnbr_base(42, "");
    write(1, "\\n", 1);
	//write(1, "\\n:", 2);
	ft_putnbr_base(42, "0");
    write(1, "\\n", 1);

    //write(1, "\\n:", 2);
	ft_putnbr_base(42, "01234560789");
    write(1, "\\n", 1);

	//write(1, "\\n:", 2);
	ft_putnbr_base(42, "+-0123456789abcdef");
    write(1, "\\n", 1);
	//write(1, "\\n:", 2);
	ft_putnbr_base(42, "\\t0123456789abcdef");
    write(1, "\\n", 1);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="42\n2a\n-2a\n\n\n\n\n\n"
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
path_c = Join(Config.PATH_git,"ex05/ft_atoi_base.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_atoi_base(char *str, char *base);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_atoi_base.h"
int main(void)
{
    printf("42:%d\\n", ft_atoi_base("2a", "0123456789abcdef"));
	printf("-42:%d\\n", ft_atoi_base("   --------+-2a", "0123456789abcdef"));
	printf("42:%d\\n", ft_atoi_base("   -+-2a", "0123456789abcdef"));
	printf("0:%d\\n", ft_atoi_base("   --------+- 2a", "0123456789abcdef"));
	printf("0:%d\\n", ft_atoi_base("   --------+-z", "0123456789abcdef"));
	printf("0:%d\\n", ft_atoi_base("   --------+-2a", ""));
	printf("0:%d\\n", ft_atoi_base("   --------+-2a", "0"));
	printf("0:%d\\n", ft_atoi_base("   --------+-2a", "+-0"));
	printf("0:%d\\n", ft_atoi_base("   --------+-2a", "\\t01"));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""42:42
-42:-42
42:42
0:0
0:0
0:0
0:0
0:0
0:0
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")