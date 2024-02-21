from BaseLib import *
import sys

Config.PATH_main = os.path.dirname(os.path.realpath(__file__))


if len(sys.argv) < 2:
    print("Error argument")
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



elif name == "Rush01":
    from Rush01.Rush01 import *

else:
    print("Error argument")