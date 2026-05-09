#Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:

    # Constructor to initialize real (r) and imaginary (i) parts
    def __init__(self, r, i):
        self.r = r   # real part
        self.i = i   # imaginary part

    # Overloading + operator to add two complex numbers
    def __add__(self, c2):
        # c2 is the second complex number object
        return Complex(self.r + c2.r, self.i + c2.i)

    # Defines how the object will be printed
    def __str__(self):
        return f"{self.r} + {self.i}i"


# Creating two complex number objects
c1 = Complex(1, 2)   # 1 + 2i
c2 = Complex(3, 4)   # 3 + 4i

# Adding the two complex numbers using overloaded + operator
result = c1 + c2

# Printing the result
print(result)