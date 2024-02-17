import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Sudoku
from Sudoku import my_game
from Sudoku import my_list
from Sudoku import my_list_column
from Sudoku import new_game
from tkinter.ttk import Entry, Style

# creating window and styles
Sudoku.new_game(my_list, my_list_column, my_game)
window = tk.Tk()
style = ttk.Style(window)
window.title("Sudoku")
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
style_cell = Style()
# create a style with a red background
style_cell.configure("Red.TEntry", fieldbackground="red")


frame = ttk.Frame(window)
frame.pack()


def hint():
    y = 0
    for i in range(9):
        for j in range(9):
            # Get the value of the cell from the list
            value = my_game[i][j]
            # Set the StringVar object to the value
            text_vars[i][j].set(value)
            if y == 0 and value == 0:
                value = my_list[i][j]
                my_game[i][j] = value
                # Set the StringVar object to the value
                text_vars[i][j].set(value)
                y += 1
                # Create an Entry widget with the textvariable option
                entry = ttk.Entry(numbers_frame, width=1,
                                  textvariable=text_vars[i][j], font=("Arial", 16, "bold"))
                entry.grid(row=i, column=j, padx=3, pady=3)


def get_numbers():
    # Create an empty list
    numbers = [[], [], [], [], [], [], [], [], []]
    # Loop over the rows and columns of the board
    for i in range(9):
        for j in range(9):
            # Get the value of the Entry widget
            value = text_vars[i][j].get()
            # Append it to the list
            numbers[i].append(int(value))
    if numbers == my_list:
        tkinter.messagebox.showinfo(title="You Won", message="You Won")
    else:
        tkinter.messagebox.showinfo(title="You Lose", message="You Lose")


text_vars = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
numbers_frame = ttk.LabelFrame(frame, text="Sudoku numbers")
numbers_frame.grid(row=0, column=0, padx=20, pady=20)


def destroy():
    children = numbers_frame.winfo_children()
    for child in children:
        child.destroy()


def new():
    destroy()
    global my_list
    global my_list_column
    global my_game
    my_list = [[], [], [], [], [], [], [], [], []]
    my_list_column = [[], [], [], [], [], [], [], [], []]
    my_game = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    my_list = new_game(my_list, my_list_column, my_game)
    for i in range(9):
        for j in range(9):
            # Get the value of the cell from the list
            value = my_game[i][j]
            # Set the StringVar object to the value
            text_vars[i][j].set(value)
            if value == 0:
                entry = ttk.Entry(numbers_frame, width=1, textvariable=text_vars[i][j],
                                  font=("Arial", 16, "bold"))
            else:
                entry = ttk.Entry(numbers_frame, width=1,
                                  textvariable=text_vars[i][j])
            # Place the Entry widget in the grid
            entry.grid(row=i, column=j, padx=3, pady=3)


new()

button_label = ttk.LabelFrame(frame, text="Buttons")
button_label.grid(row=0, column=1, padx=20, pady=20, sticky="n")
button_end = ttk.Button(button_label, text="End", command=get_numbers)
button_end.grid(row=0, column=0, padx=7, pady=7)
button_hint = ttk.Button(button_label, text="hint", command=hint)
button_hint.grid(row=2, column=0, padx=7, pady=7)
button_new = ttk.Button(button_label, text="New", command=new)
button_new.grid(row=3, column=0, padx=7, pady=7)


window.mainloop()

