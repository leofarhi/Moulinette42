# Cree par Lfarhi le 01/02/2024
# Durant la piscine de 42
from BaseLib import *
import sys

Config.PATH_main = os.path.dirname(os.path.realpath(__file__))


if len(sys.argv) < 2:
    print("Error argument")
    quit()


if sys.argv[1] == "print":
    if len(sys.argv) < 3:
        print("Error argument")
    else:
        Exec("clear")
        Exec("bat "+Join(Config.PATH_main, sys.argv[2])+"/*.py")
    quit()

if sys.argv[1] == "path":
    if len(sys.argv) < 3:
        print("Error argument")
    else:
        GetGitPath(sys.argv[2], True)
    quit()

if sys.argv[1] == "git":
    if len(sys.argv) < 3:
        print("Error argument")
    else:
        Exec("clear")
        path = GetGitPath(sys.argv[2])
        if (path == None):
            print("Error argument")
        else:
            PrintTree(path)
            print("path :",path)
            cmt_name = input("commit name :")
            print(Process(["git","add","."],cwd=path))
            print(Process(["git","commit","-m",cmt_name],cwd=path))
            print(Process(["git","push"],cwd=path))
    quit()

if sys.argv[1] == "cd":
    if len(sys.argv) < 3:
        print("Error argument")
    else:
        path = GetGitPath(sys.argv[2])
        print("path :",path)
        if (path == None):
            print("Error argument")
        else:
            Exec('bash -c "cd '+path+'; exec bash"')
    quit()

name = sys.argv[1]

if name == "C_00":
    from C_00.C_00 import *

elif name == "C_01":
    from C_01.C_01 import *

elif name == "C_02":
    from C_02.C_02 import *

elif name == "C_03":
    from C_03.C_03 import *

elif name == "C_04":
    from C_04.C_04 import *

elif name == "C_05":
    from C_05.C_05 import *

elif name == "C_06":
    from C_06.C_06 import *

elif name == "C_07":
    from C_07.C_07 import *

elif name == "C_08":
    from C_08.C_08 import *

elif name == "C_09":
    from C_09.C_09 import *

elif name == "C_10":
    from C_10.C_10 import *

elif name == "C_11":
    from C_11.C_11 import *



elif name == "Rush01":
    from Rush01.Rush01 import *

elif name == "BSQ":
    from BSQ.BSQ import *

else:
    print("Error argument")