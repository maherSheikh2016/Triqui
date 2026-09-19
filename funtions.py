import tkinter as tk
from tkinter import messagebox
MyScreen = tk.Tk()
MyScreen.geometry("400x400")
MyScreen.title("Tic-tac-toe")

frame = tk.Frame(MyScreen, bg="lightgreen")
frame.place(x=0, y=0, width=400, height=400)

canvas = tk.Canvas(frame, width=400, height=400, bg="lightgreen")
canvas.place(x=0, y=0)

def draw_grid():
    coordinates = [((150, 50), (150, 350)), ((250, 50), (250, 350)), ((50, 150), (350, 150)), ((50, 250), (350, 250))]
    for start, end in coordinates:
        canvas.create_line(start[0], start[1], end[0], end[1], width=5, fill="black")

def draw_x(x, y):
    x1 = canvas.create_line(x - 40, y - 40, x + 40, y + 40, width=5, fill="blue")
    x2 = canvas.create_line(x - 40, y + 40, x + 40, y - 40, width=5, fill="blue")
    canvas.tag_raise(x1, x2)

def draw_o(x, y):
    o = canvas.create_oval(x - 40, y - 40, x + 40, y + 40, width=5, outline="orange")
    canvas.tag_raise(o)

def create_button(x, y, text, command):
    button = tk.Button(frame, text=text, command=command, bg="lightgreen")
    button.place(x=x, y=y, width=90, height=90)
    return button

def win_check(board):
    for i in range(3):
        if board[0][i] == "x" and board[1][i] == "x" and board[2][i] == "x":
            messagebox.showinfo("Game Over", "Player X wins!")
            break
    for j in range(3):
            if board[j][0] == "x" and board[j][1] == "x" and board[j][2] == "x":
                messagebox.showinfo("Game Over", "Player X wins!")
                break

    if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
        messagebox.showinfo("Game Over", "Player X wins!")

    for w in range(3):
        if board[0][w] == "o" and board[1][w] == "o" and board[2][w] == "o":
            messagebox.showinfo("Game Over", "Player O wins!")
            break
    for x in range(3):
            if board[x][0] == "o" and board[x][1] == "o" and board[x][2] == "o":
                messagebox.showinfo("Game Over", "Player O wins!")
                break

    if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
        messagebox.showinfo("Game Over", "Player O wins!")