# Turtle graphics

Python's built-in Turtle module: a window, a pen, and movement commands.

## What I learned

- `Turtle` and `Screen`, `forward`, `setheading`, `circle`, `dot`
- RGB with `colormode(255)`
- `onkey` for keyboard control
- loops to repeat shapes; `random` for color and distance
- splitting color data into its own module (`color_palette`)

## Programs

1. **turtle_basics.py** — first turtle; square, dashed line, and polygons are in comments (uncomment one at a time).
2. **turtle_colors.py** — a list of color names for `random.choice`.
3. **etch_a_sketch.py** — W/A/S/D to draw, C to clear. (This was named like a race before; it is drawing.)
4. **random_walk.py** — 200 random steps, thick pen, random RGB.
5. **spirograph.py** — overlapping circles with a 5° heading gap.
6. **turtle_race/main.py** — bet on a color; six turtles race.
7. **hirst_painting/hirst_painting.py** — grid of dots using **hirst_painting/color_palette.py**.

## After this folder

You should be able to open a Turtle window, draw with loops, and listen for keys.

## How to run

```
python turtle_basics.py
python etch_a_sketch.py
python random_walk.py
python spirograph.py
python turtle_race/main.py
python hirst_painting/hirst_painting.py
```

Click the Turtle window to exit programs that call `exitonclick()`.
