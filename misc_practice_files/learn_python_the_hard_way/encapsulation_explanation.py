#  Python Encapsulation (The art of data hiding)
#  What is an API? - the documentation
#  public, private,
#  _varaiables, _method

class ClassName():
    # Remember, upon instantiating a class object, the class calls the __init__ method to setup
    #
    def __init__(self):

        self._privatevariable = "Private"
        self.publicvariable = "Public"

    # The private method starts with an underscore, only to be used inside of class
    def _privateMethod1(self): pass
    def _privateMethod2(self): pass

    # Public methods should be called outside of class
    def publicMethod(self):

        return 5

c = ClassName()


# As we can see here, the public and private methods and variables can both
# be called, but it's considered "best practice" to use them as intended
print c._privateMethod1()
print c.publicMethod()
print c._privatevariable
print c.publicvariable
