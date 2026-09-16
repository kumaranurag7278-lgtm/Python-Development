from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def gather_info():
    email_info = email_input.get()
    password_info = passowrd_input.get()
    website_info = website_input.get()
    with open("password.txt",mode='a') as file:
        file.write(f"{website_info} | {email_info} | {password_info} \n")
    email_input.delete(0,END)
    passowrd_input.delete(0,END)
    website_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


# window

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# canvas 
canvas = Canvas(width=200 ,height=200)
locker_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image =locker_image)
canvas.grid(row=0,column=1)

# label 
website = Label(text="Website: ")
website.grid(column=0,row=1)

email = Label(text = "Email/Username: ")
email.grid(column=0,row=2)

password = Label(text = "Password: ")
password.grid(column=0,row=3)


# Input :
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)


email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"kumaranurag.7278@gmail.com")

passowrd_input = Entry(width=22)
passowrd_input.grid(row=3,column=1)


# Buttons

password_button = Button(text="Generate Password")
password_button.grid(column=2,row=3)


add_button = Button(text="Add",width=36,command=gather_info)
add_button.grid(column=1,row=4,columnspan=2)







window.mainloop()