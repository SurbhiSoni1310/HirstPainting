import random
from turtle import Turtle, Screen

toto = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    toto.color(R, G, B)


toto.speed("fast")

for i in range(0, 36):
    change_color()
    toto.circle(100)
    toto.right(10)

screen = Screen()
screen.exitonclick()
