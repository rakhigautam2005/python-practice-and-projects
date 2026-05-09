#class is  a blueprint for cretaing a object that are valid.
class Employee:
    name  = "Rakhi"
    language = "py"#this is the class attribute.
    salary = "120000"

rakhi = Employee()
rakhi.name = "Rakhi"#this is an object attribute.

print(rakhi.name, rakhi.language,rakhi.name)
#here harry is a object  and an object ia an instantiation of class.when a class is defined ,a template(info) is defined .Memory is located just after the object instantiation.
# class attribute is a attribute that belongs to the class rather than particular object.
rohan = Employee()
rohan.name = "Roro"
print(rohan.salary, rohan.language,rohan.name)
#here name is instance attribute and salary and language they directly belong to the class.

