from BaseLib import *
Config.PATH_git = GetGitPath("C_06")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

######################
#Exo 0
######################
ResetTempDir()
print("#"*15,"Exo 0 Norme","#"*15)
path_c = Join(Config.PATH_git,"ex00/ft_print_program_name.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode()
v2 = res=="./Output\n"
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
path_c = Join(Config.PATH_git,"ex01/ft_print_params.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(args=["test1","test2","test3"])
v2 = res=="test1\ntest2\ntest3\n"
valid = valid and v2

res = ExecuteCode()
v2 = res==""
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
path_c = Join(Config.PATH_git,"ex02/ft_rev_params.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(args=["test1","test2","test3"])
v2 = res=="test3\ntest2\ntest1\n"
valid = valid and v2

res = ExecuteCode()
v2 = res==""
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
path_c = Join(Config.PATH_git,"ex03/ft_sort_params.c")
valid = CheckNorme(path_c)
IfValid(valid)
temp_c = CopyToTemp(path_c)
CompileTemp()
print("#"*15,"Exec","#"*15)
res = ExecuteCode(args=["a","B","C","AA","A","D",""])
v2 = res=="\nA\nAA\nB\nC\nD\na\n"
valid = valid and v2

res = ExecuteCode()
v2 = res==""
valid = valid and v2

IfValid(v2)
IfValid(valid,"Exo 3")
print("#"*40)
print("")