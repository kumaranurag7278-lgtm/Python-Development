from tkinter import *

# create a window :
window = Tk()
window.title("my first GUI program")

# size of the window 
window.minsize(width=500,height=300)

# Label :
my_label = Label(text="I am a Label",font=("Arial",24,"italic"))
my_label.pack(side="top")


# change text 
# my_label.config(text="New Text") #another way of changing the text


# Button
def button_clicked():
    # my_label["text"] = "onichan came inside me"
    new_text = input.get()
    my_label.config(text=new_text)

    print("onichan yamate kudasai")

button = Button(text="Click me daddy",command = button_clicked)
button.pack()

# Entry 
input = Entry(width=15)
input.pack()

window.mainloop()