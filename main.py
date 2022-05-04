# import colorgram
import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)
#
# color_list = colorgram.extract("image.jpg", 20)
# for index in range(len(color_list)):
#     color_list[index] = tuple(color_list[index].rgb)
# print(color_list)
color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237),
              (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234),
              (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97),
              (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]
tod = Turtle()
tod.speed("fastest")
tod.pu()
tod.setposition(-250,-250)
tod.pd()
for y in range(10):
    old_y = tod.ycor()
    print(old_y)
    for x in range(10):
        color = color_list[randint(0, len(color_list)-1)]
        tod.dot(20, color)
        tod.pu()
        tod.forward(50)
        tod.pd()
    tod.pu()
    new_y = old_y + 50
    tod.setposition(-250, new_y)
    tod.pd()






screen = Screen()
screen.screensize(1000,500)
screen.exitonclick()
