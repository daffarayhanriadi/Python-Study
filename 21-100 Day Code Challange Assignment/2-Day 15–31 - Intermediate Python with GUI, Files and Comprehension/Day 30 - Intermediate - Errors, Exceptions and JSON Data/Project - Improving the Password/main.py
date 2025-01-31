import json
import tkinter as tk
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """
    * If you can do something with if and else very easily, then you should stick to if and else. If you can't do it with if and else very easily, and it's actually an error that's going to be thrown that you don't have any other way of dealing with, then you should be using the try, except, else, finally keywords.

    * The other way to think about it is that an exception is something that is meant to be exceptional. It's something that happens very rarely. Whereas if and else catches things that happen frequently.
    """
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Info", message=f"No details for the {website} exists")
            
        # Alternative Solution
        # try:
        #     email = data[website]["email"]
        #     password = data[website]["password"]
        # except KeyError:
        #     messagebox.showinfo(title="Info", message="No details for the website exists")
        # else:
        #     messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_list = (
        [choice(letters) for _ in range(randint(8, 10))]
        + [choice(numbers) for _ in range(randint(2, 4))]
        + [choice(symbols) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

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
            # with open("data.txt", mode="a") as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")
            
            # Challenge
            """
            Modify the code to handle the FileNotFoundError.
            Create a new data.json file if it doesn't exist.
            If the file already exist, then simply add the new entry.
            """
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading the old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving & Writing the update data to json file
                    json.dump(data, data_file, indent=4)
            finally:
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

# Labels
website_label = tk.Label(text="Website")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
email_entry = tk.Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "daffarayhanriadi@gmail.com")
password_entry = tk.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = tk.Button(
    text="Generate Password", command=generate_password
)
generate_password_button.grid(column=2, row=3, sticky="EW")
add_button = tk.Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# Challenge
# TODO-1: Add a "Search" button next to the website entry field.
# TODO-2: Adjust the layout and the other widgets as needed to get the desired look.
# TODO-3: Create a function called find_password() that gets triggered when the "Search" button is pressed.
# TODO-4: Check if the user's entry matches an item in the data.json.
# TODO-5: If yes, show a messagebox with the website's name and password.
# TODO-6: Catch an exception that might occur trying to access the data.json showing a messagebox with the text: "No Data File Found".
# TODO-7: If the user's website does not exist inside the data.json, show a messagebox that reads "No details for the website exists".

search_button = tk.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
