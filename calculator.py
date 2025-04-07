from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.geometry('325x225')
    root.attributes('-topmost', True)

    mainframe = Frame(root, padx=5, pady=5)
    mainframe.pack()

    num1 = IntVar()
    num2 = IntVar()
    operator = StringVar()

    # Display
    num_display = Entry(mainframe, borderwidth=2, relief='solid', justify='right')
    num_display.insert(END, '0')
    num_display.grid(column=0, columnspan=5, row=0)

    # Number buttons
    num_btns = Frame(mainframe)
    clear_btn = Button(num_btns, text='Clear', command=lambda: clear(num_display, num1, num2, operator))
    clear_btn.grid(column=1, row=3, columnspan=2)
    num_btns.grid(column=0, row=1, padx=3, pady=2)
    numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
    row = 0
    column = 0
    col_span = 1
    for i in range(len(numbers)):
        btn = Button(num_btns, text=numbers[i], command= lambda num=numbers[i]: update_num_display(num, num_display))
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
                         num1, num2, selected_operator, operator, num_display))
        if column > 1:
            row += 1
            column = 0
        btn.grid(column=column, row=row)
        column += 1
    equals_btn = Button(operators_frame, text='=', command=lambda: operate(num1, num2, operator, num_display))
    equals_btn.grid(column=0, row=2, columnspan=2)
    print(operator.get())
    print(num1.get())

    mainframe.mainloop()


def update_num_display(num, num_display):
    current = num_display.get()
    if current == '0':
        current = ''
    num_display.delete(0, END)
    num_display.insert(END, current + num)


def clear(num_display, num1, num2, operator):
    num1.set(0)
    num2.set(0)
    operator.set('')
    num_display.delete(0, END)
    num_display.insert(END, '0')


def operator_pressed(num1, num2, selected_operator, operator, num_display):
    # If there already is a num 1
    if operator.get():
        num1.set(operate(num1, num2, operator, num_display))
        operator.set(selected_operator)
    else:
    # If there's no num1
        num1.set(int(num_display.get()))
        operator.set(selected_operator)
        num_display.delete(0, END)
        num_display.insert(END, 0)


def operate(num1, num2, operator, num_display):
    # num1 +-x/ num2 = solution
    # update display with solution
    num2.set(num_display.get())
    print(operator.get())
    if operator.get() == '+':
        solution = num1.get() + num2.get()
    elif operator.get() == '-':
        solution = num1.get() - num2.get()
    elif operator.get == 'x':
        solution = num1.get() * num2.get()
    elif operator.get() == '/':
        solution = num1.get() / num2.get()

    clear(num_display, num1, num2, operator)
    num1.set(solution)
    num_display.delete(0, END)
    num_display.insert(END, solution)


if __name__ == '__main__':
    main()