import tkinter as tk
from math import *


root = tk.Tk() #intialize tkinter
root.title("Calculator") #title for the window
root.geometry("300x500") #size for the window


result_var= tk.StringVar() #stores the result after compilation
result_entry = tk.Entry(root, textvariable=result_var, font=("Italic", 20),fg = 'white', bg = 'white', justify=tk.RIGHT) #for the input expression
result_entry.grid(row=0, column=0, columnspan=4) #grid for the calculator
buttons = [
    ('log', 1, 0), ('log2', 1, 1), ('**', 1, 2),('C', 1, 3),
    ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('⌫', 2, 3),
    ('1/x', 3, 0), ('x!', 3, 1), ('x^3', 3, 2), ('|x|', 3, 3),
    ('(', 4, 0), (')', 4, 1), ('%', 4, 2), ('/', 4, 3),                #buttons are being alloted as per the grid (text,row,column)
    ('√', 5, 0), ('³√', 5, 1), ('e', 5, 2), ('pi', 5, 3),
    ('7', 6, 0), ('8', 6, 1), ('9', 6, 2), ('*', 6, 3),
    ('4', 7, 0), ('5', 7, 1), ('6', 7, 2), ('-', 7, 3),
    ('1', 8, 0), ('2', 8, 1), ('3', 8, 2), ('+', 8, 3),
    ('+/-', 9, 0), ('0', 9, 1), ('.', 9, 2), ('=', 9, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, font=("Italic", 5, 'bold'),fg = 'white', bg = 'black' , command= lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

def calculate(expression):
    try:
        result = str(eval(expression))
        return result
    except (ZeroDivisionError, Exception) as e:
        return f"Error: {e}"

def trigo(function, value):
    try:
        angle = radians(float(value))
        if function == "sin":
            calculated_value = sin(angle)
            return calculated_value
        elif function == "cos":
            calculated_value = cos(angle)
            return calculated_value
        elif function == "tan":
            calculated_value = tan(angle)
            return calculated_value
    except Exception as e:
        return f"Error: {e}"
def inverse(value):
    try:
        result = str(1/eval(value))
        return result
    except Exception as e:
        return f"Error: {e}"

def pow3(function, value):
    try:
        result = pow(eval(value), 3)
        return result
    except Exception as e:
        return f"Error: {e}"
def on_button_click(button_text):
    if button_text == "=":
        result = calculate(result_var.get())
        result_var.set(result)
    elif button_text == "C":
        result_var.set("")
    elif button_text == "⌫":
        result_var.set(result_var.get()[0:len(result_var.get()) - 1])
    elif button_text == "+/-":
        current_text = result_var.get()
        if current_text and current_text[0] == "-":
            result_var.set(current_text[1:])
        else:
            result_var.set("-" + current_text)

    elif button_text == "|x|":
        current_text = result_var.get()
        if current_text and current_text[0] == "-":
            result_var.set(current_text[1:])
    
    elif button_text == "x^3":
        result = pow3(button_text, result_var.get())
        result_var.set(result)

    elif button_text == "x!":
        current_text = result_var.get()
        result_var.set(factorial(int(result_var.get())))

    elif button_text == "³√":
        current_value = float(result_var.get())
        cube_root_value = pow(current_value, 1/3)
        result_var.set(str(cube_root_value))
    
    elif button_text == "√":
        current_value = float(result_var.get())
        cube_root_value = pow(current_value, 1/2)
        result_var.set(str(cube_root_value))

    elif button_text == "sin":
        result = trigo(button_text, result_var.get())
        result_var.set(result)
    elif button_text == "cos":
        result = trigo(button_text, result_var.get())
        result_var.set(result)
    elif button_text == "tan":
        result = trigo(button_text, result_var.get())
        result_var.set(result)
    elif button_text == "1/x":
        result = inverse(result_var.get())
        result_var.set(result)
    else:
        current_text = result_var.get()
        new_text = current_text + button_text
        result_var.set(new_text)

root.mainloop()
