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

def calculate():
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
