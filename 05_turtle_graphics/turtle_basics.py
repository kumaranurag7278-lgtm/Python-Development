"""First Turtle graphics practice.

Most drawing code is commented so you can uncomment one exercise at a time.
The window stays open until you click it.

The coral "timmy" snippet at the bottom was your first Turtle demo
(from the PrettyTable lesson).
"""

from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")

# timmy_turtle.color("pink")
# timmy_turtle.forward(100)
# timmy_turtle.right(90)

# Square — method 1 (repeat forward + turn four times)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)

# Square — method 2 (loop)
# for _ in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)

# Dashed line
# for _ in range(15):
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()

# Draw triangle through decagon (3 to 10 sides)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)
#
# for shape_size_n in range(3, 11):
#     draw_shape(shape_size_n)

# --- first Turtle object (from the PrettyTable + Turtle intro lesson) ---
# timmy = Turtle()
# timmy.color("coral")
# timmy.forward(100)

screen = Screen()
screen.exitonclick()
