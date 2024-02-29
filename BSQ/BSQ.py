from BaseLib import *
Config.PATH_git = GetGitPath("BSQ")
Config.normeflag = "-R CheckForbiddenSourceHeader"

###############################

Exec("clear")

DelDir(tempDir)
print("#"*15,"BSQ Norme","#"*15)
listfiles = os.listdir(Config.PATH_git)
IfValid(CheckNorme(Config.PATH_git,14))
shutil.copytree(Config.PATH_git, tempDir, ignore=shutil.ignore_patterns("Moulinette"))
print("#"*15,"Compilation","#"*15)
print(Process(["make"],cwd=tempDir))
PrintTree()
print("#"*15,"Exec","#"*15)

if "lfarhi" in tempDir:
    import BSQ.lfarhi as userTst
elif "gicomlan" in tempDir:
    import BSQ.gicomlan as userTst

userTst.Init()
userTst.Execute()

#res = ExecuteCode(exc=["valgrind"],args=args,returnAll = True, cat_e = True)
#CheckMemory(res.stderr)

#res = ExecuteCode(args=args, cat_e = True)

print("#"*40)