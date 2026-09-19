import tkinter as tk
from funtions import MyScreen, draw_grid, draw_x, draw_o, create_button
turn = "X"
save = {
    "x1" = None
    "y1" = None
    "x2" = None
    "y2" = None
    "x3" = None
    "y3" = None
    "x4" = None
    "y4" = None
    "x5" = None
}
def button_command(x, y, row, column):
    global turn
    if turn == "X":
        draw_x(x, y)
        for key, value in items(save)  and key == "o" + w:
            if save[key] == None:
                save[key] = (row, column)
                break

        turn = "O"
    else:
        draw_o(x, y)
        for key, value, w in items(save):
            if save[key] == None and key == "o" + w:
                save[key] = (row, column)
                break
        turn = "X"
def Myc(name, row, column, x, y):
    button_command(x, y, row, coulumn)
    name.destroy()
    


for i in range(3):
    for j in range(3):
        button = create_button(50 + j * 105, 50 + i * 105, "", None)
        button.configure(command=lambda button=button, row=i, column=j, x=100 + j * 100, y=100 + i * 100: Myc(button, row, column, x, y))

draw_grid()

MyScreen.mainloop()