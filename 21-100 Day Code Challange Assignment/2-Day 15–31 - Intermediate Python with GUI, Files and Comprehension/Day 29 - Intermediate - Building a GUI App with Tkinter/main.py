import tkinter as tk

window = tk.Tk()

r = tk.Label(bg="red", width=20, height=5)
r.grid(column=0, row=0)

g = tk.Label(bg="green", width=20, height=5)
g.grid(column=1, row=1)

b = tk.Label(bg="blue", width=40, height=5)
b.grid(column=0, row=2, columnspan=2) # Columnspan

window.mainloop()
