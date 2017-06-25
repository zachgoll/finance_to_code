from abc import ABCMeta, abstractmethod

'''
The hierarchy in this script

object
    Shape
        Rectangle
            Square
'''

# The interface (cannot be called, but can be used as a super class)
class Shape(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

# Code below does not work because you are trying to call an interface!
#s = Shape()
#print s.area()


class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # this does not call Shape's __init__ method.  It calls Python's builtin "object"
        super(Rectangle, self).__init__()

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 +self.height * 2

class Square(Rectangle):

    def __init__(self, side_length):
        self.side_length = side_length
        # takes the __init__ of Rectangle, but passes in side_length as both width and height
        super(Square, self).__init__(side_length, side_length)

    # We can still override class methods
    def perimeter(self):
        print "Using the square's specific perimeter calculation method"
        return self.side_length * 4

# What's going on here???  Basically, the super class "Shape" with its abstract
# methods ensures that Rectangle(Shape) class has both the area() and perimeter()
# methods written out.  This is useful because without those two methods, you don't
# really have a shape..
rect = Rectangle(5, 6)
print rect.area()
print rect.perimeter()

# Even though Square class doesn't explicitly define the area() method, we know
# that it has an area because Rectangle has it as required by the super class
sq = Square(5)
print sq.area()
print sq.perimeter()
