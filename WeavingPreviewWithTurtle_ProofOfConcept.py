import turtle
  
bob = turtle.Turtle()
wd = 10

turtle.mode("logo") # draws going up, is perhaps nicer for viewing a band
bob.ht() # don't show the turtle
bob.width(wd) # set the pen properties


def check_len(string_group):
    return sum(n for _, n in string_group)

def cm(st_color, int_forward):	#set color then move
    bob.color(st_color)
    bob.forward(int_forward * wd)

l_border1 = [('black', 3), 
             ('white', 1),
             ('black', 1)]

l_sheepLeg = [    ('green', 2) # field
    ,('black', 4) # leg
    ,('white', 6) # wooly sheep body
    ,('black', 1) # ear
    ,('green', 3) # field
    ,('dark green', 2) # hills
    ,('teal', 3 )   # sky
]

l_sheepHead = [
    ('green', 2 + 4) # field
    ,('white', 4) # wooly sheep body
    ,('black', 3)  # sheep head
    ,('white', 1)  # more wool
    ,('green', 3 )   # field
    ,('dark green', 2) # hills
    ,('teal', 2)   # sky
]

l_field = [
    ('green', 15) # field
    ,('dark green', 2) # hills
    ,('teal', 4 )   # sky
]

theSheepLists = [l_sheepLeg, l_sheepHead, l_field]

def list_any_line(colorList, border1, border2, heightOffset):
    bob.teleport(bob.xcor() + wd, heightOffset)
    for col, dist in border1:
        cm(col, dist)
    for col, dist in colorList:
        cm(col, dist)
    for col, dist in border2:
        cm(col, dist)

def weaveLists(listsOfLists, lowerBorder, upperBorder, repeats= 2):
    ## do something to check whether the length is consistent?
    for i in listsOfLists: 
        print('The number of strings in this heddle group is ' + str(check_len(i)))

    # it's easier for my head to remember ABAC pattern, than whether it's 1232 or 1213
    def l_A(): list_any_line(listsOfLists[0],lowerBorder, upperBorder, 0 * wd/3)
    def l_B(): list_any_line(listsOfLists[1],lowerBorder, upperBorder, -1 * wd/3)
    def l_C(): list_any_line(listsOfLists[2],lowerBorder, upperBorder, 1 * wd/3)

    l_C()   # for sheep, at least, start with a field
    for i in range(repeats):
        l_A()
        l_B()
        l_A()
        l_C()
    if __name__ == "__main__": turtle.exitonclick()

def exitOnCommand():    # function when used as an imported module
    turtle.exitonclick()

if __name__ == "__main__":  
    weaveLists(theSheepLists, l_border1, l_border1, 4)