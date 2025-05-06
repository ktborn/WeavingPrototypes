# Noodling around with southwestern inspired designs

import WeavingPreview as wv
import WeavingDesigns as wd
import DataTypeValidation as dtv

# Build a design
my_weaving = [
    [],
    [],
    []
]

wd.stripe(my_weaving, "green", 2)
wd.stripe(my_weaving, 'red', 1)
wd.solid_diamond_center(my_weaving, "white", "white", "darkorange", 1, False)
wd.stripe(my_weaving, 'red', 1)
wd.stripe(my_weaving, "green", 2)
wd.stripe(my_weaving, "green", 2)
wd.add_to_single_heddle(my_weaving, 0, "green", 1)
wd.fill_to_level(my_weaving, "royalblue4")
wd.stripe(my_weaving, 'royalblue4', 3)

wd.hills_uneven_warp_threads(my_weaving, "sienna", 3, True)
wd.stripe(my_weaving, 'saddlebrown', 2)
wd.fill_to_level(my_weaving, 'skyblue')
wd.stripe(my_weaving, 'skyblue', 2)

# see the output
wv.weavePattern_noBorders(my_weaving, 4)
# print(my_weaving) # a prettyprint function doesn't yet exist for the weaving pattern, it's in the TODO list.

# Build a different design
my_weaving2 = [
    [],
    [],
    []
]

wd.stripe(my_weaving2, 'turquoise', 3)
wd.solid_diamond_center(my_weaving2, 'white', 'black', 'red', 1, False)
wd.solid_diamond_center(my_weaving2, 'black', 'red', 'white', 1, False)
wd.solid_diamond_center(my_weaving2, 'red', 'white', 'black', 1, False)


# View it so far, with and without borders
wv.weavePattern_implicitBorders(my_weaving, 3)   # implied border
wv.weavePattern_noBorders(my_weaving2, 4)

# Keep building on this design
wd.solid_diamond_center(my_weaving2, 'white', 'black', 'red', 1, False)
wd.solid_diamond_center(my_weaving2, 'black', 'red', 'white', 1, False)
wd.solid_diamond_center(my_weaving2, 'red', 'white', 'black', 1, False)

# View it
wv.weavePattern_noBorders(my_weaving2, 4)

# Continue incremental building 
wd.stripe(my_weaving2, 'white', 1)
wd.stripe(my_weaving2, 'turquoise', 3)
# and viewing
wv.weavePattern_noBorders(my_weaving2, 4)


## Redo the original my_weaving, slight variations
my_weaving3 = [
    [],
    [],
    []
]

# Build design
wd.stripe(my_weaving3, "black", 2)
wd.stripe(my_weaving3, 'red', 1)
wd.solid_diamond_center(my_weaving3, "red", "red", "white", 1, False)
wd.stripe(my_weaving3, 'red', 1)
wd.stripe(my_weaving3, "black", 2)
wd.stripe(my_weaving3, "green", 4)
wd.add_to_single_heddle(my_weaving3, 1, "green", 1)
wd.fill_to_level(my_weaving3, "royalblue4")
wd.stripe(my_weaving3, 'royalblue4', 2)

wd.hills_uneven_warp_threads(my_weaving3, "sienna", 2, True)
wd.stripe(my_weaving3, 'chocolate', 3)
wd.stripe(my_weaving3, 'saddlebrown', 3)
wd.fill_to_level(my_weaving3, 'skyblue')
wd.stripe(my_weaving3, 'skyblue', 2)

# View design
wv.weavePattern_noBorders(my_weaving3, 3)

wv.saveToSvg_timestamp("TimeToWeave") # Save all the screen output
wv.exitOnCommand() # Don't instantly disappear the design