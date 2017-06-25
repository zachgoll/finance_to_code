#!/usr/bin/python
class Matrix():

    def __init__(self, rows, columns, default_character = " "):

        self.rows = rows
        self.columns = columns

        self.grid = [[default_character]*columns for _ in xrange(rows)]

    def print_matrix(self):

        for row in self.grid:
            print "".join(row)

    def update_character_in_matrix(self, row_number, column_number, new_character):

        # Make sure character is inside the grid
        if 0 <= row_number < self.rows:
            if 0 <= column_number < self.columns:
                self.grid[column_number][row_number] = new_character
                return
        raise IndexError("Index error.  Indexes outside grid")
