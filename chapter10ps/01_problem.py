#create a class "Programmer"for sorting in formation of few programmersa  working at a microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name =name
        self.salary = salary
        self.pin = pin

p = Programmer("Rakhi", 1200000,208011)
print(p.name,p.salary,p.pin,p.company)
r = Programmer("Rohan", 1200000,208011)
print(r.name,r.salary,r.pin,r.company)
