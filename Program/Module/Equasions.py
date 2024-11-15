import math
from .BasicFunctions import check

# constant variables 
global CURIE
global Avogadro #Avogadro constant

## set variables
CURIE: int = 3.7e10
Avogadro: int = 6.02214076e23

#----------------------------------Functions----------------------------------#
#Individual flexible functions for the calculations needed within the program.#
#The functions will only use the global variables as defined above. But none  #
#will pull information themselfs from the program or files. These are strictly#
#input and output functions.                                                  #
#-----------------------------------------------------------------------------#

def calc_atoms(gram: int | float, isotope_weight: int | float) -> float:
    """_summary_
    A function to calculate the number of atoms with material from its weight in grams.
    Args:
        gram (int): The amount of material in {grams}
        isotope_weight (int): The attomic weight of the material {gram/mol}
    
    Returns:
        float: returns the estimated number of atoms within the sample.
    """
    
    #check variables that are inputted
    values = {
        'V1': (gram, int|float),
        'V2': (isotope_weight, int|float),
    }
    if check(values) == False:
        raise ValueError('Values Not Correct format. Needs to be int or float.')


    #Calculate the number of mols of the material from grams
    mols:float = gram/isotope_weight

    #Calculate the number of atoms from mols and the global variable Avogadro
    atoms:float = mols*Avogadro
    
    return atoms

def decay_constant(half_life:int|float, units:str, conversion: int|float = 1, constant: int | float = None) -> float:
    """_summary_
    This function determines converts the half life of a isotope into seconds. Then using
    The half life equasion, determines the isotopes constant for decay.

    Args:
        half_life (int | float): The time it takes for half of the amount of a isotope to decay. Also known as half life.
        units (str): The units the half life is in.
        conversion (int | float): The direct conversion factor for.
        constant (int | float): The decay constant is added for backwords calculation.

    Returns:
        float: returns the decay constant for that element (1/s)
    """
    #Check the values that are inputed into the function.
    values = {
        'V1': (half_life, int|float),
        'V2': (units, str),
        'V3': (conversion, int|float),
        'V4': (constant, int|float),
    }
    if check(values) == False:
        raise ValueError("Invalid input types: 'half_life' should be int or float, 'units' should be str, "
                        "and 'conversion' should be int or float if provided.")
    
    #Determine the units the half life of the isotope is in. Then determine the conversion factor to convert to seconds
    if half_life is not None:
        match units:
            case 'Yr':
                conversion:int = 365*24*60*60
            case 'Day':
                conversion:int = 24*60*60
            case 'Hr':
                conversion:int = 60*60
            case 'min': 
                conversion = 60
            case 'sec': 
                conversion = 1
            case 'ms':
                conversion = 1/1000
            case 'micros':
                conversion = 1/1000000
            case 'ns':
                conversion = 1/1000000000
            case 'ps':
                conversion = 1/1000000000000
            case 'fs':
                conversion = 1/1000000000000000
            case 'as':
                conversion = 1/1000000000000000000
            case 'zs':
                conversion = 1/1000000000000000000000
            case _:
                if not conversion:
                    raise ValueError('There is no unit type or conversion number for time')
    
    if constant is None:
        #convert the half life to seconds
        time_hl: float = half_life * conversion

        #Calculate the isotope constant
        constant:float = math.log(2) / time_hl

        return constant
    
    elif half_life is None and constant is not None:
        #If no input of halflife, calculate the half life is there is a constant
        time_hl: float = math.log(2) / constant
        return time_hl
    
    else:
        raise ValueError('Half Life value or decay constant is missing. Provide Value for either.')

def decay(constant:int|float = None, atoms:int|float = None, dps: int|float = None) -> int|float:
    """_summary_
    determine the decay for the amount of the isotope. 

    Args:
        constant (int | float): the decay constant for the isotope
        atoms (int | float): the number of items at the time of decay
        dps (int | float): 
    Returns:
        int|float: returns the decay of a isotope in the units of CURIE
    """
    #check if variables are None or int.
    values = {
        'V1': (constant, int|float),
        'V2': (atoms, int|float),
        'V3': (dps, int|float),
    }
    if check(values) == False:
        raise ValueError()

    #Depending on what variables are feed into this function, the function will still calculate the decay in Ci's
    if dps is None and atoms is not None and constant is not None:
        dps: int|float = constant*atoms
        decay_curie: int|float = dps/CURIE
    if dps is not None:
        decay_curie: int|float = dps/CURIE
    else:
        raise ValueError('Not enough arguments to calculate decay.')

    return decay_curie
    

