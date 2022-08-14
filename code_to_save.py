#######################################################
# DRAW A SHAPE OF ANY SIZE i.e. triangle - hexangle etc
#######################################################


from turtle import Turtle, Screen
import random as r

tiny = Turtle()

# num_sides = 7


def draw_shape(num_sides, col="blue", s=3):
    tiny.color(col)
    tiny.pensize(s)
    angle = 360 / num_sides
    for x in range(num_sides):
        tiny.forward(100)
        tiny.left(angle)


colors = ['blue', 'red', 'green', 'black', 'orange', 'yellow']
for _ in range(3, 11):
    draw_shape(_, col=r.choice(colors))



# draw_shape(3, "red")
# draw_shape(4, "yellow", 2)
# draw_shape(5, "blue", 3)
# draw_shape(6, "green", 4)
# draw_shape(7, "brown", 5)
# draw_shape(8, "skyblue", 6)
# draw_shape(9, "orange", 7)
# draw_shape(10, "black", 8)

#############
# END
#############

# ////////////////

####################
# RANDOM WALK START:
####################


from turtle import Turtle, Screen
import random as r

tiny = Turtle()
colors = ['blue', 'red', 'green', 'black', 'orange', 'yellow', '#273c75', 'pink', '#ffd700', '#9c88ff']
directions = [0, 90, 180, 270]

def draw_shape(col, s=15):
    tiny.pensize(s)
    tiny.speed('fastest')
    for x in range(200):
        # randwalk = r.randrange(0, 361, 90)
        #* or pass in 'randwalk' to setheading()
        tiny.color(r.choice(col))
        tiny.forward(25)
        tiny.setheading(r.choice(directions))


#>>> ALTERNATIVE FOR COMPLETELY RANDOM COLOUR:



import turtle as t
import random as r

tiny = t.Turtle()


def rand_col():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


colors = rand_col()
directions = [0, 90, 180, 270]
t.colormode(255)
tiny.pensize(15)
tiny.speed('fastest')

for x in range(100):
    # randwalk = r.randrange(0, 361, 90)
    #* or pass in 'randwalk' to setheading()
    tiny.color(rand_col())
    tiny.forward(25)
    tiny.setheading(r.choice(directions))

screen = t.Screen()
screen.exitonclick()



#############
# END
#############

