# Projects

Multi-file programs: a quiz (OOP + data) and Snake (Turtle + classes).

## What I learned

- split a program across modules (`main` vs model vs data)
- a class that holds a list of other objects (`QuizBrain`, `Snake`)
- game loop: update screen, check collisions, sleep a bit
- inheritance: `Food` and `ScoreBored` extend `Turtle`

## Quiz (`quiz/`)

True/False questions from **data.py**. **question_model.py** is one question. **quiz_brain.py** asks, checks, and scores. **main.py** builds the bank and runs the loop.

```
python quiz/main.py
```

Type `true` or `false` for each question.

## Snake (`snake_game/`)

**snake.py** — body segments and arrow-key heading. **food.py** — random dots. **scoreboard.py** — score and GAME OVER. **main.py** — collision with food, walls, and tail.

```
python snake_game/main.py
```

Use the arrow keys. Click the window when the game ends.

## After this folder

You should be able to keep related classes in separate files and import them from `main.py`.
