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

for i in range(3):
    for j in range(3):
        button = create_button(50 + j * 100, 50 + i * 100, "", lambda x=100 + j * 100, y=100 + i * 100: button_command(x, y))

draw_grid()

MyScreen.mainloop()