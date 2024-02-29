from BaseLib import *
import C_09.ResultDir as ResTree
Config.PATH_git = GetGitPath("C_10")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
files = os.listdir(Join(Config.PATH_git,"ex00"))
count = 0
for i in files:
    if i[-2:] in [".c",".h"]:
        count+=1
valid = CheckNorme(Join(Config.PATH_git,"ex00"), count)
IfValid(valid)
for file in files:
    CopyToTemp(Join(Join(Config.PATH_git,"ex00"), file))
print("#"*15,"Exec","#"*15)
print(Process(["make"],cwd=tempDir))
v3 = PrintTree() == \
""".
├── ft_display_file
├── ft_display_file.c
└── Makefile

0 directories, 3 files
"""
IfValid(v3)

filePath = Join(tempDir,"ft_display_file.c")
print(filePath)
with open(filePath, "r") as fic:
    text = fic.read()
res = Process(["./ft_display_file", filePath],cwd=tempDir)
print(res)
v2 = str(res)==text
valid = valid and v2
IfValid(v2)

res = Process(["./ft_display_file", filePath,filePath],stderr=True,cwd=tempDir)
print(res.stderr)
IfValid(str(res.stderr)=="Too many arguments.\n")

res = Process(["./ft_display_file"],stderr=True,cwd=tempDir)
print(res.stderr)
IfValid(str(res.stderr)=="File name missing.\n")

res = Process(["./ft_display_file",Join(tempDir,"nothing.c")],stderr=True,cwd=tempDir)
print(res.stderr)
IfValid(str(res.stderr)=="Cannot read file.\n")

print(Process(["make","fclean"],cwd=tempDir))
v3 = PrintTree() == \
""".
├── ft_display_file.c
└── Makefile

0 directories, 2 files
"""
IfValid(v3)
print(Process(["make","all"],cwd=tempDir))
v3 = PrintTree() == \
""".
├── ft_display_file
├── ft_display_file.c
└── Makefile

0 directories, 3 files
"""
IfValid(v3)
print(Process(["make","clean"],cwd=tempDir))
v3 = PrintTree() == \
""".
├── ft_display_file
├── ft_display_file.c
└── Makefile

0 directories, 3 files
"""
IfValid(v3)


IfValid(valid,"Exo 0")
print("#"*40)
print("")
