# Triqui

A small Tic-Tac-Toe game made with Python and Tkinter.

## Requirements

- Python 3
- Tkinter, usually included with standard Python installations

## Run the Game

From this folder, run:

```bash
python3 home.py
```

The game opens a 3x3 board. Player X starts, followed by Player O.

## How the Code Works

### 1. The window is created

`funtions.py` creates the Tkinter window, frame, canvas, and drawing functions. The canvas is used for the board grid and for drawing X and O marks.

### 2. The buttons are created

`home.py` uses nested loops to create nine buttons:

- The outer loop selects the row.
- The inner loop selects the column.
- Each button is assigned its row and column through its callback.

The callback also stores the drawing coordinates. This lets the program identify exactly which cell was clicked.

### 3. A player clicks a cell

The button calls `Myc()` with:

- The clicked button
- Its row
- Its column
- Its drawing coordinates

`Myc()` passes this information to `button_command()` and then removes the clicked button from the board.

### 4. The current player's mark is drawn

`button_command()` checks the current turn:

- X calls `draw_x()`.
- O calls `draw_o()`.

The selected position is then stored in the `board` matrix as either `"x"` or `"o"`.

### 5. The winner is checked

After a move, `win_check(board)` checks the board for three matching marks in a row, column, or diagonal.

## Board Coordinates

The board uses zero-based coordinates:

```text
(0, 0) | (0, 1) | (0, 2)
-------+---------+-------
(1, 0) | (1, 1) | (1, 2)
-------+---------+-------
(2, 0) | (2, 1) | (2, 2)
```

For example, the top-left cell is `(0, 0)` and the bottom-right cell is `(2, 2)`.

## Known Issue: One Diagonal Does Not Work

The current `win_check()` function checks only the main diagonal:

```text
(0, 0) -> (1, 1) -> (2, 2)
```

It does **not** check the opposite diagonal:

```text
(0, 2) -> (1, 1) -> (2, 0)
```

Because of this, a player can place three matching marks from the top-right corner to the bottom-left corner without the game announcing a win.

The missing check should compare these three cells for X and O:

```python
board[0][2]
board[1][1]
board[2][0]
```

This is a known limitation and still needs to be added to `win_check()`.

## Other Known Limitations

- The game does not currently stop all future moves after a winner is announced.
- A draw message is not implemented yet.
- The button spacing and drawing-coordinate spacing should be kept consistent when the board layout is changed.

## Project Files

- `home.py` contains the game state, turns, button creation, and move handling.
- `funtions.py` contains the Tkinter window, board drawing, mark drawing, button helper, and winner check.
- `Readme.md` contains this project documentation.
