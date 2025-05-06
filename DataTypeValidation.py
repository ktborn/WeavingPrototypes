# Data type validation for weaving

def is_valid_heddle_set(single_heddle_set):
    """
    Test whether the provided variable meets the expectations for a heddle set
    1. is it a list
    2. is each list element a tuple
    2a. where the tuple contains exactly 2 elements
    2b. the first element is a string
    2c. and the second element is an integer

    TODO: optional future feature: validate the string is a supported color name

    Args:
        single_heddle_set: something intended to be a heddle set
    """

    # test overall data type
    if not isinstance(single_heddle_set, list):
        return (False, "The overall data is not a list, it is", type(single_heddle_set))
    
    # test each list item
    for i in single_heddle_set:
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

def is_valid_list_of_heddle_sets(lists_of_heddle_sets, expected_num_sets = None):
    """
    Validates whether an input is a well formatted list of heddle sets. Optionally validates whether the list is the expected length - such as 3 heddle sets for Turned Krokbragd style

    Args:
        lists_of_heddle_sets: something intended to be a list of items which themsleves pass the validation for heddle sets
        expected_num_sets: optional. An integer for the expected length of the list. 

    """
    if not isinstance(lists_of_heddle_sets, list):
        return(False, "The overall data is not a list, it is", type(lists_of_heddle_sets))
    
    # keep describing issues if it's not the expected length - are the ones that are present valid heddle sets?
    is_valid = True
    description = ""

    if expected_num_sets is not None:
        if not len(lists_of_heddle_sets) == expected_num_sets:
            is_valid = False
            description += "The length of the list is not the expected length. "
        else:
            description += "The list is the expected length. "
    else:
        description += "The list length was not evaluated. "
    
    for i in lists_of_heddle_sets:
        result = is_valid_heddle_set(i)
        print("For list item", i, "the result was", result)
        if result[0] == False:
            description += "A list item is not a valid heddle set"
            return (False, description)
    #if is_valid:
    description += "The individual list items are all valid heddle sets."
    return (is_valid, description)

def is_valid_ABC_heddle_sets(lists_of_heddle_sets):
    return is_valid_list_of_heddle_sets(lists_of_heddle_sets, 3)


if __name__ == "__main__": 
    empty_list = []
    list_1_good = [('white', 1)]
    list_1_bad_reverse = [(1, 'black')]
    list_1_bad_tuple_size = [('black', 2, 'gray')]
    list_1_good = [('white', 1)]
    list_2_good = [('white', 1), ("green", 3)]

    # print(is_valid_heddle_set(empty_list))
    # print(is_valid_heddle_set(list_1_bad_reverse))
    # print(is_valid_heddle_set(list_1_bad_tuple_size))
    # print(is_valid_heddle_set(list_1_good))
    # print(is_valid_heddle_set(list_2_good))


    print(is_valid_list_of_heddle_sets([empty_list, list_1_good, list_2_good]))

    print(is_valid_list_of_heddle_sets([empty_list, list_1_good, list_2_good], 2))

    print(is_valid_list_of_heddle_sets([empty_list, list_1_good, list_1_bad_reverse]))
