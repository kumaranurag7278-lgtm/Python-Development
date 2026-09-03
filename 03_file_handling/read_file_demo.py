"""Read a text file from the same folder as this script.

Uses os.path so the path still works no matter which directory you run from.
Commented blocks show create / append / older open-close style.
"""

import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "sample_file.txt")

with open(file_path, "r") as f:
    box = f.read()

print(box)

# --- create a new file (fails if it already exists) ---
# with open("my_file2", "x") as n:
#     n.write("chaar xhawani")

# --- append (old open/close style; always close the file) ---
# f = open("sample_file.txt", "a")
# f.write("chaar chawani ghode pe \n")
# f.close()
