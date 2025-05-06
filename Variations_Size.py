import WeavingPreview as wv
import DataTypeValidation as dtv 
import math # for rounding padding values

# written before I caught on that lists are passed by reference, so returning things wasn't needful

# Sample Borders (lists of color-height tuples)
no_border = []
white_border = [('white', 1)]
black_border = [('black', 3)]
# color lists
cl_ROYGBIV = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
cl_BGR = ['black', 'gray', 'red']

def combine_lists(bd, td):
    """
    Combines two designs

    Args:
        bd: bottom design. A list of 3 lists of color, height tuples. Each nested list is assumed to have the same total height
        td: top design. A list of 3 lists of color, height tuples.
    """
    new_design = [] 
    for i in range(min(len(bd), len(td))):  
        nd_l = []
        nd_l.append(bd[i]) 
        nd_l.append(td[i])
        new_design.append(nd_l)
    return new_design

def test_combine_lists():
    blue_stripe = [
        ['blue', 4],
        ['blue', 4],
        ['blue', 4]
    ]
    green_stripe = [
        ['green', 4],
        ['green', 4],
        ['green', 4]
    ]
    return combine_lists(blue_stripe, green_stripe)

def center_design(dh: int, bc, tc, lists):
    """
    Adds padding to the provided design with distinct bottom and top padding colors, to create the desired height. 
    Does not have an effect if the provided design is or exceeds the desired height. 
    In case of odd numbered padding, the extra goes to the top. 

    Args:
        dh (int): the desired height
        bc (str): the bottom color, using a Turtle-supported color name
        tc (str): the top color, using a Turtle-supported color name
        lists (list of color, height tuples): the existing design

    """ 
    new_lists = []
    for l in lists: 
        design_height = sum(t[1] for t in l)
        bh = int(math.floor((dh - design_height) / 2))
        th = int(math.ceil((dh - design_height)/ 2))

        if th > 0:
            l.insert(0, (bc, bh))
            l.append((tc, th))
        # new_lists += l # this may be creating a long list, vs list of lists
        new_lists.append(l)
    return new_lists

def size_variation():
    test_list = ['white', 'red']
    d1 = diamonds(test_list, 1)
    d2 = diamonds(test_list, 3)

    sh = 32 # standardized height
    c1 = center_design(sh, 'black', 'black', d1)
    c2 = center_design(sh, 'black', 'black', d2)

    return (c1, c2)

def test_center_design2():
    cl_BGR2 = cl_BGR + cl_BGR
    d1 = diamonds(cl_BGR2, 1)
    d2 = diamonds(cl_BGR, 2)

    sh = 35 # standardized height
    c1 = center_design(sh, 'black', 'black', d1)
    c2 = center_design(sh, 'black', 'black', d2)
    
    return (c1, c2)

def test_center_design3():
    d1 = diamonds(cl_BGR, 3)
    d2 = diamonds(cl_ROYGBIV, 1)

    sh = 50 # standardized height
    c1 = center_design(sh, 'black', 'black', d1)
    c2 = center_design(sh, 'black', 'black', d2)
    
    return (c1, c2)

    
   
def stripe(color, height):
    """
    Basic function: create a stripe of a given color and height
    """
    ABC = (color, height)
    design_ABC = [ABC, ABC, ABC]
    return design_ABC

def test_stripe_and_combine():
    s1 = stripe('blue', 4)
    s2 = stripe('green', 6)
    d1 = combine_lists(s1, s2)
    print("s1, s2, d1", s1, s2, d1)
    s3 = stripe('gray', 2)
    d2 = combine_lists(d1, s3)
    print('s3, d2', s3, d2)
    # wv.weavePattern_implicitBorders(d2)
    return d2

def diamonds(list_colors, height_unit = 3):
    diamond_A = []
    diamond_B = []
    diamond_C = []

    diamond_A = []
    for i in range(len(list_colors)):
        if i == 0:
            diamond_B += [(list_colors[i], 1* height_unit)]
            diamond_A += [(list_colors[i], 2* height_unit)]
            diamond_C += [(list_colors[i], 3* height_unit)]
        elif i % 2 == 1:
            diamond_B += [(list_colors[i], 5 * height_unit)]
            diamond_A += [(list_colors[i], 3 * height_unit)]
            diamond_C += [(list_colors[i], 1 * height_unit)]
        elif i % 2 == 0:
            diamond_B += [(list_colors[i], 1 * height_unit)]
            diamond_A += [(list_colors[i], 3 * height_unit)]
            diamond_C += [(list_colors[i], 5 * height_unit)]
    # finish the diamonds: equal # of threads in each heddle group
    if len(list_colors) % 2 == 0:
            diamond_B += [(list_colors[0], 1 * height_unit)]
            diamond_A += [(list_colors[0], 2 * height_unit)]
            diamond_C += [(list_colors[0], 3 * height_unit)]
    else:
        diamond_B += [(list_colors[0], 3 * height_unit)]
        diamond_A += [(list_colors[0], 2 * height_unit)]
        diamond_C += [(list_colors[0], 1 * height_unit)]

    diamond_ABC = [diamond_A, diamond_B, diamond_C]
    # if __name__ == "__main__": wv.weavePattern_ReqdBorders(diamond_ABC, black_border, black_border, 3)
    return diamond_ABC
    

cl_browns = ['DarkOrange', 'DarkRed', 'sienna1', 'tan']

def tests1():
    diamonds(cl_BGR)
    diamonds(cl_ROYGBIV)
    wv.saveToSvg('Diamond3.svg')
    wv.exitOnCommand()


c1, c2 = test_center_design2()
wv.weavePattern_implicitBorders(c1, 3)
wv.weavePattern_implicitBorders(c2, 3)
wv.saveToSvg("CenteredDesigns4.svg")

# print("test combine lists:", test_combine_lists())
# result_bool, result_desc  = dtv.is_valid_heddle_set(test_combine_lists())
# print("Validity of test_combine_lists output as a heddle set:", result_desc)
result_test_combine_lists = test_combine_lists()
result  = dtv.is_valid_heddle_set(result_test_combine_lists[0])
print("Validity of test_combine_lists output's first list item as a heddle set:", result)

result  = dtv.is_valid_list_of_heddle_sets(result_test_combine_lists)
print("Validity of test_combine_lists output as a list of heddle sets:", result)

result  = dtv.is_valid_ABC_heddle_sets(result_test_combine_lists)
print("Validity of test_combine_lists output as a Turned Krokbragd list of heddle sets:", result)

# result_bool, result_desc = dtv.is_valid_heddle_set(test_stripe_and_combine())
# print("Validity of test stripe and combine output as a heddle set", result_desc)
# # print( test_stripe_and_combine())
wv.exitOnCommand()
