# PROYECTO-FINAL-EQUIPO-6

'Proyecto final - Modificación de videojuego con Freegames'





## Emiliano Gallardo Muñiz - A01712804

**Juego:** Tic Tac Toe

 Proceso 

Antes de modificar nada, descargué la versión original del juego con `python -m freegames copy tictactoe` y analicé su lógica: el archivo usa `turtle` para dibujar la cuadrícula y las jugadas, un diccionario `state` para saber de quién es el turno, y una función `tap` que se dispara al hacer clic en la ventana. La versión original no distinguía visualmente entre X y O, no validaba casillas ocupadas, y no detectaba fin de juego.

Hice cada modificación en su propio commit para mantener buen orden:

1. *Color, grosor y centrado de X/O:** modifiqué `drawx` y `drawo` agregando `color()` y `width(5)`, y ajusté los offsets de dibujo agregando un `pad` en X para que ambos símbolos quedaran centrados dentro de su casilla de 133x133 píxeles.

2. *Validación de casilla ocupada:* agregué una matriz `board` de 3x3 que registra qué jugador ocupó cada posición, junto con una función `index()` que convierte las coordenadas de pixel en índices de fila/columna. La función `tap` ahora revisa `board[row][col]` antes de dibujar, y simplemente ignora el clic si la casilla ya tiene una jugada.

3. *Detección de ganador y empate:* agregué `check_winner()`, que arma las 8 combinaciones ganadoras posibles (3 filas, 3 columnas, 2 diagonales) y revisa si alguna tiene 3 jugadas iguales; y `board_full()`, que detecta si ya no quedan casillas libres. Al detectar cualquiera de los dos casos, `tap` marca `state['over'] = True` para bloquear más jugadas y llama a `show_message()` para mostrar el resultado en pantalla.

*Nota de un problema que tuve* al probar el juego, el mensaje de "Ganó el jugador X" o "Empate" nunca aparecía visualmente, aunque la lógica sí detectaba el resultado correctamente (lo confirmé imprimiendo el estado del tablero en la terminal). El problema era que `show_message` dibujaba el texto en `y = -250`, fuera del área visible de la ventana original de 420x420 píxeles. Lo resolví aumentando el alto de la ventana a 500 píxeles y ajustando la posición del mensaje a `y = -220`.

*Pruebas realizadas:* verifiqué manualmente que el juego bloquea clics sobre casillas ocupadas, que detecta victoria en línea horizontal, vertical y diagonal, y que muestra "Empate" al llenar el tablero sin un ganador.

## Daniel Ayala Domínguez - A00843615

**Juego:** Pacman

**Descripción de los cambios:**
- Modifiqué la estructura del laberinto en la matriz `tiles` cambiando la distribución de caminos y paredes.
- Cambié el color y tamaño del alimento a magenta con un punto de mayor visibilidad dentro del mapa.
- Incrementé la velocidad de los fantasmas ajustando el temporizador del ciclo de movimiento a un intervalo menor.

  ## Elias Ian Lopez Calvario - A01712804
  **Juego:** Memoria
  **Descripción de los cambios:**

  """
Juego de Memoria - Modificaciones realizadas:
1. Contador de pares descubiertos.
2. Detección y mensaje de victoria al destapar todas las casillas.
3. Ajuste de casillas a tablero de 6x6 y terminar de traducir a espaniol.
"""
  
