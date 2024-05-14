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

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return 'exo.tar' in f and len(f)==1

    def Compile(self):
        cmd = "tar -xvf exo.tar"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        os.remove(self.files['exo.tar'])
        print(os.listdir(Config.temp_path))
        return True
    
    def Execute(self):
        valid = True
        result = str(Process(["ls",'-l'],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        Want="""total XX
drwx--xr-x 2 XX XX XX Jun 1 XX test0
-rwx--xr-- 1 XX XX 4 Jun 1 XX test1
dr-x---r-- 2 XX XX XX Jun 1 XX test2
-r-----r-- 2 XX XX 1 Jun 1 XX test3
-rw-r----x 1 XX XX 2 Jun 1 XX test4
-r-----r-- 2 XX XX 1 Jun 1 XX test5
XX 1 XX XX 5 Jun 1 XX test6 -> test0"""
        lns = result.split("\n")
        lines = []
        for line in lns:
            line = line.split(" ")
            while "" in line :
                line.remove("")
            lines.append(line)
        res = [i.split(" ") for i in Want.split("\n")]
        for idx1, line in enumerate(lines):
            for idx2, sp in enumerate(line):
                c = Colors.GREEN
                w = (res[idx1])[idx2]
                if w != "XX" and w != sp:
                    c = Colors.RED
                    valid = False
                PrintColor(sp,c, end=" ")
            print()
        return valid
    

@AddExercise(id="ex01")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return 'z' in f and len(f)==1

    def Compile(self):
        return True
    
    def Execute(self):
        valid = True
        result = str(Process(["cat",'z'],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        print(result)
        return result == 'Z\n'
    
@AddExercise(id="ex02")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return 'clean' in f and len(f)==1

    def Compile(self):
        cmd = "chmod 777 clean"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        cmd = "touch aaa bbb sd8887 ~gg ~oo gG~oo lll~ \#sd5 ui9\# \#yyuyp\# \#ii\#f\# \#n\#\#"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        PrintTree()
        return os.listdir(Config.temp_path)==['clean', 'aaa', 'bbb', 'sd8887', '~gg', '~oo', 'gG~oo', 'lll~', '#sd5', 'ui9#', '#yyuyp#', '#ii#f#', '#n##']
    
    def Execute(self):
        result = str(Process(["bash","clean"],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        print(result)
        PrintTree()
        for i in ["lll~",'#yyuyp#','#ii#f#','#n##']:
            if i not in result:
                return False
        return os.listdir(Config.temp_path)==['clean', 'aaa', 'bbb', 'sd8887', '~gg', '~oo', 'gG~oo', '#sd5', 'ui9#']
    
@AddExercise(id="ex03")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return 'find_sh.sh' in f and len(f)==1

    def Compile(self):
        cmd = "chmod 777 find_sh.sh"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        cmd = "mkdir ditEmpty dir1 dir2 dir3 dir1/subdir1 dir1/subdir2"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        cmd = "touch f1.sh dir1/f2.sh dir1/subdir1/f3.sh dir1/subdir2/f4.sh dir2/f5.sh dir3/f6.sh"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        cmd = "touch e1.png dir1/e2.txt dir1/subdir1/e3.shsh dir1/subdir2/e4.esh dir2/e5.xl dir3/e6.ok"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        PrintTree()
        print()
        return str([f+d for _, d, f in os.walk(Config.temp_path)])==str([['find_sh.sh', 'f1.sh', 'e1.png', 'ditEmpty', 'dir1', 'dir2', 'dir3'], [], ['f2.sh', 'e2.txt', 'subdir1', 'subdir2'], ['f3.sh', 'e3.shsh'], ['f4.sh', 'e4.esh'], ['f5.sh', 'e5.xl'], ['f6.sh', 'e6.ok']])
    
    def Execute(self):
        result = str(Process(["bash","find_sh.sh"],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        result = result.replace("\n","$\n")
        print(result)
        for _, _, f in os.walk(Config.temp_path):
            for file in f:
                if str(file).endswith(".sh"):
                    file = file.split('.')[0]
                    if file not in result:
                        PrintColor(file+" not here", Colors.RED)
                        return False
                else:
                    file = file.split('.')[0]
                    if file in result:
                        PrintColor(file+" here", Colors.RED)
                        return False
        return True
    
@AddExercise(id="ex04")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return 'MAC.sh' in f and len(f)==1

    def Compile(self):
        cmd = "chmod 777 MAC.sh"
        res = Process(cmd,stderr=True,shell=True,cwd=Config.temp_path)
        return True
    
    def Execute(self):
        result = str(Process(["bash","MAC.sh"],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        print(result)
        for i in result.split('\n'):
            if i == "":continue
            if i.count(':') != 5 and '\n' not in i:
                return False
        return True
    
@AddExercise(id="ex05")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Norme(self):
        f = [os.path.basename(i) for i in self.files]
        print(f)
        return '"\\?$*\'MaRViN\'*$?\\"' in f and len(f)==1

    def Compile(self):
        return True
    
    def Execute(self):
        result = str(Process(["cat",self.files['"\\?$*\'MaRViN\'*$?\\"']],cwd=Config.temp_path, stderr=True)).replace("\r\n","\n").replace("\r","\n")
        print(result)
        return result=="42"
    
class BaseExercise_ft_putchar(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Init(self):
        super().Init()
        file = os.path.join(Config.temp_path,"ft_putchar.c")
        shutil.copyfile(Join(os.path.dirname(__file__),'ft_putchar.c'),file)
        return True
    
@AddExercise(id="ex06")
class Exo(BaseExercise_ft_putchar):
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
    
@AddExercise(id="ex07")
class Exo(BaseExercise_ft_putchar):
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
    
@AddExercise(id="ex08")
class Exo(BaseExercise_ft_putchar):
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
    
@AddExercise(id="ex09")
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
    
@AddExercise(id="ex10")
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
    
@AddExercise(id="ex11")
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
    
@AddExercise(id="ex12")
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
    printf("0:%d\\n", ft_iterative_factorial(25));
    printf("479001600:%d\\n", ft_iterative_factorial(12));
    printf("0:%d\\n", ft_iterative_factorial(13));
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
0:0
479001600:479001600
0:0
"""
    
@AddExercise(id="ex13")
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
	printf("0:%d\\n", ft_recursive_factorial(25));
	printf("479001600:%d\\n", ft_recursive_factorial(12));
	printf("0:%d\\n", ft_recursive_factorial(13));
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
0:0
479001600:479001600
0:0
"""

@AddExercise(id="ex14")
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

@AddExercise(id="ex15")
class Exo(BaseExercise_ft_putchar):
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
    
@AddExercise(id="ex16")
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
    
@AddExercise(id="ex17")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        AutoMain(self.files["ft_strcmp.c"],"int ft_strcmp(char *s1, char *s2);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_strcmp.h"
int main(void)
{
    if (strcmp("a","a") == ft_strcmp("a","a"))
        printf("OK\\n");
    if (strcmp("a","b") == ft_strcmp("a","b"))
        printf("OK\\n");
    if (strcmp("ad","b") == ft_strcmp("ad","b"))
        printf("OK\\n");
    if (strcmp("bd","b") == ft_strcmp("bd","b"))
        printf("OK\\n");
    if (strcmp("b","bd") == ft_strcmp("b","bd"))
        printf("OK\\n");
    if (strcmp("bd","bqq") == ft_strcmp("bd","bqq"))
        printf("OK\\n");
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK")==6
    
@AddExercise(id="ex18")
class Exo(BaseExercise_ft_putchar):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        v = ExecuteCode(args=["test1","test2","test3"])=="test1\ntest2\ntest3\n"
        v2 = ExecuteCode()==""
        return v and v2
    
@AddExercise(id="ex19")
class Exo(BaseExercise_ft_putchar):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        return CompileTemp()

    def Execute(self):
        v = ExecuteCode(args=["a","B","C","AA","A","D","","12","1","123"])=="\n1\n12\n123\nA\nAA\nB\nC\nD\na\n"
        v2 = ExecuteCode()==""
        return v and v2

@AddExercise(id="ex20")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        
    def Init(self):
        super().Init()
        Config.valgrind.active = True
        return True

    def Compile(self):
        AutoMain(self.files["ft_strdup.c"],"char *ft_strdup(char *src);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode().count("OK") == 2
    
@AddExercise(id="ex21")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        
    def Init(self):
        super().Init()
        Config.valgrind.active = True
        return True

    def Compile(self):
        AutoMain(self.files["ft_range.c"],"int *ft_range(int min, int max);",
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="""0, 1, 2, 3, 4 : 0, 1, 2, 3, 4, 
NULL
-1, 0 :-1, 0, 
"""

@AddExercise(id="ex22")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Init(self):
        super().Init()
        Config.normeflag = ["-R","CheckDefine"]
        return True

    def Compile(self):
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
""")
        return CompileTemp()

    def Execute(self):
        tests = [
        ["-123"],
        ["-2147483647"],
        ["2147483647"],
        ["0"]
        ]
        resTXT = ""
        for i in tests:
            res = ExecuteCode(args=i)
            resTXT += res
        return resTXT=="""123
2147483647
2147483647
0
"""

@AddExercise(id="ex23")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Init(self):
        super().Init()
        Config.normeflag = ["-R","CheckForbiddenSourceHeader"]
        return True

    def Compile(self):
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
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()=="42,21"
    

from . import ResultDirEx24 as ResTree24

@AddExercise(id="ex24")
class Exo(BaseExercise_ft_putchar):
    def __init__(self, id):
        super().__init__(id)

    def Init(self):
        super().Init()
        MakeDir(Join(Config.temp_path,'srcs'))
        MakeDir(Join(Config.temp_path,'includes'))
        h_file = Join(Join(Config.temp_path,"includes"),"ft.h")
        shutil.copyfile(Join(os.path.dirname(__file__),'ft_ex24.h'),h_file)
        shutil.move(Join(Config.temp_path,'ft_putchar.c'),Join(Config.temp_path,'srcs','ft_putchar.c'))
        files = ['ex10/ft_swap.c',
        'ex17/ft_strcmp.c',
        'ex15/ft_putstr.c',
        'ex16/ft_strlen.c',]
        for file in files:
            file = Join(Config.project_path,file)
            if not os.path.isfile(file):
                PrintColor('file '+file+' not found',Colors.RED)
                return False
            PrintColor('file '+file+' copied',Colors.YELLOW)
            self.files[file] = self.CopyToTemp(file,"srcs")
        return True
    
    def GetFiles(self, path):
        return [d + f for _, d, f in os.walk(path)]
    
    def Norme(self):
        return CheckNorme(Config.temp_path)

    def Compile(self):
        v = True
        print("#"*5,"make","#"*5)
        print(Process(["make"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make)==str(self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make fclean","#"*5)
        print(Process(["make","fclean"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make_fclean)==str(self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make all","#"*5)
        print(Process(["make","all"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make_all)==str(self.GetFiles(Config.temp_path))) and v
    
        print("#"*5,"make clean","#"*5)
        print(Process(["make","clean"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make_clean)==str(self.GetFiles(Config.temp_path))) and v

        print("#"*5,"make re","#"*5)
        print(Process(["make","re"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make_re)==str(self.GetFiles(Config.temp_path))) and v
    
        print("#"*5,"make fclean","#"*5)
        print(Process(["make","fclean"],cwd=Config.temp_path))

        print("#"*5,"make libft.a","#"*5)
        print(Process(["make","libft.a"],cwd=Config.temp_path))
        PrintTree()
        v = IfValid(str(ResTree24.make_libft_a)==str(self.GetFiles(Config.temp_path))) and v

        #print(self.GetFiles(Config.temp_path))    
        return v

    def Execute(self):
        return True
    

@AddExercise(id="ex25")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)

    def Compile(self):
        self.vals = [0]+[-2147483648]+[2147483647]+[random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
        AutoMain(self.files["ft_foreach.c"],"void ft_foreach(int *tab, int length, void (*f)(int));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_foreach.h"

void ft_putnbr(int nb)
{
    printf("%d\\n", nb);
}

int main(void)
{
    static int len = """+str(len(self.vals))+""";
    int vals["""+str(len(self.vals))+"""] = """+str(self.vals).replace("[","{").replace("]","}")+""";

    ft_foreach(vals, len, &ft_putnbr);
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        return ExecuteCode()==("\n".join([str(i) for i in self.vals]))+"\n"
    
@AddExercise(id="ex26")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
    
    def Init(self):
        super().Init()
        #Config.valgrind.print = True
        Config.valgrind.active = True
        return True

    def Compile(self):
        AutoMain(self.files["ft_count_if.c"],"int ft_count_if(char **tab, int (*f)(char*));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_count_if.h"

int find(char *str)
{
    int index = 0;
    char c[2] = "X";
    while (str[index] != '\\0')
    {
        c[0] = str[index];
        if (atoi(c))
            return 1;
        index++;
    }
    return 0;
}

int main(int argc, char **argv)
{
    argv[argc-1] = 0;
    printf("%d\\n",ft_count_if(argv + 1 ,&find));
    return (0);
}
""")
        return CompileTemp()

    def Execute(self):
        tests = [
    ["1255","876045","40405"],
    [],
    ["00000"],
    ["00000", "1145"]
]
        res = ""
        for test in tests:
            res+=ExecuteCode(args=test+["NULL"])
        return res=="""3
0
0
1
"""


@AddExercise(id="ex27")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        
    def Init(self):
        super().Init()
        Config.valgrind.active = True
        return True

    def Compile(self):
        print("#"*5,"make","#"*5)
        print(Process(["make"],cwd=Config.temp_path))
        return "ft_display_file" in os.listdir(Config.temp_path)

    def Execute(self):
        Config.output_name = 'ft_display_file'
        file = Join(Config.temp_path,"text.txt")
        shutil.copyfile(Join(os.path.dirname(__file__),"text.txt"),file)
        with open(file,"r") as fic:
            txt = fic.read()
        v = True
        v = v and "File name missing.\n" in ExecuteCode(args=[], returnAll= True).stderr
        v = v and "Too many arguments.\n" in ExecuteCode(args=["text.txt","text.txt"], returnAll= True).stderr
        v = v and "Cannot read file.\n" in ExecuteCode(args=["nothing.txt"], returnAll= True).stderr
        v = v and ExecuteCode(args=["text.txt"])==txt
        return v