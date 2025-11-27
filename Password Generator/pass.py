import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    return "".join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Length must be a number.")
        return

    pwd = generate_password(length, letters_var.get(), numbers_var.get(), symbols_var.get())
    
    if pwd.startswith("Error"):
        messagebox.showerror("Error", pwd)
    else:
        password_var.set(pwd)

def copy_to_clipboard():
    pwd = password_var.get()
    if not pwd:
        messagebox.showwarning("No Password", "Generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=15)
main_frame.grid(row=0, column=0)

ttk.Label(main_frame, text="PASSWORD GENERATOR", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 10))

ttk.Label(main_frame, text="Password length:").grid(row=1, column=0, sticky="w")
length_var = tk.StringVar(value="12")
ttk.Entry(main_frame, textvariable=length_var, width=10).grid(row=1, column=1, sticky="w", pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(main_frame, text="Include letters", variable=letters_var).grid(row=2, column=0, columnspan=2, sticky="w")
ttk.Checkbutton(main_frame, text="Include numbers", variable=numbers_var).grid(row=3, column=0, columnspan=2, sticky="w")
ttk.Checkbutton(main_frame, text="Include symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2, sticky="w")

ttk.Label(main_frame, text="Generated password:").grid(row=5, column=0, sticky="w", pady=(10, 0))
password_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=password_var, width=35).grid(row=5, column=1, sticky="w", pady=(10, 0))

ttk.Button(main_frame, text="Generate", command=on_generate).grid(row=6, column=0, pady=10, sticky="e")
ttk.Button(main_frame, text="Copy", command=copy_to_clipboard).grid(row=6, column=1, pady=10, sticky="w")

root.mainloop()
