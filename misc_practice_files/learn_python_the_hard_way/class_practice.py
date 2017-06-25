class Company():

    # This is a "class/static" variable, because it applies to all instances
    # of the class, and not specific to one
    # Do not abuse the use of static variables!!
    company_name = "Costco"

    def __init__(self, office_loc, division):

        # These are called "instance variables," and are part of the object"
        self.office_loc = office_loc
        self.division = division

    def where_do_you_work(self):
        return self.office_loc

    def what_do_you_do(self):
        return self.division

job = Company("St. Louis", "Dev-Ops")

print job.where_do_you_work()
print job.what_do_you_do()

# In order to print a static variable, must call the class and not the instances
print Company.company_name
