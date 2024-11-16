from Module.Equasions import *
from Module.BasicFunctions import *

child = None

values_to_check = {
        "value1": (10, int),
        "value2": (3.14, float),
        "value3": (child, None),
        "value4": (10.11, int | float),
    }

CheckBool, CheckList = check(values_to_check)
print(CheckBool)
print(CheckList)

atoms = calc_atoms(10,325.2,None,226)
print(atoms)

gram = calc_atoms(None,325.2,263,None)
print(gram)