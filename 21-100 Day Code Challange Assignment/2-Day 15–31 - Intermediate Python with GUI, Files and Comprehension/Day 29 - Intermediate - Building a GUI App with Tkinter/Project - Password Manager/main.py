import tkinter as tk
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    # nr_letters = random.randint(8, 10)
    # nr_numbers = random.randint(2, 4)
    # nr_symbols = random.randint(2, 4)

    # Challenge
    """
    Change the existing for loops to use Python List Comprehension instead (see Day 26).
    Remember to combine the results so that you can shuffle them to create a password. 
    """
    password_list = (
        [choice(letters) for _ in range(randint(8, 10))]
        + [choice(numbers) for _ in range(randint(2, 4))]
        + [choice(symbols) for _ in range(randint(2, 4))]
    )

    # ## Alternative Solution-1
    # password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # password_list = password_letters + password_numbers + password_symbols

    ## Alternative Solution-2
    # random_letters = [random.choice(letters) for _ in range(nr_letters)]
    # random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # random_password = [random_letters, random_numbers, random_symbols]
    # password_list = [char for sublist in random_password for char in sublist]

    # for _ in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for _ in range(nr_numbers):
    #     password_list.append(random.choice(numbers))

    # for _ in range(nr_symbols):
    #     password_list.append(random.choice(symbols))

    shuffle(password_list)

    password = "".join(password_list)

    ## Alternative Solution
    # password = ""
    # for char in password_list:
    #     password_list += char

    # print(f"Your password is: {password}")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Challenge
"""
1. Create a function called save()
2. Write to the data inside the entries to a data.txt file when the Add button is clicked.
3. Each website, email, and password combination should be on a new line inside the file.
4. All fields need to be cleared after Add button is pressed.
"""


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Challenge
    """
    Do not save the data and show the pop up above if the website or 
    password fields were left empty
    """
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        # Add pop-up
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}"
            f"\nPassword: {password}\nIs it ok to save?",
        )

        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# canvas.grid(padx=20, pady=20) # Alternative to Set The Padding

# Labels
website_label = tk.Label(text="Website")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
# website_entry = tk.Entry(width=35)
# website_entry.grid(column=1, row=1, columnspan=2)
# email_entry = tk.Entry(width=35)
# email_entry.grid(column=1, row=2, columnspan=2)
# password_entry = tk.Entry(width=21)
# password_entry.grid(column=1, row=3)
website_entry = tk.Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = tk.Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "daffarayhanriadi@gmail.com")
password_entry = tk.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
# generate_password_button = tk.Button(text="Generate Password")
# generate_password_button.grid(column=2, row=3)
# add_button = tk.Button(text="Add", width=36)
# add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = tk.Button(
    text="Generate Password", command=generate_password
)
generate_password_button.grid(column=2, row=3, sticky="EW")
add_button = tk.Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
