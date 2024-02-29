from BaseLib import *
Config.PATH_git = GetGitPath("BSQ")

genPerl = Join(os.path.dirname(os.path.realpath(__file__)),"gen.pl")

def GenMap(w, h, d, name = "map.txt"):
    res = Process(["perl", genPerl, str(w), str(h), str(d)],cwd=tempDir).stdout
    with open(Join(tempDir,name), "w") as fic:
        fic.write(res)
    return res

def WriteMap(data, name = "map.txt"):
    with open(Join(tempDir,name), "w") as fic:
        fic.write(data)
    return data