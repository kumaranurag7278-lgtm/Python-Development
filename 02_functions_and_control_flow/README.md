# Functions and control flow

Programs that stay running in a loop and use functions plus dictionaries.

## What I learned

- `def` with parameters and `return`
- dictionaries of nested data (coffee menu, celebrity stats)
- `while` loops and a flag to stop (`off`, wrong guess)
- `global` for a running total (`profit`)

## Programs

1. **coffee_machine.py** — order espresso/latte/cappuccino, pay with coins, type `report` or `off`. Resources go down after each drink.
2. **higher_lower.py** — compare two celebrities' follower counts; correct answers keep a streak.

## After this folder

You should be able to break a game into functions and keep state (resources, score, current celebrity A) across loop turns.

## How to run

```
python coffee_machine.py
python higher_lower.py
```

Coffee machine: type a drink name, then coin counts. `report` prints remaining water/coffee/milk.
