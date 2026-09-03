"""Spirograph: many circles, each rotated by a small heading change.

size_of_gap is the turn in degrees. 360 / gap = how many circles complete
one full spin.
"""

from turtle import Turtle, Screen
import random


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(color_change())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
