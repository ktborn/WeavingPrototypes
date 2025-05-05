# Several basic weaving designs:
# Adding to an individual heddle set, 
# adding equally to all heddle sets to make a stripe, 
# making a diamond with solid center, 
# making hills, 
# and evening out heddle sets by filling with a specified color.
# Diamonds and hills can be specified for the B heddle set or C heddle set. (Since A is the repeating set in ABAC patterns, it won't be the vertex of a diamond or hill)

DEBUG = False

def add_to_single_heddle(list_of_lists, list_index: int, color, height):
    """
    Add warp threads to the selected heddle. 
    Heddle group A = 0 index, B = 1, C = 2
    """
    if len(list_of_lists) > list_index: # not equal, b/c one-based counting vs zero indexed list
        new_warps = (color, height)
        list_of_lists[list_index].append(new_warps)


def stripe(list_of_lists, color, height):
    pw = (color, height)
    for l in list_of_lists:
        l.append(pw)

def solid_diamond_center(list_of_lists, bg_l, bg_u, fg, height_units: int, center_on_C: bool):
    """
    Draw a solid diamond across 3 heddle sets
    Allows for distinct lower background and upper background colors
    Assumes lists are passed by reference and can be directly modified - does not return copy of lists.
    """

    if len(list_of_lists) == 3:
        heddle_set_A = list_of_lists[0]
        heddle_set_B = list_of_lists[1]
        heddle_set_C = list_of_lists[2]
    
    
        diamond_shortest_section = [
        (bg_l, 2 * height_units),
        (fg, 1 * height_units),
        (bg_u, 2 * height_units)]

        diamond_medium_section = [

        
        (bg_l, 1 * height_units),
        (fg, 3 * height_units),
        (bg_u, 1 * height_units) ]

        diamond_tallest_section = [
        (fg, 5 * height_units)]

        # The medium section has to be the repeated part in ABAC
        heddle_set_A.extend(diamond_medium_section)

        # The tallest part of the diamond could fall on B or on C
        if center_on_C == True:
            heddle_set_C.extend(diamond_tallest_section)
            heddle_set_B.extend(diamond_shortest_section)
        else:
            heddle_set_B.extend(diamond_tallest_section)
            heddle_set_C.extend(diamond_shortest_section)
        
        if DEBUG: print("After the diamond section", list_of_lists)

def fill_to_level(list_of_lists, fill_color):
    max_warp_threads = max(sum(h for _, h in heddle_set) for heddle_set in list_of_lists)

    for heddle_set in list_of_lists:
        warp_threads = sum(h for _, h in heddle_set)
        if warp_threads < max_warp_threads:
            make_level = (fill_color, max_warp_threads - warp_threads)
            heddle_set.append(make_level)

def hills_uneven_warp_threads(list_of_lists, hill_color,  height_units: int, center_on_C: bool):
    """
    Draw an upward pointing triangle across 3 heddle sets - there is NO upper fill. 
    Assumes lists are passed by reference and can be directly modified - does not return copy of lists.
    """

    if len(list_of_lists) == 3:
        heddle_set_A = list_of_lists[0]
        heddle_set_B = list_of_lists[1]
        heddle_set_C = list_of_lists[2]
    
        hill_shortest_section = [
        (hill_color, 1 * height_units)]

        hill_medium_section = [        
        (hill_color, 2 * height_units) ]

        hill_tallest_section = [
        (hill_color, 3 * height_units)]

        # The medium section has to be the repeated part in ABAC
        heddle_set_A.extend(hill_medium_section)

        # The tallest part of the diamond could fall on B or on C
        if center_on_C == True:
            heddle_set_C.extend(hill_tallest_section)
            heddle_set_B.extend(hill_shortest_section)
        else:
            heddle_set_B.extend(hill_tallest_section)
            heddle_set_C.extend(hill_shortest_section)
        
        if DEBUG: print("After the triangle section", list_of_lists)


def solid_hills(list_of_lists, color_lower, color_upper, height_units: int, center_on_C: bool):
    """
    Draw an upward pointing triangle across 3 heddle sets, using a top color to fill the heddle sets evenly (making downward pointing triangle)
    Assumes lists are passed by reference and can be directly modified - does not return copy of lists.
    """

    if len(list_of_lists) == 3:
        heddle_set_A = list_of_lists[0]
        heddle_set_B = list_of_lists[1]
        heddle_set_C = list_of_lists[2]
    
    
        hill_shortest_section = [
        (color_lower, 1 * height_units),
        (color_upper, 2 * height_units)]

        hill_medium_section = [        
        (color_lower, 2 * height_units),
        (color_upper, 1 * height_units) ]

        hill_tallest_section = [
        (color_lower, 3 * height_units)]

        # The medium section has to be the repeated part in ABAC
        heddle_set_A.extend(hill_medium_section)

        # The tallest part of the diamond could fall on B or on C
        if center_on_C == True:
            heddle_set_C.extend(hill_tallest_section)
            heddle_set_B.extend(hill_shortest_section)
        else:
            heddle_set_B.extend(hill_tallest_section)
            heddle_set_C.extend(hill_shortest_section)
        
        if DEBUG: print("After the triangle section", list_of_lists)