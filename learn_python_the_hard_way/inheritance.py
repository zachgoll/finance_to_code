#object
#   Car

# When you provide "object" as an argument to a class, you create a superclass
# Superclass Car (things can be take from this class and applied to sub-classes)
class Car(object):

    def __init__(self, car_type, color):

        self.car_type = car_type
        self.color = color

    def drive(self):
        print "Driving my %s %s" % (self.color, self.car_type)

    def park(self):
        print "Parked car"

# Sub-class of Car (see how we passed "Car" in as an argument to the class?)

class Honda(Car):

    def __init__(self, color):

        super(Honda, self).__init__("Honda", color)
        # self.car_type = car_type    // we don't need these now
        # self.color = color

        # Another way to do it
        # Car.__init__(self, "Honda", color)

myhonda = Honda("Green")
myhonda.drive()

mycar = Car("Toyota", "Yellow")

mycar.drive()
mycar.park()
