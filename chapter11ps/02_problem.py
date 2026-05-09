#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    pass


# Pets inherits Animals
class Pets(Animals):
    pass


class Dog(Pets):

    @staticmethod   # static method → can be called without using self
    def bark():
        print("Bow Bow!")


d = Dog()
d.bark()