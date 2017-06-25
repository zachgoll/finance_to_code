#!/usr/bin/python

# tells the symbol where to go on the grid
class Direction():

    SOUTH = "s"
    NORTH = "w"
    WEST = "a"
    EAST = "d"


class MainSymbol():

    def __init__(self, symbol, startX=0, startY=0, velx = 1, vely = 1, trace = '*'):

        self.symbol = symbol

        self.x = startX
        self.y = startY

        self.velx = velx
        self.vely = vely

    def move(self, direction):

        # Y instructions

        if direction == Direction.SOUTH:
            self.y += self.vely
        elif direction == Direction.NORTH:
            self.y -= self.vely

        # X instructions

        elif direction == Direction.WEST:
            self.x -= self.velx
        elif direction == Direction.EAST:
            self.x += self.velx
