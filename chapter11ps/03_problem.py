#Create a class ‘Employee’ and add salary and increment properties to it.
#Write a method ‘salaryAfterIncrement’ with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    # Class attributes (default values)
    salary = 234
    increment = 20

    # Property method (acts like a variable but actually runs a function)
    @property
    def salaryAfterIncrement(self):
        # Calculates salary after applying increment percentage
        return (self.salary + self.salary * (self.increment / 100))


    # Setter method for salaryAfterIncrement
    # This allows us to set salaryAfterIncrement and automatically update increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        # Calculate the increment percentage from new salary
        self.increment = ((salary / self.salary) - 1) * 100


# Creating object of Employee class
e = Employee()

# Setting salary after increment
# This will automatically calculate the increment percentage
e.salaryAfterIncrement = 280.8

# Printing the increment percentage
print(e.increment)