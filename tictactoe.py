"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(5)
    pad = 15
    line(x + pad, y + pad, x + 133 - pad, y + 133 - pad)
    line(x + pad, y + 133 - pad, x + 133 - pad, y + pad)


def drawo(x, y):
    """Draw O player."""
    color('red')
    width(5)
    up()
    goto(x + 67, y + 5)
    down()
    circle(52)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

def index(value):
    """Convert grid coordinate to row/column index (0, 1, or 2)."""
    return int((value + 200) // 133)


board = [[None] * 3 for _ in range(3)]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    col = index(x)
    row = index(y)

    if board[row][col] is not None:
        return  # casilla ya ocupada, ignora el tap

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[row][col] = player
    update()
    state['player'] = not player
