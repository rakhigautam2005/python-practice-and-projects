#create a class with a class attribute  a; create a object from it and set 'a' directly using object = 0 .does this change the class attribute.
class Demo:
    a = 2
o = Demo()
print(o.a)#prints the class attribute because the instance attribute is not present. 
o.a = 0#instance  attribute is set.
print(o.a)#printsthe instance attribute becuase the instance attribute is present.
print(Demo.a)#prints the class atttribute and the attribute of class won't change .
     