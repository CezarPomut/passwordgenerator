from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    list=[]
    global website_entry
    global email_entry
    global password_entry
    a=website_entry.get()
    website_entry.insert(0,"")
    b=email_entry.get()
    c=password_entry.get()
    password_entry.insert(0,"")
    list.append(a)
    list.append(b)
    list.append(c)
    return list



def add_data():
    lista_secundara=get_data()
    parole = open("parole.txt", "a")
    for x in lista_secundara:
        parole.write(f"{x}\n")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas= Canvas(width=200, height=200, bg=YELLOW , highlightthickness=0)
logo_img= PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)

website_entry=Entry(width=45,justify="left")
website_entry.grid(row=1,column=1,padx=10, sticky="W")
website_entry.focus()

email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)

email_entry=Entry(width=45,justify="left")
email_entry.grid(row=2,column=1,padx=10, sticky="W")
email_entry.insert(0, "pomutcezz@gmail.com")

password_label=Label(text="Password")
password_label.grid(row=3,column=0)

password_entry=Entry(width=21, justify="left")
password_entry.grid(row=3,column=1, padx=10, sticky="W")

password_button=Button(text="Generate Password",justify="right", width=14)
password_button.grid(row=3, column=1,padx=10, sticky="e")

add_button=Button(text="Add",width=38,command=add_data)
add_button.grid(row=4, column=1)

website_entry.insert(0,"orice vreau eu")

window.mainloop()

