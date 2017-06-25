#!/usr/bin/python

import matrix
from character import *

rows, columns = 23, 40

# Instantiate the Matrix class in main file
game_matrix = matrix.Matrix(rows, columns, default_character=" ")
main_symbol = MainSymbol("#")

game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

while True:

    game_matrix.print_matrix()

    direction = raw_input("Where to next (WASD)?")

    if direction == 'q': break
    elif direction not in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):
        continue

    main_symbol.move(direction)
    game_matrix.update_character_in_matrix(main_symbol.y, main_symbol.x, main_symbol.symbol)
