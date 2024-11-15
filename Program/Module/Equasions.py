import math
from BasicFunctions import check

# Create Global Variables 
#Why? Because future equations may require these variables
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

def calc_atoms(gram: int | float, isotope_weight: int | float, atoms:int|float = None, mols: int|float = None) -> float|int:
    """_summary_
    A function to calculate the number of atoms with material from its weight in grams.
    Args:
        gram (int|float): The amount of material in {grams}
        isotope_weight (int|float): The attomic weight of the material {gram/mol}
        atoms (int|float): the number of atoms within a sample
    
    Returns:
        float|int: returns the estimated number of atoms within the sample.
    """
    
    #check variables that are inputted
    values = {
        'gram': (gram, int|float|None),
        'Isotope Weight': (isotope_weight, int|float|None),
        'atoms':(atoms, int|float|None),
        'mols': (mols, int|float|None),
    }
    is_valid, skipped_args = check(values)  # Unpack the tuple

    if not is_valid: # if is_valid is false
        raise ValueError('Values Not Correct format. Needs to be int or float.')

    match skipped_args:
        case ['atoms']|['atoms','mols']:
            #Calculate the number of mols of the material from grams
            if not mols: #if there is no moles, calculate it
                mols:float = gram/isotope_weight
            #Calculate the number of atoms from mols and the global variable Avogadro
            atoms:float = mols*Avogadro
            return atoms
        
        case ['gram']|['gram','mols']:
            #Calculate the number of mols
            if not mols: #if there is no moles, calculate it
                mols:float = gram/isotope_weight
            #Calculate grams
            gram = mols * isotope_weight
            return gram
        
        case ['Isotope Weight']|['Isotope Weight','mols']:
            #Calculate the number of mols
            if not mols: #if there is no moles, calculate it
                mols:float = gram/isotope_weight
            #Calculate the Isotope Weight
            isotope_weight = mols / gram
            return isotope_weight
        
        case []:
            pass

        case _:
            raise ValueError('Error with list returned')


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
        'Half Life': (half_life, int|float|None),
        'Units': (units, str|None),
        'Conversion': (conversion, int|float|None),
        'constant': (constant, int|float|None),
    }
    is_valid, skipped_args = check(values)  # Unpack the tuple

    if not is_valid: # if is_valid is false
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

def decay(constant:int|float = None, atoms:int|float = None, dps: int|float = None, decay_curie: int|float = None) -> int|float:
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
        'constant': (constant, int | float | None),
        'atoms': (atoms, int | float | None),
        'dps': (dps, int | float | None),
        'decay_curie': (decay_curie, int | float | None),
    }

    is_valid, skipped_args = check(values)  # Unpack the tuple

    if not is_valid:
        print('Check Error with activity function')
        raise ValueError('Value Error!')

    # Handle skipped arguments with match
    match skipped_args:
        case ['decay_curie']|['decay_curie','dps']:
            # Calculate DPS and decay_curie if decay_curie is skipped
            dps: int | float = constant * atoms
            decay_curie: int | float = dps / CURIE
            return decay_curie
        case['decay_curie','constant','atoms']:
            decay_curie: int | float = dps / CURIE
        case []:
            # No skipped arguments, likely all values are provided
            pass
        case _:
            # Handle unexpected cases
            raise ValueError(f"Unexpected skipped arguments: {skipped_args}")

    
    

