from BaseLib import *

class BaseMan:
	def __init__(self, args = []) -> None:
		self.args = args

	def Print(self):
		pass

Mans = {}

def AddMan(id):
    def decorator(classType):
        Mans[id] = classType(sys.argv[3:])
        return classType
    return decorator

@AddMan('')
class NoMan(BaseMan):
	def Print(self):
		print("No man for this project")

def ExecMan(id):
	if id not in Mans:
		PrintColor("No man for this ID", Colors.RED)
		return
	Mans[id].Print()