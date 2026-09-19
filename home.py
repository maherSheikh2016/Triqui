import tkinter as tk
from funtions import MyScreen, draw_grid, draw_x, draw_o, create_button, win_check
turn = "X"
board =[
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
def button_command(x, y, row, column):
    global turn
    if turn == "X":
        draw_x(x, y)
        for x in range(3):
            for y in range(3):
                if board[x][y] == None and (x, y) == (row, column):
                    board[x][y] = "x"
                    turn = "O"
                    win_check(board)
                    break
    else:
        draw_o(x, y)
        for x in range(3):
                    for y in range(3):
                        if board[x][y] == None and (x, y) == (row, column):
                            board[x][y] = "o"
                            turn = "X"
                            win_check(board)
                            break
def Myc(name, row, column, x, y):
    button_command(x, y, row, column)
    name.destroy()
    


for i in range(3):
    for j in range(3):
        button = create_button(50 + j * 105, 50 + i * 105, "", None)
        button.configure(command=lambda button=button, row=i, column=j, x=100 + j * 100, y=100 + i * 100: Myc(button, row, column, x, y))

draw_grid()

MyScreen.mainloop()