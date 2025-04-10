"""
TODO:
1. support decimals
   - add a decimal button
2. add more math functions
   - square
   - square root
3. enhance clear button
   - make 1 press clear the display and a second clear all memory
4. style
5. explore class idea offered by chat gpt
"""


from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.geometry('325x225')
    # root.attributes('-topmost', True)
    root.lift()
    root.focus_force()

    mainframe = Frame(root, padx=5, pady=5)
    mainframe.pack()

    num1_var = DoubleVar()
    last_press = StringVar()
    operator_var = StringVar()

    # Display
    num_display = Entry(mainframe, borderwidth=2, relief='solid', justify='right')
    num_display.insert(END, '0')
    num_display.grid(column=0, columnspan=5, row=0)

    # Number buttons
    num_btns = Frame(mainframe)
    num_btns.grid(column=0, row=1, padx=3, pady=2)
    numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
    row = 0
    column = 0
    col_span = 1
    for i in range(len(numbers)):
        btn = Button(num_btns, text=numbers[i], relief='raised', command= lambda num=numbers[i]: update_num_display(num, num_display, operator_var, last_press))
        if numbers[i] == '0':
            column = 0
            row = 3
            col_span = 2
        if column > 2:
            row += 1
            column = 0
        btn.grid(column=column, columnspan=col_span, row=row)
        column += 1
    decimal_button = Button(num_btns, text=".", command=lambda: update_num_display('.', num_display, operator_var, last_press))
    decimal_button.grid(column=2, row=3)

    # Operator buttons
    operators_frame = Frame(mainframe)
    operators_frame.grid(row=1, column=1, sticky='n', padx=3, pady=2)
    operators = ['+', '-', 'x', '/']
    column = 0
    row = 1
    for i in range(len(operators)):
        # operator = operators[i]
        btn = Button(operators_frame, text=operators[i], 
                     command=lambda selected_operator=operators[i]: operator_pressed(
                         num1_var, selected_operator, operator_var, num_display, last_press))
        if column > 1:
            row += 1
            column = 0
        btn.grid(column=column, row=row)
        column += 1
    equals_btn = Button(operators_frame, text='=', command=lambda: equals(num1_var, operator_var, num_display, last_press))
    equals_btn.grid(column=0, row=3, columnspan=2)

    clear_btn = Button(operators_frame, text='Clear', command=lambda: clear(num_display, num1_var, operator_var, last_press))
    clear_btn.grid(column=0, row=0, columnspan=2)

    mainframe.mainloop()


def update_num_display(num, num_display, operator, last_press):
    # current = num_display.get()
    # if current == '0' or operator.get() or last_press.get() == '=':
    #     current = ''
    # if num == '.':
    #     if current == '':
    #         current = '0'
    # num_display.delete(0, END)
    # num_display.insert(END, current + num)
    # last_press.set('number')
    # print(last_press.get())

    current = num_display.get()
    if current == '0' or last_press.get() == 'operator' or last_press.get() == '=':
        num_display.delete(0, END)
    if num == '.' and current == '0':
        num_display.insert(END, 0)

    
    num_display.insert(END, num)
    last_press.set('number')
    print(last_press.get())


def clear(num_display, num1_var, operator_var, last_press):
    num1_var.set(0)
    operator_var.set('')
    num_display.delete(0, END)
    num_display.insert(END, '0')
    last_press.set('clear')


def operator_pressed(num1_var, selected_operator, operator_var, num_display, last_press):
    # If there already is a num 1
    if last_press.get() == 'operator':
        operator_var.set(selected_operator)
    elif operator_var.get():
        operate(num1_var, operator_var, num_display, last_press)
        operator_var.set(selected_operator)
    else:
    # If there's no num1
        num1_var.set(float(num_display.get()))
        operator_var.set(selected_operator)
        num_display.delete(0, END)
        num_display.insert(END, 0)
    last_press.set('operator')


def equals(num1_var, operator_var, num_display, last_press):
    if last_press.get() == '=' or last_press.get() == '':
        last_press.set('=')
    else:
        operate(num1_var, operator_var, num_display, last_press)
        last_press.set('=')


def operate(num1_var, operator_var, num_display, last_press):
    num1 = num1_var.get()
    num2 = float(num_display.get())
    operator = operator_var.get()
    solution = calculate(num1, num2, operator)
    if solution % 1 == 0:
        solution = int(solution)

    clear(num_display, num1_var, operator_var, last_press)
    num1_var.set(solution)
    num_display.delete(0, END)
    num_display.insert(END, solution)


def calculate(num1, num2, operator):
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    elif operator == 'x':
        solution = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'Error'
        else:
            solution = num1 / num2
    print(solution)
    return solution


if __name__ == '__main__':
    main()