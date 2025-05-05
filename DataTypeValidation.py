# Data type validation for weaving

def is_valid_heddle_set(input):
    """
    Test whether the provided variable meets the expectations for a heddle set
    1. is it a list
    2. is each list element a tuple
    2a. where the tuple contains exactly 2 elements
    2b. the first element is a string
    2c. and the second element is an integer

    TODO: validate the string is a supported color

    Args:
        input: something intended to be a heddle set
    """

    # test overall data type
    if not isinstance(input, list):
        return (False, "The overall data is not a list, it is", type(input))
    
    # test each list item
    for i in input:
        # test data type for list item
        if not isinstance(i, tuple):
            return(False, "An element in the list is not a tuple, it is", type(i))
        
        # test tuple length
        if not len(i) == 2:
            return(False, "A tuple in the list is not length 2, it is length", len(i))
        # test tuple data types
        if not isinstance(i[0], str):
            return(False, "A tuple has a leading value which is not a string, it is",  type(i[0]))
        
        if not isinstance(i[1], int):
            return(False, "A tuple has a second value which is not an integer, it is",  type(i[1]))
    
    return(True, "This is a well formatted heddle set.")

