# Cree par Lfarhi le 07/02/2024
# Durant la piscine de 42
from BaseLib import *
from BaseMan import *
from BaseExercise import *
from Commandes import *
import sys

#sys.argv = ["Moulinette.py","print","Piscine.C_00"]
#sys.argv = ["Moulinette.py","Piscine.C_01"]

if len(sys.argv) < 2:
    print("Error argument")
    quit()

if sys.argv[1] in Commandes:
    try:
        args = sys.argv[2:]
        Commandes[sys.argv[1]](*args)
    except Exception as e:
        print(f"Error : {e}")
    quit()

name = sys.argv[1]
try:
    spec = importlib.import_module(f"Projects.{name}.{name.split('.')[-1]}")
except Exception as e:
    print("Error argument:",e)
    quit()

if len(sys.argv) == 3:
    ExecExercise(sys.argv[2])
else:
    ExecExercises()