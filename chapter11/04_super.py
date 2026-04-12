class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1


class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()#it will consider above class too.
        print("Constructor of Manager")
    c = 3
o =Employee()
print(o.a)#Prints the a attribute
#print(o.b)#prints the error as there is no attribute in Employee class
#o =Programmer()
#print(o.a,o.b)
o = Manager()
print(o.a,o.b,o.c)