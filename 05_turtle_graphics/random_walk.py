"""Random walk: turtle steps in one of four directions with a random RGB color.

colormode(255) lets us use 0–255 for red, green, and blue instead of 0.0–1.0.
"""

from turtle import Turtle, Screen
import random


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


direction = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.speed("fast")
timmy.pensize(20)
for _ in range(200):
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.color(color_change())

screen.exitonclick()
