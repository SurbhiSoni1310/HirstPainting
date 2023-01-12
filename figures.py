from turtle import Turtle, Screen
import random

toto = Turtle()
toto.pencolor()


def move_right(angle):
    toto.forward(100)
    toto.right(angle)


def draw_figure(sides, angle):
    toto.begin_fill()
    change_color()
    for i in range(0, sides):
        move_right(angle)
    toto.end_fill()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    toto.color(R, G, B)
    toto.fillcolor((R, G, B))


for i in range(3, 11):
    draw_figure(i, 360 / i)

screen = Screen()
screen.exitonclick()
