import tkinter as tk

#* Creating a new window and configurations
window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#* Labels Widget
label = tk.Label(text="I Am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
label.pack()

# We can set options (widget/properties that we have created)
label["text"] = "New Text"
label.config(text="New Text")

#* Buttons Widget
# Challenge-2
"""
Show "Button Got Clicked" on my_label when the button get's clicked.
"""
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked") # Solution Challenge-2
    print(type(entry.get()))
    label.config(text=entry.get())  # Solution Challenge-3


# calls button_clicked() when pressed
button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Challenge-3
"""
Figure out how to get whatever is written in Entry to be the text in 
the Label. The moment is when we click on the Button. 
"""

#* Entries Widget
entry = tk.Entry(width=30)
# Add some text to begin with
entry.insert(tk.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()


#* Text Widget
text = tk.Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(tk.END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.pack()


#* Spinbox Widget
def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#* Scale Widget
def scale_used(value):
    print(value)
    

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()


#* Check Button Widget
def checkbutton_used():
    # Prints 1 if ON button checked, otherwise 0
    print(checked_state.get())
    

# Variable to hold on to checked state, 0 is off, 1 is on
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#* Radio Button Widget
def radio_used():
    print(radio_state.get())
    
    
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#* List Box Widget
def listbox_used(event): # The event parameter is used
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    
# Create Listbox and populate it with fruits
listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
    # listbox.insert(tk.END, item)  # Insert at the end (Alternative)
# Bind ListboxSelect event to function
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
