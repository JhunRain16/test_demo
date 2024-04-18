import tkinter as tk

# Function to update the display
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the display
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Function to negate the expression
def negate():
    global expression
    if expression and expression[0] == '-':
        expression = expression[1:]
    else:
        expression = '-' + expression
    input_text.set(expression)

# Creating a GUI window
window = tk.Tk()
window.title("Jhun Ultra Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Variable to hold the user input expression
expression = ""

# Variable to hold the expression displayed on the screen
input_text = tk.StringVar()

# Entry widget to display the expression
entry = tk.Entry(window, textvariable=input_text, font=('Arial', 14), bd=10, insertwidth=4, width=20, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0','±', '.', '+', '(', ')',   # added negate button
]

row_num = 1
col_num = 0

for button in buttons:
    if button == '±':
        tk.Button(window, text=button, font=('Arial', 17), width=5, height=2, command=negate).grid(row=row_num, column=col_num)
    else:
        tk.Button(window, text=button, font=('Arial', 17), width=5, height=2, command=lambda item=button: button_click(item)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Button to clear the expression
tk.Button(window, text="C", font=('Arial', 17), width=5, height=2, command=clear).grid(row=5, column=1, columnspan=3)

# Button to evaluate the expression
tk.Button(window, text="=", font=('Arial', 17), width=5, height=2, command=calculate).grid(row=5, column=3)

window.mainloop()
