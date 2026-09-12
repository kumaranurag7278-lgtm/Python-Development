import tkinter

# create a window :
window = tkinter.Tk()
window.title("my first GUI program")

# size of the window 
window.minsize(width=500,height=300)

# Label :
my_label = tkinter.Label(text="I am a Label",font=("Arial",24,"italic"))
my_label.pack(side="top")


window.mainloop()