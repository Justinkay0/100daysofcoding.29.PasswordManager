import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    entry_state = False
    if len(username_entry.get()) < 1 or len(web_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showerror(title='Error in input', message='Please do not leave any fields blank!')
    else:
        entry_state = messagebox.askokcancel(title=f'{web_entry.get()}', message=f"These are the details entered \n"
                                                                             f"Email: {username_entry.get()}\n"
                                                                             f"Password: {password_entry.get()}\n"
                                                                             f"Is it ok to save?")
    if entry_state:
        with open(file='data.txt', mode='a') as f:
            f.write(f"{web_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
            web_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# window initialisation
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# password image
canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
web_label = tk.Label(text='Website:')
web_label.grid(row=1, column=0)

username_label = tk.Label(text='Email/Username:')
username_label.grid(row=2, column=0)

password_label = tk.Label(text='Password:')
password_label.grid(row=3, column=0)

# entries
web_entry = tk.Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
# Place cursor here
web_entry.focus()

username_entry = tk.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'CEO@freedom.com')

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# buttons
generate_password_button = tk.Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text='Add', width=36, command=add_pw)
add_button.grid(row=4, column=1, columnspan=2)
# mainloop
window.mainloop()
