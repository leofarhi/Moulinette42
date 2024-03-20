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
        AutoMain(self.files["ft_ft.c"],"void ft_ft(int *nbr);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="42"
    
@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_ultimate_ft.c"],"void ft_ultimate_ft(int *********nb);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="42"

@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_swap.c"],"void ft_swap(int *a, int *b);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="OK"

@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_div_mod.c"],"void ft_div_mod(int a, int b, int *div, int *mod);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="OK"

@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_ultimate_div_mod.c"],"void ft_ultimate_div_mod(int *a, int *b);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="OK"

@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_putstr.c"],"void ft_putstr(char *str);",
"""
#include <unistd.h>
#include "ft_putstr.h"
int main(void)
{
    ft_putstr("Hello World");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="Hello World"

@AddExercise(id="ex06")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strlen.c"],"int ft_strlen(char *str);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="OK"

@AddExercise(id="ex07")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self,vals=[]):
        AutoMain(self.files["ft_rev_int_tab.c"],"void ft_rev_int_tab(int *tab, int size);",
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
    """)
        return CompileTemp()
    
    def Check(self,vals):
        self.Compile(vals)
        want = ",".join([str(i) for i in vals])+","
        PrintColor("Check with :\n"+want+"%",Colors.YELLOW)
        want = ",".join(([str(i) for i in vals])[::-1])
        if want != "": want+=","
        PrintColor("Check want :\n"+want+"%",Colors.CYAN)
        print("#"*30)
        res = ExecuteCode()
        v2 = res==want
        return v2

    def Execute(self):
        tests = [
            [0],
            [i-15 for i in range (30)],
            []
        ]
        valid = True
        for vals in tests:
            v = self.Check(vals)
            IfValid(v)
            valid = valid and v
        return valid

@AddExercise(id="ex08")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self,vals=[]):
        AutoMain(self.files["ft_sort_int_tab.c"],"void ft_sort_int_tab(int *tab, int size);",
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
    """)
        return CompileTemp()
    
    def Check(self,vals):
        self.Compile(vals)
        want = ",".join([str(i) for i in vals])+","
        PrintColor("Check with :\n"+want+"%",Colors.YELLOW)
        want = [i for i in vals]
        want.sort()
        want = ",".join([str(i) for i in want])
        if want != "": want+=","
        PrintColor("Check want :\n"+want+"%",Colors.CYAN)
        print("#"*30)
        res = ExecuteCode()
        v2 = res==want
        return v2

    def Execute(self):
        tests = [
            [0],
            [0,-2147483648,2147483647]+[random.randint(-100,100) for i in range (10)],
            []
        ]
        valid = True
        for vals in tests:
            v = self.Check(vals)
            IfValid(v)
            valid = valid and v
        return valid

