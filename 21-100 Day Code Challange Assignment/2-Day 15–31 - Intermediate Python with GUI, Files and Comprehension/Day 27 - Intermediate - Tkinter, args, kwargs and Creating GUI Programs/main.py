import tkinter as tk

def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)

# Creating a new window and configurations
window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Labels (Component)
my_label = tk.Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons (Component)
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Challenge-4
"""Add a new button, its position must be to the right of the previous
button and aligned with the component label"""
# New Buttons
new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entries (Component)
entry = tk.Entry(width=10)
print(entry.get())
entry.grid(column=3, row=2)


window.mainloop()
