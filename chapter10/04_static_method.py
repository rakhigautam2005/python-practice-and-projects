#static method is a method when sometimes we need a function that does not use the self parameter .
class Employee:
    name  = "Rakhi"
    language = "py"#this is the class attribute.
    salary = "120000"
    @staticmethod
    def getInfo():#no need to povide self if we are using the static method.
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("good morning")
rakhi = Employee()
rakhi.language = "js"#this is an instance attribute and it will take preference over class attributes aduring assignment and retrieval .

rakhi.getInfo()
#Employee.getInfo(rakhi)
rakhi.greet()