class Employee:
    name  = "Rakhi"
    language = "py"#this is the class attribute.
    salary = "120000"
    
    def __init__(self, name, salary, language):#dundar method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object") 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
            print("good morning")
rakhi = Employee("Rakhi", "1300000","js")
rakhi.name = "Rakhi"
print(rakhi.name,rakhi.salary,rakhi.language)
#rohan = Employee()
#actually in_it will get called whenever we make an object