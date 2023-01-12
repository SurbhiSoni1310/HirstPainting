import colorgram
from turtle import Turtle, Screen
import turtle as t
import random
from time import sleep

t.colormode(255)
color = [(198, 13, 32), (250, 238, 17), (39, 76, 189), (39, 217, 69), (238, 226, 5), (229, 159, 46), (27, 40, 156),
         (215, 75, 13), (198, 15, 11), (15, 154, 15), (242, 35, 166), (229, 17, 121), (70, 10, 31),
         (61, 15, 8), (224, 141, 209), (11, 97, 62), (222, 160, 8), (51, 212, 230), (18, 19, 43), (11, 227, 239),
         (237, 156, 218), (87, 74, 209), (78, 211, 162), (84, 233, 199), (60, 233, 241), (4, 67, 41), (211, 90, 58),
         (176, 179, 228), (235, 169, 164), (8, 244, 224), (247, 10, 40), (4, 80, 115), (13, 58, 243)]

tom = Turtle()
screen = Screen()
tom.penup()
tom.setposition(-350, -250)
tom.pendown()

tom.speed("fastest")
while tom.xcor() <= -350 and tom.ycor() <= 250:
    while tom.xcor() <= 350:
        tom.dot(50, random.choice(color))
        tom.penup()
        tom.forward(100)
        tom.pendown()
    tom.penup()
    tom.setposition(-350, tom.ycor() + 100)
sleep(10)
