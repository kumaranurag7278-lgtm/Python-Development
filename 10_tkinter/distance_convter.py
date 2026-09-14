from tkinter import *


# Button click
def button_click():
    mile = float(input_box.get())
    kilometer = mile * 1.6
    my_label.config(text=kilometer)


window = Tk()
window.title("Mile to Kilometer Converter")

window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# my label 
my_label = Label(text="0")
my_label.grid(column=1,row=1)


# another label
is_equal = Label(text="Is equal to ")
is_equal.grid(column=0,row=1)

Km = Label(text="KM")
Km.grid(column=2,row=1)


# Button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


# Input
input_box = Entry(width=15)
input_box.grid(column=1, row=0)

 
window.mainloop()

