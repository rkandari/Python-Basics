import tkinter as tk  ## import the package for GUI
from tkinter import messagebox ## importing a messagebox

root = tk.Tk() # Creating an object of tk
root.title("Calculator") # Give the title
label = tk.Label(root, text="Enter first number", pady=(10)) ## Creating an label for first number
label.pack() ## Pack is used for sequential execution

first_number_entry = tk.Entry(root) ## Enter first no
first_number_entry.pack()

label2 = tk.Label(root, text="Enter second number") ## Creating an label for second number
label2.pack()

second_number_entry = tk.Entry(root) ## Enter second no
second_number_entry.pack()

operations = tk.Label(root, text="Operations") ## Creating an label for operations
operations.pack()

def addition(): ## defining an addition function
    first, second = takeValueInput()
    result = first + second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def subtract(): ## defining an subtraction function
    first, second = takeValueInput()
    result = first - second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def multiply(): ## defining an multiplication function
    first, second = takeValueInput()
    result = first * second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def divide(): ## defining an divison function
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))

def takeValueInput(): ## Input the value of first and second number
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


addition_button = tk.Button(root, text="+",
                            command=lambda : addition()) ## Creating sn addition button
addition_button.pack()

minus_button = tk.Button(root, text="-",
                         command=lambda : subtract()) ## Creating an subtraction button
minus_button.pack()

multiply_button = tk.Button(root, text="*",
                            command=lambda : multiply()) ## Creating sn multiplication button
multiply_button.pack()

division_button = tk.Button(root, text="/",
                            command=lambda : divide()) ## Creating an divison button
division_button.pack()

result_label = tk.Label(root, text="Operations result is:")
result_label.pack()

root.mainloop() ## closing the GUI