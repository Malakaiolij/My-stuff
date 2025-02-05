import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        # Get user input
        miles = float(miles_entry.get())
        kilometers = float(kilometers_entry.get())

        # Perform conversions
        miles_to_kilometers = miles * 1.61
        kilometers_to_miles = kilometers / 1.61

        # Display results
        result_label.config(text=f"{miles} miles is {round(miles_to_kilometers, 2)} kilometers\n"
                                 f"{kilometers} kilometers is {round(kilometers_to_miles, 2)} miles")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for miles and kilometers.")

def reset():
    miles_entry.delete(0, tk.END)
    kilometers_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Miles and Kilometers Converter")

# Create and place the input fields
miles_label = tk.Label(root, text="Enter a length in miles:")
miles_label.grid(row=0, column=0, padx=10, pady=10)
miles_entry = tk.Entry(root)
miles_entry.grid(row=0, column=1, padx=10, pady=10)

kilometers_label = tk.Label(root, text="Enter a length in kilometers:")
kilometers_label.grid(row=1, column=0, padx=10, pady=10)
kilometers_entry = tk.Entry(root)
kilometers_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
