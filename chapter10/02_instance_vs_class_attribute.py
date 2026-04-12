class Employee:
    name  = "Rakhi"
    language = "py"#this is the class attribute.
    salary = "120000"

rakhi = Employee()
#rakhi.language = "js"#this is an instance attribute and it will take preference over class attributes aduring assignment and retrieval 
print(rakhi.language,rakhi.salary)

