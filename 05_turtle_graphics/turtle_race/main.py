"""Turtle race: bet on a color, then six turtles run to the right edge.

Each turtle gets a unique color from the list. The loop stops when one
turtle's x position is past 230 (near the finish).
"""

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make a bet",
    prompt="Which turtle will win the race? Enter the color: ",
)
colors = ["red", "yellow", "green", "pink", "blue", "orange"]

y_axis = -200
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    y_axis = y_axis + 50
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    random_color = random.choice(colors)
    new_turtle.color(random_color)
    colors.remove(random_color)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have won! The {winning_color} is the winner")
                else:
                    print(f"You have lost! The {winning_color} is the winner")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
