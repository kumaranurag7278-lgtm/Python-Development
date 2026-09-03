"""Etch-a-sketch with the keyboard.

W forward, S back, A left, D right, C clear and return home.
This was originally in a file named turtle_race — it is drawing, not a race.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")
tim.pensize(3)
tim.pencolor("blue")


def move_forward():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def erase():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=erase)
screen.exitonclick()
