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
        AutoMain(self.files["ft_iterative_factorial.c"],"int ft_iterative_factorial(int nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""0:0
0:0
1:1
1:1
3628800:3628800
6:6
"""
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_recursive_factorial.c"],"int ft_recursive_factorial(int nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""0:0
0:0
1:1
1:1
3628800:3628800
6:6
"""

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_iterative_power.c"],"int ft_iterative_power(int nb, int power);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""0:1
0:0
0:0
1:1
10:10
100:100
216:216
"""

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_recursive_power.c"],"int ft_recursive_power(int nb, int power);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""0:1
0:0
0:0
1:1
10:10
100:100
216:216
"""

@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_fibonacci.c"],"int ft_fibonacci(int index);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""-1:-1
-1:-1
0:0
1:1
1:1
2:2
55:55
"""

@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_sqrt.c"],"int ft_sqrt(int nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""1:1
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

@AddExercise(id="ex06")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_is_prime.c"],"int ft_is_prime(int nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 16

@AddExercise(id="ex07")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_find_next_prime.c"],"int ft_find_next_prime(int nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 17

@AddExercise(id="ex08")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_ten_queens_puzzle.c"],"int ft_ten_queens_puzzle(void);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_ten_queens_puzzle.h"
int main(void)
{
    int res = ft_ten_queens_puzzle();
	printf("%d\\n",res);
    if (res == 724)
        printf("OK\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        res = str(ExecuteCode(canPrint=False))
        print(res[:99]+"\n...\n"+res[-103:])
        valid = "0257948136\n0258693147\n" in res
        valid = valid and "4605713829\n4609582731\n" in res
        valid = valid and "9742051863" in res
        PrintColor("Cet exercice n'a pas la solution dans la moulinette",Colors.YELLOW)
        return valid and res.count("OK") == 1

