from BaseLib import *
Config.PATH_git = GetGitPath("C_11")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")



######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_foreach.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
vals = [0]+[-2147483648]+[random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
AutoMain(temp_c,"void ft_foreach(int *tab, int length, void(*f)(int));",
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
    static int len = """+str(len(vals))+""";
    int vals["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";

    ft_foreach(vals, len, &ft_putnbr);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res== ("\n".join([str(i) for i in vals]))+"\n"
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
path_c = Join(Config.PATH_git,"ex01/ft_map.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
vals = [0]+[-2147483648]+[random.randint(-10000,0) for i in range (15)]+[random.randint(0,10000) for i in range (15)]
AutoMain(temp_c,"int *ft_map(int *tab, int length, int (*f)(int));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_map.h"

int fct(int nb)
{
    return nb/2;
}

int main(void)
{
    static int len = """+str(len(vals))+""";
    int vals["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";

    int *res = ft_map(vals, len, &fct);
    for (int i = 0; i < len; i++)
        printf("%d\\n", res[i]);
    free(res);
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res== ("\n".join([str(int(i/2)) for i in vals]))+"\n"
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
path_c = Join(Config.PATH_git,"ex02/ft_any.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)

tests = [
    ["1255","876045","40405"],
    [],
    ["00000"]
]

AutoMain(temp_c,"int ft_any(char **tab, int (*f)(char*));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_any.h"

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
    argv[argc - 1] = NULL;
    printf("%d\\n",ft_any(argv + 1, &find));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i+["NULL"],returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == \
"""1
0
0
"""
valid = valid and v2
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 1")
print("#"*40)
print("")



######################
#Exo 3
######################
ResetTempDir()
print("#"*15,"Exo 3 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex03/ft_count_if.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)

tests = [
    ["1255","876045","40405"],
    [],
    ["00000"],
    ["00000", "1145"]
]

AutoMain(temp_c,"int ft_count_if(char **tab, int length, int (*f)(char*));",
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
    printf("%d\\n",ft_count_if(argv + 1, argc - 1 ,&find));
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
v2 = True
resTXT = ""
for i in tests:
    res = ExecuteCode(exc=["valgrind"], args=i,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == \
"""3
0
0
1
"""
valid = valid and v2
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
path_c = Join(Config.PATH_git,"ex04/ft_is_sort.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)


print("#"*15,"Exec","#"*15)
v2 = True
resTXT = ""
tests = [
    [1],
    [],
    [-1, 2, 2, 5],
    [1, 5, 1, 0],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 2, 2, 3, 4],
    [4, 3, 3, 2, 1],
    [1, 2, 3, 4, 1],
]

for vals in tests:

    AutoMain(temp_c,"int ft_is_sort(int *tab, int length, int(*f)(int, int));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_is_sort.h"

int cmp(int a, int b)
{
    return a - b;
}

int main(void)
{
    static int len = """+str(len(vals))+""";
    int vals["""+str(len(vals))+"""] = """+str(vals).replace("[","{").replace("]","}")+""";

    printf("%d\\n",ft_is_sort(vals, len ,&cmp));
    return (0);
}
"""
)
    CompileTemp()
    res = ExecuteCode(exc=["valgrind"],returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == \
"""1
1
1
0
1
1
1
1
0
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 4")
print("#"*40)
print("")



######################
#Exo 5
######################
Config.ExeName = "do-op"
ResetTempDir()
print("#"*15,"Exo 5 Norme","#"*15)
path_exo = Join(Config.PATH_git,"ex05")
listfiles = os.listdir(path_exo)
valid = CheckNorme(path_exo, 3)
IfValid(valid)
for file in listfiles:
    path = Join(path_exo,file)
    CopyToTemp(path)


print("#"*15,"Exec","#"*15)
v2 = True
resTXT = ""
tests = [
    ['10','/', '0'],
    ['10','%', '0'],
    ['-2147483648','+', '2147483647'],
    ['-2147483648','+', '0'],
    ['0','+', '2147483647'],
    ['2','+', '1'],
    ['10','/', '2'],
    ['10','*', '2'],
    ['10','%', '2'],
    ['10','#', '2'],
    ['10','##', '2'],


    [],
    ['1','+', '1'],
    ['42ami','-', '--+-20toto12'],
    ['1','p', '1'],
    ['1','+', 'toto3'],
    ['toto3','+', '4'],
    ['foo','plus','bar'],
]
print(Process(["make", "re"],cwd=tempDir))
for vals in tests:
    res = ExecuteCode(exc=["valgrind"], args=vals,returnAll = True)
    v2 = v2 and CheckMemory(res.stderr, False)
    resTXT += res.stdout
v2 = v2 and resTXT == \
"""Stop : division by zero
Stop : modulo by zero
-1
-2147483648
2147483647
3
5
20
0
0
0
2
62
0
1
4
0
"""
valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 5")
print("#"*40)
print("")

Config.ExeName = "Output"

######################
#Exo 6
######################
ResetTempDir()
print("#"*15,"Exo 6 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex06/ft_sort_string_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_sort_string_tab(char **tab);",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_sort_string_tab.h"
int main(int argc, char **argv)
{
    argv[argc - 1] = NULL;
    ft_sort_string_tab(argv + 1);
    argv++;
    while (*argv)
    {
        printf("%s\\n", argv[0]);
        argv++;
    }
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(args=["a","B","C","AA","A","D","","12","1","123","NULL"])
v2 = res=="\n1\n12\n123\nA\nAA\nB\nC\nD\na\n"
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
path_c = Join(Config.PATH_git,"ex07/ft_advanced_sort_string_tab.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
AutoMain(temp_c,"void ft_advanced_sort_string_tab(char **tab, int(*cmp)(char *, char *));",
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "ft_advanced_sort_string_tab.h"

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (*s1 != '\\0' && *s2 != '\\0' && *s1 == *s2)
	{
		s1++;
		s2++;
		i++;
	}
	if (*s1 == *s2)
		return (0);
	else
	{
		if (*s1 < *s2)
			return (-1);
		else
			return (1);
	}
}

int	ft_str_char_cmp(char *s1, char *s2)
{
	return (*s2 - *s1);
}

int main(int argc, char **argv)
{
    int (*fcts[])(char*,char*) = {&ft_strcmp, &ft_str_char_cmp};
    argv[argc - 1] = NULL;

    ft_advanced_sort_string_tab(argv + 2, fcts[atoi(argv[1])]);
    argv+=2;
    while (*argv)
    {
        printf("%s\\n", argv[0]);
        argv++;
    }
    return (0);
}
"""
)
CompileTemp()
print("#"*15,"Exec","#"*15)
tests = [
    ["0",   "a","B","C","AA","A","D","","12","1","123",    "NULL"],
    ["1",   "a","B","C","AA","A","D","","12","1","123",    "NULL"],
    ["1",   "NULL"],
    ["1",   "a",   "NULL"],
]
ress = [
    "\n1\n12\n123\nA\nAA\nB\nC\nD\na\n",
    "a\nD\nC\nB\nAA\nA\n12\n1\n123\n\n",
    "",
    "a\n",
]
v2 = True
for index in range(len(tests)):
    res = ExecuteCode(exc=["valgrind"], args=tests[index],returnAll = True)
    v2 = v2 and res.stdout==ress[index]
    v2 = v2 and CheckMemory(res.stderr, False)
    print("#"*15)

valid = valid and v2
IfValid(v2)
IfValid(valid,"Exo 7")
print("#"*40)
print("")

