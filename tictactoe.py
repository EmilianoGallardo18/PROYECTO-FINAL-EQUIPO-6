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


state = {'player': 0, 'over': False}
players = [drawx, drawo]

def index(value):
    """Convert grid coordinate to row/column index (0, 1, or 2)."""
    return int((value + 200) // 133)


board = [[None] * 3 for _ in range(3)]

def check_winner():
    """Return the winning player (0 or 1) or None if there is no winner yet."""
    lines = []
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])
        lines.append([board[0][i], board[1][i], board[2][i]])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for combo in lines:
        if combo[0] is not None and combo[0] == combo[1] == combo[2]:
            return combo[0]
    return None


def board_full():
    """Return True if all squares have been played."""
    return all(cell is not None for row in board for cell in row)


def show_message(text):
    """Display a message in the center of the board."""
    up()
    goto(0, -220)
    color('black')
    write(text, align='center', font=('Arial', 20, 'normal'))


def tap(x, y):
    """Draw X or O in tapped square."""
    if state['over']:
        return

    x = floor(x)
    y = floor(y)
    col = index(x)
    row = index(y)

    if board[row][col] is not None:
        return  

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[row][col] = player

    update()    


    winner = check_winner()
    if winner is not None:
        state['over'] = True
        show_message(f'Gano el jugador {"X" if winner == 0 else "O"}')
        update()
        return

    if board_full():
        state['over'] = True
        show_message('Empate')
        update()
        return

    state['player'] = not player

setup(420, 500, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
