from tkinter import *

# Button
def button_clicked():
    # my_label["text"] = "onichan came inside me"
    new_text = input.get()
    my_label.config(text=new_text)

    print("onichan yamate kudasai")



# create a window :
window = Tk()
window.title("my first GUI program")

# size of the window 
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

# Label :
my_label = Label(text="I am a Label",font=("Arial",24,"italic"))


# we can use - Grid() , pack() or place() to show my_label on window.
my_label.grid(column=0,row=0)
# my_label.pack(side="top")



# change text 
# my_label.config(text="New Text") #another way of changing the text



button = Button(text="Click me daddy",command = button_clicked)
# button.pack()
button.grid(column=1,row=2)


# Entry 
input = Entry(width=15)
# input.pack()
input.grid(column=2,row=3)


window.mainloop()