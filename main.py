import turtle as t
import random as r

t.colormode(255)


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



tim = t.Turtle()
tim.speed(0)
tim.penup()


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

tim.hideturtle()
for i in range(1, 100 + 1):
    # tim.color(r.choice(color_list))
    tim.dot(20, r.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



# def rand_col():
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     random_color = (red, green, blue)
#     return random_color


#
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         tim.color(rand_col())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(4)

### used 'colorgram' module to extract the colours from the image and
### then used the 'colorgram' module to generate a list of colours

screen = t.Screen()
screen.exitonclick()