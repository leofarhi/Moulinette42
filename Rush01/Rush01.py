from BaseLib import *
Config.PATH_git = GetGitPath("Rush01")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

ResetTempDir()
listfiles = os.listdir(Config.PATH_git)
CheckNorme(Config.PATH_git)
for file in listfiles:
    path = Join(Config.PATH_git,file)
    CopyToTemp(path)

print("#"*15,"Exec","#"*15)
CompileTemp("-g")
#args=['1 1 1 1'] #Valid
#args=['2 1 1 2 2 1 1 2'] #Valid
#args=['1 2 2 3 2 1 3 2 1 3 3 2'] #Error
args=['1 2 3 2 3 2 1 2 1 2 2 2 4 1 3 2'] #Valid
#args=['4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2'] #valid
#args=['4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2 1 2 2 2 1 2 2 2 1 2 2 2 1 2 2 2 1 2 2 2'] #Error
#args=['1 2 4 3 2 3 1 2 3 3 1 2 4 3 2 3 1 2 3 3'] #Valid
#args=['3 1 3 2 2 1 4 2 2 3 2 3 2 2 1 3 2 1 2 4'] #Valid

res = ExecuteCode(exc=["valgrind"],args=args,returnAll = True, cat_e = True)
CheckMemory(res.stderr)

#res = ExecuteCode(args=args, cat_e = True)

print("#"*40)

