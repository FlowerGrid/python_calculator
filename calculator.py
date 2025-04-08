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

    num1 = IntVar()
    last_press = StringVar()
    operator = StringVar()

    # Display
    num_display = Entry(mainframe, borderwidth=2, relief='solid', justify='right')
    num_display.insert(END, '0')
    num_display.grid(column=0, columnspan=5, row=0)

    # Number buttons
    num_btns = Frame(mainframe)
    clear_btn = Button(num_btns, text='Clear', command=lambda: clear(num_display, num1, operator, last_press))
    clear_btn.grid(column=1, row=3, columnspan=2)
    num_btns.grid(column=0, row=1, padx=3, pady=2)
    numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
    row = 0
    column = 0
    col_span = 1
    for i in range(len(numbers)):
        btn = Button(num_btns, text=numbers[i], relief='raised', command= lambda num=numbers[i]: update_num_display(num, num_display, operator, last_press))
        if column > 2:
            row += 1
            column = 0
        btn.grid(column=column, columnspan=col_span, row=row)
        column += 1

    # Operator buttons
    operators_frame = Frame(mainframe)
    operators_frame.grid(row=1, column=1, sticky='n', padx=3, pady=2)
    operators = ['+', '-', 'x', '/']
    column = 0
    row = 0
    for i in range(len(operators)):
        # operator = operators[i]
        btn = Button(operators_frame, text=operators[i], 
                     command=lambda selected_operator=operators[i]: operator_pressed(
                         num1, selected_operator, operator, num_display, last_press))
        if column > 1:
            row += 1
            column = 0
        btn.grid(column=column, row=row)
        column += 1
    equals_btn = Button(operators_frame, text='=', command=lambda: equals(num1, operator, num_display, last_press))
    equals_btn.grid(column=0, row=2, columnspan=2)

    mainframe.mainloop()


def update_num_display(num, num_display, operator, last_press):
    current = num_display.get()
    if current == '0' or operator.get() or last_press.get() == '=':
        current = ''
    num_display.delete(0, END)
    num_display.insert(END, current + num)
    last_press.set('number')


def clear(num_display, num1, operator, last_press):
    num1.set(0)
    operator.set('')
    num_display.delete(0, END)
    num_display.insert(END, '0')
    last_press.set('clear')


def operator_pressed(num1, selected_operator, operator, num_display, last_press):
    # If there already is a num 1
    if last_press.get() == 'operator':
        operator.set(selected_operator)
    elif operator.get():
        calculate(num1, operator, num_display, last_press)
        operator.set(selected_operator)
    else:
    # If there's no num1
        num1.set(int(num_display.get()))
        operator.set(selected_operator)
        num_display.delete(0, END)
        num_display.insert(END, 0)
    last_press.set('operator')


def equals(num1, operator, num_display, last_press):
    calculate(num1, operator, num_display, last_press)
    last_press.set('=')

def calculate(num1, operator, num_display, last_press):
    # num1 +-x/ num2 = solution
    # update display with solution
    num2 = int(num_display.get())
    if operator.get() == '+':
        solution = num1.get() + num2
    elif operator.get() == '-':
        solution = num1.get() - num2
    elif operator.get() == 'x':
        solution = num1.get() * num2
    elif operator.get() == '/':
        solution = num1.get() / num2

    clear(num_display, num1, operator, last_press)
    num1.set(solution)
    num_display.delete(0, END)
    num_display.insert(END, solution)


if __name__ == '__main__':
    main()