# Python learning projects

Personal practice from beginner syntax through Turtle graphics and small games.

## How this repo is organized

| Folder | What is in it |
|---|---|
| [01_beginner](01_beginner/) | Inputs, math, if/else, lists, random, a password generator |
| [02_functions_and_control_flow](02_functions_and_control_flow/) | Functions, dictionaries, and game loops |
| [03_file_handling](03_file_handling/) | Reading a text file with a safe path |
| [04_oop](04_oop/) | Classes, attributes, methods, PrettyTable |
| [05_turtle_graphics](05_turtle_graphics/) | Turtle drawings, etch-a-sketch, race, Hirst dots |
| [06_projects](06_projects/) | True/False quiz and Snake |

## Setup

Python 3 is enough for almost everything. Turtle is in the standard library.

The only extra package is **prettytable** (OOP demo):

```
pip install -r requirements.txt
```

## How to run a program

From this folder, pass the path to the file. Examples:

```
python 01_beginner/tip_calculator.py
python 02_functions_and_control_flow/coffee_machine.py
python 06_projects/quiz/main.py
python 06_projects/snake_game/main.py
```

Turtle programs open a window. Click the window to close them when the code uses `exitonclick()`.

## What you should be able to do after this repo

- Use variables, types, f-strings, and if/else
- Loop, pick random values, and store data in lists and dictionaries
- Split a program into functions
- Read a file next to your script
- Build a class and use someone else's class (`PrettyTable`, `Turtle`)
- Combine several modules into one project (quiz, snake)
