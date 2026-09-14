from tkinter import *


# Button function
def button_clicked():
    new_text = input_box.get()
    my_label.config(text=new_text)


# Create a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(
    text="I am a Label",
    font=("Arial", 24, "italic")
)
my_label.grid(column=0, row=0)


# Button
button = Button(
    text="Click me",
    command=button_clicked
)
button.grid(column=1, row=2)


# Entry
input_box = Entry(width=15)
input_box.grid(column=2, row=3)


# Keep the window running
window.mainloop()
