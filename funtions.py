import tkinter as tk

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
    canvas.create_line(x - 40, y - 40, x + 40, y + 40, width=5, fill="blue")
    canvas.create_line(x - 40, y + 40, x + 40, y - 40, width=5, fill="blue")

def draw_o(x, y):
    canvas.create_oval(x - 40, y - 40, x + 40, y + 40, width=5, outline="orange")

def create_button(x, y, text, command):
    button = tk.Button(frame, text=text, command=command)
    button.place(x=x, y=y, width=100, height=100)
    return button