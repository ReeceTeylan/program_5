#Create a Simple App Calculator

# Integrate tkinter to the code
# The application will ask the user to choose one of the four math operations
# The application will ask the user for two numbers
# Display the result
# The application will ask if the user wants to try again or not
# If yes, repeat Step 1
# If no, Display “Thank you!” and the program will exit 
# Use Python Function and appropriate Exceptions to capture errors during runtime
import tkinter as tk
from tkinter import font

def calculate():
    def perform_operation():
        try:
            operation_symbol, operation_func = operations[user_operation.get()]
            first_number = float(first_number_entry.get())
            second_number = float(second_number_entry.get())
            result = operation_func(first_number, second_number)
            result_label.config(text=f"The result is: {result}")

    operations = {
        'Addition': ('+', lambda x, y: x + y),
        'Subtraction': ('-', lambda x, y: x - y),
        'Multiplication': ('*', lambda x, y: x * y),
        'Division': ('/', lambda x, y: x / y)
    }

    window = tk.Tk()
    window.title("Calculator")

    user_operation_frame = tk.Frame(window)
    user_operation_frame.grid(row=0, column=0, padx=10, pady=10)

    user_operation = tk.StringVar(window)
    user_operation.set("Addition")

    for operation in operations:
        tk.Radiobutton(user_operation_frame, text=operation, variable=user_operation, value=operation).pack(side=tk.LEFT, padx=10, pady=10)

    first_number_label = tk.Label(window, text="Enter the first number:", font=font.Font(family="Consolas",size=15), bg="seagreen", fg="white")
    first_number_label.grid(row=1, column=0, padx=10, pady=10)

    first_number_entry = tk.Entry(window, font=font.Font(family="Consolas",size=13), bg="darkseagreen", fg="white")
    first_number_entry.grid(row=2, column=0, padx=10, pady=10)

    second_number_label = tk.Label(window, text="Enter the second number:", font=font.Font(family="Consolas",size=15), bg="seagreen", fg="white")
    second_number_label.grid(row=3, column=0, padx=10, pady=10)

    second_number_entry = tk.Entry(window, font=font.Font(family="Consolas",size=13), bg="darkseagreen", fg="white")
    second_number_entry.grid(row=4, column=0, padx=10, pady=10)

    result_label = tk.Label(window, text="")
    result_label.grid(row=5, column=0, padx=10, pady=10)
