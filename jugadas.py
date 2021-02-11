from funciones_adicionales import *

def step(tablero, posx1, posy1, posx2, posy2, turno):
    tablero[transform_pos(posx1)][posy1-1] = 'o'
    tablero[transform_pos(posx2)][posy2-1] = 'y'

tablero = create_board()
print_board(tablero)

step(tablero, 'h', 8, 'g', 7, 0)
print_board(tablero)