# Creating a class named Number
class Number:

    # Constructor method
    def __init__(self, n):
        # Store the value inside object
        self.n = n

    # Operator overloading method for +
    def __add__(self, num):
        # Adding values of two objects
        return self.n + num.n


# Creating objects of Number class
n = Number(1)
m = Number(2)

# Using + operator on objects
# This internally calls __add__()
print(n + m)