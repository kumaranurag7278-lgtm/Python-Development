📧 Mail Merge Project

A simple **Mail Merge Project** built with Python as part of **Angela Yu's 100 Days of Python Bootcamp**.

The project takes a list of names and a letter template, replaces a placeholder in the template with each person's name, and creates a separate personalized letter for every person.

## 🚀 What This Project Does

The program:

1. Reads a list of names from a text file.
2. Reads a letter template.
3. Removes unnecessary whitespace from each name.
4. Replaces the placeholder `[name]` in the letter with the actual name.
5. Creates a separate file for each person.
6. Saves all personalized letters in an output folder.

### Example

If the names file contains:

```text
Anurag
Rahul
Aman
```

And the letter template contains:

```text
Dear [name],

You are invited to my party!
```

The program generates:

```text
Dear Anurag,

You are invited to my party!
```

```text
Dear Rahul,

You are invited to my party!
```

```text
Dear Aman,

You are invited to my party!
```

## 🧠 Concepts Learned

This project helped me understand the basics of **Python file handling** and working with text files.

### 1. Opening Files with `open()`

Learned how to open files using:

```python
open("file.txt")
```

and different file modes:

* `r` → Read
* `w` → Write
* `a` → Append

Example:

```python
with open("file.txt", "r") as file:
    content = file.read()
```

### 2. Using `with open()`

Used the `with` statement to work with files safely.

```python
with open("file.txt") as file:
    data = file.read()
```

Using `with` automatically handles closing the file after the operation is completed.

### 3. Reading File Contents

Used `.read()` to read the complete contents of a file:

```python
content = file.read()
```

Also learned how to use `.readlines()` to read the lines of a file:

```python
names = file.readlines()
```

### 4. Using `.strip()`

Used `.strip()` to remove unnecessary whitespace and newline characters from each name:

```python
name = name.strip()
```

This is especially useful when reading data line-by-line from a text file.

### 5. Using `.replace()`

Used `.replace()` to replace the `[name]` placeholder in the letter template:

```python
new_letter = letter.replace("[name]", name)
```

### 6. Creating Multiple Files Dynamically

Learned how to create different filenames using **f-strings**:

```python
with open(f"output/letter_for_{name}.txt", "w") as file:
    file.write(new_letter)
```

This allows the program to generate files such as:

```text
letter_for_Anurag.txt
letter_for_Rahul.txt
letter_for_Aman.txt
```

## 🛠️ Technologies Used

* **Python 3**
* File Handling
* String Manipulation
* `with open()`
* `.read()`
* `.readlines()`
* `.strip()`
* `.replace()`
* f-strings

## 📂 Project Structure

```text
Mail Merge Project/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   │
│   └── Letters/
│       └── starting_letter.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Anurag.txt
│       ├── letter_for_Rahul.txt
│       └── ...
│
└── main.py
```

## 💡 Key Takeaway

The main purpose of this project was to practice **working with files in Python**.

I learned how to read data from files, process the data, modify strings, and generate multiple output files programmatically instead of creating each file manually.

This project gave me practical experience with Python's basic file-handling operations and showed how they can be used to automate repetitive tasks.
