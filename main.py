import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# window initialisation
window = tk.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# password image
canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
web_label = tk.Label(text='Website:', justify='right')
web_label.grid(row=1, column=0, sticky='E')

username_label = tk.Label(text='Email/Username:', justify='right')
username_label.grid(row=2, column=0, sticky='E')

password_label = tk.Label(text='Password:', justify='right')
password_label.grid(row=3, column=0, sticky='E')

# entries
web_entry = tk.Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky='W')

username_entry = tk.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2,sticky='W')

password_entry = tk.Entry(width=26)
password_entry.grid(row=3, column=1, columnspan=1, sticky='W')

# buttons
generate_password_button = tk.Button(text='Generate Password', width=14)
generate_password_button.grid(row=3, column=2, sticky='W')

add_button = tk.Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')
# mainloop
window.mainloop()

