# File handling

How to open a file that lives next to the script, even if you run Python from another folder.

## What I learned

- `open` modes (read, append, create)
- `with open(...)` so the file closes automatically
- `os.path.dirname(__file__)` + `os.path.join` for a reliable path
- always close files if you use the old `f = open(...)` style

## Programs

1. **read_file_demo.py** — reads **sample_file.txt** and prints it.
2. **sample_file.txt** — the text being read.

Commented lines in the demo show create (`"x"`) and append (`"a"`).

## After this folder

You should be able to read a project file without hard-coding `C:\...` paths.

## How to run

```
python read_file_demo.py
```
