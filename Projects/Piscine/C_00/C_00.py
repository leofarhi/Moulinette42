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
        AutoMain(self.files["ft_putchar.c"],"void ft_putchar(char c);","""
#include "ft_putchar.h"
int main(void)
{
    ft_putchar('a');
    ft_putchar('b');
    return (0);
}
""")
        return CompileTemp()
    
    def Execute(self):
        return ExecuteCode()=="ab"
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_alphabet.c"],"void ft_print_alphabet(void);","""
#include "ft_print_alphabet.h"
int main(void)
{
    ft_print_alphabet();
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="abcdefghijklmnopqrstuvwxyz"

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_reverse_alphabet.c"],"void ft_print_reverse_alphabet(void);","""
#include "ft_print_reverse_alphabet.h"
int main(void)
{
    ft_print_reverse_alphabet();
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="abcdefghijklmnopqrstuvwxyz"[::-1]

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_numbers.c"],"void ft_print_numbers(void);","""
#include "ft_print_numbers.h"
int main(void)
{
    ft_print_numbers();
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="0123456789"

@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_is_negative.c"],"void ft_is_negative(int n);","""
#include "ft_is_negative.h"
int main(void)
{
    ft_is_negative(-1);
    ft_is_negative(0);
    ft_is_negative(1);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="NPP"

@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_comb.c"],"void ft_print_comb(void);","""
#include "ft_print_comb.h"
int main(void)
{
    ft_print_comb();
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="012, 013, 014, 015, 016, 017, 018, 019, 023, 024, 025, 026, 027, 028, 029, 034, 035, 036, 037, 038, 039, 045, 046, 047, 048, 049, 056, 057, 058, 059, 067, 068, 069, 078, 079, 089, 123, 124, 125, 126, 127, 128, 129, 134, 135, 136, 137, 138, 139, 145, 146, 147, 148, 149, 156, 157, 158, 159, 167, 168, 169, 178, 179, 189, 234, 235, 236, 237, 238, 239, 245, 246, 247, 248, 249, 256, 257, 258, 259, 267, 268, 269, 278, 279, 289, 345, 346, 347, 348, 349, 356, 357, 358, 359, 367, 368, 369, 378, 379, 389, 456, 457, 458, 459, 467, 468, 469, 478, 479, 489, 567, 568, 569, 578, 579, 589, 678, 679, 689, 789"

@AddExercise(id="ex06")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def resExo(self):
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

    def Compile(self):
        AutoMain(self.files["ft_print_comb2.c"],"void ft_print_comb2(void);","""
#include "ft_print_comb2.h"
int main(void)
{
    ft_print_comb2();
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        res = ExecuteCode(canPrint=False)
        print(res[:40]," ... ",res[-40:], end="")
        PrintColor("%",'\033[4m')
        res2 = self.resExo()
        res = res==res2
        res = res and "00 99, 01 02" in res2
        if not "00 99, 01 02" in res2:
            PrintColor("00 99, 01 02 not in result",Colors.RED)
        return res

@AddExercise(id="ex07")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        self.vals = [0,-2147483648,2147483647]+[random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
        AutoMain(self.files["ft_putnbr.c"],"void ft_putnbr(int nb);","""
#include <unistd.h>
#include "ft_putnbr.h"
int main(void)
{
    static int len = """+str(len(self.vals))+""";
    int vals["""+str(len(self.vals))+"""] = """+str(self.vals).replace("[","{").replace("]","}")+""";
    for(int i = 0; i < len; i++)
    {
        ft_putnbr(vals[i]);
        write(1,",",1);
    }
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        want = ",".join([str(i) for i in self.vals])+","
        PrintColor("Check with :\n"+want,Colors.YELLOW)
        print("#"*30)
        return ExecuteCode()==want

@AddExercise(id="ex08")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_print_combn.c"],"void ft_print_combn(int n);","""
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
""")
        return CompileTemp()

    def Execute(self):
        ExecuteCode()
        PrintColor("Cet exercice n'a pas la solution dans la moulinette",Colors.YELLOW)
        return True

