
'''
The static method does not include "self" argument, because
it is not calling the object
'''

class Board(object):

    _game_tiles = []

    def __init__(self, length, width):

        if not Board._game_tiles:
            for _ in xrange(length * width):
                Board._game_tiles.append(Tile())

    # Our static method
    @staticmethod
    def move_together(x_amount, y_amount):

        for tile in Board._game_tiles:
            tile.move(x_amount, y_amount)

    @staticmethod
    def print_locations():
        for tile in Board._game_tiles:
            print tile.x, tile.y

class Tile(object):

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y

# Calling static method

my_board = Board(4,4)
Board.print_locations()
Board.move_together(10,20)
Board.print_locations()

# Calling static method syntax
#       Classname.staticmethod
#       object.method()
