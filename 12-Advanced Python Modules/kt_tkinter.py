# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa dia!")

# Frame input
frame_input = ttk.Frame(window)

# Penempatan Grid, Pack, Place
frame_input.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()