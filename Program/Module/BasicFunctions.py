
def check(values: dict) -> tuple[bool, list]:
    """
    A function to determine if the values in the dictionary are of the correct types. None values are skipped over as they provide no check.
    
    Args:
        values (dict): A dictionary where keys are value names and values are tuples of (value, expected_type).
            Example: {"value1": (10, int), "value2": (3.14, float)}
    
    Returns:
        bool: Returns True if all values match their expected types, False otherwise.
    
    Example:
    >>> values_to_check = {
        "value1": (10, int),
        "value2": (3.14, float),
        "value3": ("hello", str),
        "value4": (10.11, int | float),
        "value5": (child==None,None)
    }
    >>> assert check(values_to_check) == True
    """
    skipped_args: list = []
    for key, (value, expected_type) in values.items():
        if value is None:
            #skip value if its None
            skipped_args.append(key)
            continue

        #check if the value is the expected type
        elif not isinstance(value, expected_type):
            print(f"Error: '{key}' is not of type {expected_type}. Got {type(value)} instead.")
            return False, skipped_args

    return True, skipped_args
