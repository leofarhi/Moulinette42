from BaseLib import *
from BaseExercise import *
from random import randint
Exec("clear")
print(GetIdProject(__file__))
Config.project_path = GetGitPath(GetIdProject(__file__))
Config.normeflag = ["-R","CheckForbiddenSourceHeader"]

def generate(mini,maxi,size):
    lst = []
    if maxi - mini < size:
        raise Exception("Not enough number")
    for _ in range(size):
        rd = randint(mini,maxi)
        while rd in lst:
            rd = randint(mini,maxi)
        lst.append(rd)
    return lst


@AddExercise(id="push_swap")
class Exo(BaseExercise):
    def __init__(self, id):
        super().__init__(id)
        self.path = Config.project_path
        self.exepath = Join(Config.temp_path,"push_swap")
    
    def Compile(self):
        Config.valgrind.active = True
        #Config.valgrind.print = True
        print(Process(["make","re"],cwd=Config.temp_path))
        CopyToTemp(Join(os.path.dirname(os.path.realpath(__file__)),"checker_linux"))
        Process(["chmod","+x","checker_linux"],cwd=Config.temp_path)
        Process(["chmod","+x","push_swap"],cwd=Config.temp_path)
        return os.path.exists(self.exepath)
    
    def check(self,numbers):
        numbers = " ".join([str(x) for x in numbers])
        print(numbers)
        #print(Process("./push_swap "+numbers,cwd=Config.temp_path,shell=True))
        res = Process('ARG="'+numbers+'"; ./push_swap $ARG | ./checker_linux $ARG',cwd=Config.temp_path,shell=True,stderr= True)
        res = res.stdout + res.stderr
        res = str(res).replace("\r","").replace("\n","")
        v = "OK" in res
        PrintColor(res,Colors.GREEN if v else Colors.RED)
        if v:
            chrono = Chrono()
            chrono.Start()
            res = Process('ARG="'+numbers+'"; ./push_swap $ARG | wc -l',cwd=Config.temp_path,shell=True)
            chrono.Stop()
            res = str(res).replace("\r","").replace("\n","")
            PrintColor("Number of operation: "+res + " in "+str(chrono.GetSec(7))+"s",
                       Colors.GREEN)
        print()
        return v
    
    def Execute(self):
        r = True
        r = self.check([1,2,3]) and r
        r = self.check([4,5,6,1,2,3]) and r
        r = self.check([4,5,6,0,1,2,3]) and r
        r = self.check([4,5,6,7,1,2,3]) and r
        r = self.check([1,3,2]) and r
        r = self.check([2, 1, 3]) and r
        #TODO Check error same number
        #TODO Check error with over int
        #TODO Check error with no number (text)
        r = self.check(generate(0,100,10)) and r
        r = self.check(generate(0,100,100)) and r
        r = self.check(generate(-100,100,100)) and r
        r = self.check(generate(-200,200,300)) and r
        return r