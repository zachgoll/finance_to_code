'''
An example program that demonstrates the different levels of inheritance.
From https://learnpythonthehardway.org/book/ex44.html

The three types are:

* Implicit inheritance - you can see that even though the function implicit()
  is not defined in the child class, you can still call son.implicit() and
  return the same value that the parent class would under the dad.implicit()
* Overriding inheritance - sometimes, you want the child to behave a little
  bit differently than the parent.  By redefining the exact same function
  in the child class, you are overriding the parent class.
* Alter before or after - by using the super() command, you can get the
  parent's methods can be used within the child momentarily

  The super() command is often used to call the __init__ of the parent, hence
  getting all of the initialization properties of the parent while also building
  initialization properties for the child.
  '''

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# Prints "PARENT implicit()"
dad.implicit()
# Prints "PARENT implicit()"
son.implicit()

# Prints "PARENT override()"
dad.override()
# Prints "CHILD override()"
son.override()

# Prints "PARENT altered()"
dad.altered()
# Prints "CHILD, BEFORE PARENT altered()", "PARENT altered()", print "CHILD, AFTER PARENT altered()"
son.altered()
