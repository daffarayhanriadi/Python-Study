import tkinter as tk


def calculate():
    new_label = int(entry.get()) * 1.6
    label2.config(text=new_label)


window = tk.Tk()
window.title("Miles to Kilometer Converter")
# window.minize()
window.config(padx=20, pady=20)

# Label
label1 = tk.Label(text="is equal to")
label2 = tk.Label(text=0)
label3 = tk.Label(text="Miles")
label4 = tk.Label(text="Km")

# Entry
entry = tk.Entry(width=10)

# Button
button = tk.Button(text="Calculate", command=calculate)

# Position
label1.grid(column=0, row=1)
label2.grid(column=1, row=1)
label3.grid(column=2, row=0)
label4.grid(column=2, row=1)
entry.grid(column=1, row=0)
button.grid(column=1, row=2)


window.mainloop()
