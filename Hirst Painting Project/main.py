import colorgram
#for extracting colors from a image
# rgb_colors=[]
# colors = colorgram.extract('spots.jpg', 30)
#
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

from PIL.ImImagePlugin import number
from PIL.ImageChops import screen

tim=turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]
tim.setheading(222)
tim.forward(300)
tim.setheading(0)
number_of_dots=100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()



