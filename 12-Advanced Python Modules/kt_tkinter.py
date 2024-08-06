# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa dia!")

# Variable dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    """Fungsi ini akan dipanggil oleh tombol"""
    # print(NAMA_BELAKANG.get())
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!"
    showinfo(title="Whazzzup", message=pesan)

# Frame input
frame_input = ttk.Frame(window)

# Penempatan -> Grid, Pack, Place
frame_input.pack(padx=10, pady=10, fill="x", expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(frame_input, text="Nama Depan")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(frame_input, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(frame_input, text="Nama Belakang")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(frame_input, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(frame_input, text="Sapa", command=tombol_click)
tombol_sapa.pack(fill="x", expand=True, padx=10, pady=10)

# Main Loop window
window.mainloop()