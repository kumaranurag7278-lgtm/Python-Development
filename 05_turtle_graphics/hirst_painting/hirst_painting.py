"""Hirst-style painting: a grid of colored dots.

Imports RGB tuples from color_palette. Nested loops: 20 rows, 15 dots each.
penup so the turtle does not draw lines between dots.
"""

from color_palette import collection
import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
timmy.hideturtle()
screen.colormode(255)

timmy.penup()
start_x = -300
current_y = -300
timmy.setposition(start_x, current_y)

for _ in range(20):
    current_y = current_y + 30
    for _ in range(15):
        colors = random.choice(collection)
        timmy.dot(20, colors)
        timmy.forward(50)
    timmy.setposition(start_x, current_y)

screen.exitonclick()
