#Write a class vector representing a vector of n dimensions.
#Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:

    # Constructor to initialize x, y, z components
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Overloading + operator for vector addition
    def __add__(self, other):
        # Adding corresponding components of two vectors
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # Overloading * operator for dot product of two vectors
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # String representation of vector
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Creating vector objects
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

# Vector addition
print(v1 + v2)   # Output: Vector(5, 7, 9)

# Dot product of vectors
print(v1 * v2)   # Output: 32