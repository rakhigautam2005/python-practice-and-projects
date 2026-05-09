# Creating a class named Employee
class Employee:

    # Class attribute (same for all objects)
    a = 1

    # Class method (works with class variables)
    @classmethod
    def show(cls):
        # cls refers to the class itself
        print(f"The class attribute of a is {cls.a}")

    # Property decorator (used to access method like a variable)
    @property
    def name(self):
        # Returns full name by combining first and last name
        return f"{self.fname} {self.lname}"

    # Setter method for the property "name"
    @name.setter
    def name(self, value):
        # Splitting the full name into first and last name
        self.fname = value.split(" ")[0]  # First name
        self.lname = value.split(" ")[1]  # Last name


# Creating an object of Employee class
e = Employee()

# Changing the class attribute using object
e.a = 45

# Setting the name using property setter
e.name = "Harry Khan"

# Printing first name and last name separately
print(e.fname, e.lname)

# Calling class method
e.show()