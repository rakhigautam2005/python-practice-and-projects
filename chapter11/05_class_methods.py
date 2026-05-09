class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45

e.show()#as it will print 45 as an o/p instance attribute but we want it to  give class attribute  so we will use  classmethod and gives 1 as an o/p.