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
print(Process(["./ft_display_file", "ft_display_file.c"],cwd=tempDir))


IfValid(valid,"Exo 0")
print("#"*40)
print("")
