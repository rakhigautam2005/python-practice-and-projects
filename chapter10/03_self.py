#self parameter is a instance of the class .it is automatically passed with a function call from an object.
class Employee:
    name  = "Rakhi"
    language = "py"#this is the class attribute.
    salary = "120000"
    
    def getInfo(self):#object in which method is running is self
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    def greet(self):
        #errror will come if we will not provide self and employee.greet will get convert into rakhi.greet
        print("good morning")
rakhi = Employee()
rakhi.language = "js"#this is an instance attribute and it will take preference over class attributes aduring assignment and retrieval .

rakhi.getInfo()
#Employee.getInfo(rakhi)
rakhi.greet()