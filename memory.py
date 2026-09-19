"""Memoria, juego de memoria de reconocimiento de patrones."""

from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')

NUM_TILES = 36
GRID_SIZE = 6
TILE_SIZE = 50
OFFSET = 150

tiles = list(range(NUM_TILES // 2)) * 2
state = {'mark': None, 'pairs': 0}
hide = [True] * NUM_TILES

def square(x, y):
    "Dibujar cuadrado blanco con contorno negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(TILE_SIZE)
        left(90)
    end_fill()

def index(x, y):
    "Convertir coordenadas (x, y) a índice de casilla según el grid 6x6."
    return int((x + OFFSET) // TILE_SIZE + ((y + OFFSET) // TILE_SIZE) * GRID_SIZE)

def xy(count):
    "Convertir el índice de casilla a coordenadas (x, y)."
    return (count % GRID_SIZE) * TILE_SIZE - OFFSET, (count // GRID_SIZE) * TILE_SIZE - OFFSET

def tap(x, y):
    "Actualizar casilla seleccionada y casillas ocultas."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] += 1

def draw():
    "Dibujar imagen, casillas y estado del juego."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for spot in range(NUM_TILES):
        if hide[spot]:
            x, y = xy(spot)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 10)
        color('black')
        write(tiles[mark], font=('Arial', 22, 'normal'))

    up()
    goto(-180, 160)
    color('blue')
    write(f"Pares descubiertos: {state['pairs']}/{NUM_TILES // 2}", font=('Arial', 14, 'bold'))

    if state['pairs'] == NUM_TILES // 2:
        goto(-130, 0)
        color('green')
        write("¡Juego Completado!", font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
