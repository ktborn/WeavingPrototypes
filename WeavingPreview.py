import turtle
import datetime

# remember to use parens, even when there's no parameters to enclose.
bob = turtle.Turtle()
wd = 10
bob.speed(0) # fastest
turtle.mode("logo") # draws going up, is perhaps nicer for viewing a band0

# don't show the turtle
bob.ht()
# set the pen properties
bob.width(wd)
# start at bottom left
w = turtle.window_width()
h = turtle.window_height()
bob.teleport(-0.45 * w , -0.45 * h)     # there is other teleportation below, this won't work by itself.

def cm(st_color, int_forward):	#set color then move
    bob.color(st_color)
    bob.forward(int_forward * wd)

def check_len(heddle_set):
    try:
        return sum(h for _, h in heddle_set)
    except:
        return -1   # indicate an error, but still let the code execute 

def list_line2(colorList):
    # bob.teleport(bob.xcor() + wd,  -wd / 3)
    # border1()
    # for col, dist in colorList:
    #     cm(col, dist)
    # border2()
    print("I think this function, list_line2, is unused?")

def leave_gap():
    bob.teleport(bob.xcor() + 2* wd, 0)

def drawAHeddleSet_borderImplied(colorList, heightOffset):
    bob.teleport(bob.xcor() + wd, heightOffset)
    border1()
    for col, dist in colorList:
        cm(col, dist)
    border2()

def drawAHeddleSet_reqdBorders(colorList, border1, border2, heightOffset):
    bob.teleport(bob.xcor() + wd, heightOffset)
    for col, dist in border1:
        cm(col, dist)
    for col, dist in colorList:
        cm(col, dist)
    for col, dist in border2:
        cm(col, dist)

def drawAHeddleSet_noBorders(colorList, heightOffset):
    bob.teleport(bob.xcor() + wd, heightOffset)
    for col, dist in colorList:
        cm(col, dist)

def printHeddleOrder(listsOfLists):
    # the weave function has height offsets, declares that heddle B threads are before heddle A, which are before heddle C. 
    # TODO: output the heddle order for warping
    pass

def weavePattern_noBorders(listsOfLists, repeats= 2):
    ## Feedback on whether warp thread count is consistent, and a gauge for how wide the weaving would be.
    for i in listsOfLists: 
        print('The number of strings in this heddle group is ' + str(check_len(i)))

    # it's easier for my head to remember ABAC pattern, than whether it's 1232 or 1213
    def l_A(): drawAHeddleSet_noBorders(listsOfLists[0], 0 * wd/3)
    def l_B(): drawAHeddleSet_noBorders(listsOfLists[1], -1 * wd/3)
    def l_C(): drawAHeddleSet_noBorders(listsOfLists[2], 1 * wd/3)

    l_C()   # for sheep, at least, start with a field
    for i in range(repeats):
        l_A()
        l_B()
        l_A()
        l_C()
    leave_gap()
    if __name__ == "__main__": turtle.exitonclick()

def weavePattern_implicitBorders(listsOfLists, repeats= 2):
    ## Feedback on whether warp thread count is consistent, and a gauge for how wide the weaving would be.
    for i in listsOfLists: 
        print('The number of strings in this heddle group is ' + str(check_len(i)))

    # it's easier for my head to remember ABAC pattern, than whether it's 1232 or 1213
    def l_A(): drawAHeddleSet_borderImplied(listsOfLists[0], 0 * wd/3)
    def l_B(): drawAHeddleSet_borderImplied(listsOfLists[1], -1 * wd/3)
    def l_C(): drawAHeddleSet_borderImplied(listsOfLists[2], 1 * wd/3)

    l_C()   # for sheep, at least, start with a field
    for i in range(repeats):
        l_A()
        l_B()
        l_A()
        l_C()
    leave_gap()
    if __name__ == "__main__": turtle.exitonclick()

def weavePattern_ReqdBorders(listsOfLists, lowerBorder, upperBorder, repeats= 2):
    ## Feedback on whether warp thread count is consistent, and a gauge for how wide the weaving would be.
    for i in listsOfLists: 
        print('The number of strings in this heddle group is ' + str(check_len(i)))

    # it's easier for my head to remember ABAC pattern, than whether it's 1232 or 1213
    def l_A(): drawAHeddleSet_reqdBorders(listsOfLists[0],lowerBorder, upperBorder, 0 * wd/3)
    def l_B(): drawAHeddleSet_reqdBorders(listsOfLists[1],lowerBorder, upperBorder, -1 * wd/3)
    def l_C(): drawAHeddleSet_reqdBorders(listsOfLists[2],lowerBorder, upperBorder, 1 * wd/3)

    l_C()   # for sheep, at least, start with a field
    for i in range(repeats):
        l_A()
        l_B()
        l_A()
        l_C()
    leave_gap()
    if __name__ == "__main__": turtle.exitonclick()

def exitOnCommand():
    turtle.exitonclick()


def saveToSvg(filename):
    import canvasvg

    if  filename[-4:].lower() != ".svg":
        filename  += ".svg"
    cv = turtle.Screen().getcanvas()
    canvasvg.saveall(filename,cv) 

def saveToSvg_timestamp(filename_prefix):
    now = datetime.datetime.now()
    dated_filename = filename_prefix + now.strftime("_%Y%m%d_%H%M%S") + ".svg"
    saveToSvg(dated_filename)




def border1():
    cm('black', 3)
    cm('white', 1)
    cm('black', 1)

def border2():
    cm('black', 1)
    cm('white', 1)
    cm('black', 3)
    cm('white', 1) # used for visual effect in Turtle, not a literal weaving string.
    # Every other movement is truncated by the following movement, so it's a wide C shape
    # but the last movement gets a round dot. Having a final movement 
    # where the ink  = background is intended to truncate the round pen
    # and provide a consistent visual width for each string - more realistic

# working towards having a list, rather than separate lines. Would a list let me output the string count, make it easier to check how close they are?
l_border1 = [('black', 3), 
             ('white', 1),
             ('black', 1)]

l_sheepLeg = [    ('green', 2) # field
    ,('black', 4) # leg
    ,('white', 6) # sheep body
    ,('black', 1) # ear
    ,('green', 3) # field
    ,('dark green', 2) # hills
    ,('teal', 3 - 0)   # sky
]

l_sheepHead = [
    ('green', 2 + 4) # field
    ,('white', 4) # sheep body
    ,('black', 3)  # sheep head
    ,('white', 1)  # more wool
    ,('green', 3 )   # field
    ,('dark green', 2) # hills
    ,('teal', 3 -1)   # sky
]

l_field = [
    ('green', 15) # field
    ,('dark green', 2) # hills
    ,('teal', 4 )   # sky
]

theSheepLists = [l_sheepLeg, l_sheepHead, l_field]

if __name__ == "__main__":  
    weavePattern_ReqdBorders(theSheepLists, l_border1, l_border1, 1)