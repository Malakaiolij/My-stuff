import tkinter as tk
from tkinter import messagebox

def check_bac():
    try:
        bac = float(entry.get())
        if bac >= 0.08:
            result_label.config(text="You are legally intoxicated. Do not drive.", fg="red")
        elif bac > 0:
            result_label.config(text="You're not legally drunk yet. Drink responsibly—and still, no driving.", fg="orange")
        else:
            result_label.config(text="No alcohol detected. You're sober.", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric BAC value.")

# GUI setup
root = tk.Tk()
root.title("Malakai's Drunk Tester")

tk.Label(root, text="Enter your BAC:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Check BAC", command=check_bac, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

tk.Label(root, text="Thanks for running Malakai's Drunk Tester!", font=("Arial", 10)).pack(pady=20)

root.mainloop()
