from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = web_input.get()
    user_data = email_input.get()
    pass_data = pass_input.get()
    if len(web_data) > 0 and len(user_data) > 0 and len(pass_data) > 0:
        is_ok = messagebox.askokcancel(title=web_data,
                                       message=f"These are the details entered: \nEmail: {user_data}\nPassword: {pass_data}\nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f"{web_data} | {user_data} | {pass_data}\n")
                web_input.delete(0, 'end')
                pass_input.delete(0, 'end')
    else:
        messagebox.showinfo(title='Oops', message='Please don`t leave any fields empty!')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text='Website:')
website.grid(column=0, row=1)
email = Label(text='Email/Username:')
email.grid(column=0, row=2)
password = Label(text='Password:')
password.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'asd@gmail.com')
pass_input = Entry(width=17)
pass_input.grid(column=1, row=3)

gen_pass = Button(text='Generate Password', command=generate_password)
gen_pass.grid(column=2, row=3)
button = Button(text='Add', width=30, command=save)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
