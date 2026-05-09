#Override the len() method on vector of problem 5 to display the dimension of the vector.
class Vector:

    # Constructor that takes a list of vector elements
    def __init__(self, l):
        self.l = l

    # Magic method to define what len(object) should return
    def __len__(self):
        return len(self.l)   # returns length of the internal list


# Creating a vector object
v1 = Vector([1, 2, 3])

# Calling len() on the object
print(len(v1))