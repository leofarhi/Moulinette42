from BaseLib import *
Config.PATH_git = GetGitPath("C_05")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_iterative_factorial.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_iterative_factorial(int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_iterative_factorial.h"
int main(void)
{
    printf("0:%d\\n", ft_iterative_factorial(-10));
	printf("0:%d\\n", ft_iterative_factorial(-1));
	printf("1:%d\\n", ft_iterative_factorial(0));
	printf("1:%d\\n", ft_iterative_factorial(1));
	printf("3628800:%d\\n", ft_iterative_factorial(10));
	printf("6:%d\\n", ft_iterative_factorial(3));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""0:0
0:0
1:1
1:1
3628800:3628800
6:6
"""
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
path_c = Join(Config.PATH_git,"ex01/ft_recursive_factorial.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_recursive_factorial(int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_recursive_factorial.h"
int main(void)
{
    printf("0:%d\\n", ft_recursive_factorial(-10));
	printf("0:%d\\n", ft_recursive_factorial(-1));
	printf("1:%d\\n", ft_recursive_factorial(0));
	printf("1:%d\\n", ft_recursive_factorial(1));
	printf("3628800:%d\\n", ft_recursive_factorial(10));
	printf("6:%d\\n", ft_recursive_factorial(3));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""0:0
0:0
1:1
1:1
3628800:3628800
6:6
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
path_c = Join(Config.PATH_git,"ex02/ft_iterative_power.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_iterative_power(int nb, int power);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_iterative_power.h"
int main(void)
{
    printf("0:%d\\n", ft_iterative_power(0, 0));
    printf("0:%d\\n", ft_iterative_power(1, -10));
	printf("0:%d\\n", ft_iterative_power(1, -1));
	printf("1:%d\\n", ft_iterative_power(10, 0));
	printf("10:%d\\n", ft_iterative_power(10, 1));
	printf("100:%d\\n", ft_iterative_power(10, 2));
	printf("216:%d\\n", ft_iterative_power(6, 3));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""0:1
0:0
0:0
1:1
10:10
100:100
216:216
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
path_c = Join(Config.PATH_git,"ex03/ft_recursive_power.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_recursive_power(int nb, int power);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_recursive_power.h"
int main(void)
{
    printf("0:%d\\n", ft_recursive_power(0, 0));
    printf("0:%d\\n", ft_recursive_power(1, -10));
	printf("0:%d\\n", ft_recursive_power(1, -1));
	printf("1:%d\\n", ft_recursive_power(10, 0));
	printf("10:%d\\n", ft_recursive_power(10, 1));
	printf("100:%d\\n", ft_recursive_power(10, 2));
	printf("216:%d\\n", ft_recursive_power(6, 3));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""0:1
0:0
0:0
1:1
10:10
100:100
216:216
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
path_c = Join(Config.PATH_git,"ex04/ft_fibonacci.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_fibonacci(int index);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_fibonacci.h"
int main(void)
{
    printf("-1:%d\\n", ft_fibonacci(-10));
    printf("-1:%d\\n", ft_fibonacci(-1));
    printf("0:%d\\n", ft_fibonacci(0));
	printf("1:%d\\n", ft_fibonacci(1));
	printf("1:%d\\n", ft_fibonacci(2));
	printf("2:%d\\n", ft_fibonacci(3));
	printf("55:%d\\n", ft_fibonacci(10));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""-1:-1
-1:-1
0:0
1:1
1:1
2:2
55:55
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
path_c = Join(Config.PATH_git,"ex05/ft_sqrt.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_sqrt(int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_sqrt.h"
int main(void)
{
	printf("1:%d\\n", ft_sqrt(1));
    printf("10:%d\\n", ft_sqrt(100));
	printf("6:%d\\n", ft_sqrt(36));
	printf("0:%d\\n", ft_sqrt(37));
	printf("100:%d\\n", ft_sqrt(10000));
	printf("0:%d\\n", ft_sqrt(10001));
	printf("2000:%d\\n", ft_sqrt(4000000));
    printf("0:%d\\n", ft_sqrt(2147483647));
    printf("46340:%d\\n", ft_sqrt(2147395600));
	printf("0:%d\\n", ft_sqrt(-36));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="""1:1
10:10
6:6
0:0
100:100
0:0
2000:2000
0:0
46340:46340
0:0
"""
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
path_c = Join(Config.PATH_git,"ex06/ft_is_prime.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_is_prime(int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_is_prime.h"
int main(void)
{
	printf("%s\\n",ft_is_prime(-1) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(-3) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(0) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(1) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(2) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(3) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(4) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(5) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(6) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(7) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(10) == 0 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(11) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(13) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(19) == 1 ? "OK" : "Fail");
	printf("%s\\n",ft_is_prime(20) == 0 ? "OK" : "Fail");
    printf("%s\\n",ft_is_prime(2147483647) == 1 ? "OK" : "Fail");
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("OK") == 16
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
path_c = Join(Config.PATH_git,"ex07/ft_find_next_prime.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_find_next_prime(int nb);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_find_next_prime.h"
int main(void)
{
    printf("%s\\n",ft_find_next_prime(-2147483648) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(-1) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(-3) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(0) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(1) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(2) == 2 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(3) == 3 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(4) == 5 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(5) == 5 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(6) == 7 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(7) == 7 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(10) == 11 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(11) == 11 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(13) == 13 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(19) == 19 ? "OK" : "Fail");
	printf("%s\\n",ft_find_next_prime(20) == 23 ? "OK" : "Fail");
    printf("%s\\n",ft_find_next_prime(2147483647) == 2147483647 ? "OK" : "Fail");
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res.count("OK") == 17
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
path_c = Join(Config.PATH_git,"ex08/ft_ten_queens_puzzle.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"int ft_ten_queens_puzzle(void);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_ten_queens_puzzle.h"
int main(void)
{
	printf("%d\\n",ft_ten_queens_puzzle());
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(canPrint=False)
print(res[:99]+"\n...\n"+res[-103:])
v2 = "0257948136\n0258693147\n" in res
v2 = v2 and "4605713829\n4609582731\n" in res
v2 = v2 and "9742051863" in res
valid = valid and v2
IfValid(v2)
PrintColor("Cet exercice n'a pas la solution dans la moulinette",color_red)
print("#"*40)
print("")