from Module.BasicFunctions import check
child = None

def test_check_correct_values():
    # Test with all correct types
    values_to_check = {
        "value1": (10, int),
        "value2": (3.14, float),
        "value3": ("hello", str),
        "value4": (10.11, int | float),
        "value5": (child,None)
    }
    assert check(values_to_check) == True

def test_check_incorrect_type():
    # Test with one incorrect type
    values_to_check = {
        "value1": (10, int),
        "value2": ("3.14", float),  # Incorrect type
    }
    assert check(values_to_check) == False

def test_check_empty_dict():
    # Test with an empty dictionary
    values_to_check = {}
    assert check(values_to_check) == True  # No values to check, should pass