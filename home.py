import tkinter as tk
from funtions import MyScreen, draw_grid, draw_x, draw_o, create_button
turn = "X"
def button_command(x, y):
    global turn
    if turn == "X":
        draw_x(x, y)
        turn = "O"
    else:
        draw_o(x, y)
        turn = "X"
def Myc(name, row, column, x, y):
    button_command(x, y)
    name.destroy()

for i in range(3):
    for j in range(3):
        button = create_button(50 + j * 105, 50 + i * 105, "", None)
        button.configure(command=lambda button=button, row=i, column=j, x=100 + j * 100, y=100 + i * 100: Myc(button, row, column, x, y))

draw_grid()

MyScreen.mainloop()