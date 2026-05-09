def goodDay(name):
    print("Good Day," + name)
goodDay("Harry")#o/p= Good Day, Harry
goodDay("Rohan")#o/p= Good Day, Rohan
def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)
goodDay("Harry", "Thankyou")
#o/p= Good Day, Harry
#Thankyou               
goodDay("Rohan", "Thankyou")
#o/p= Good Day, Rohan
#Thankyou
def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)
    return("ok") #this value will be assigned to a  and we use it when we want to give any value

a = goodDay("Harry", "Thankyou")
print(a)
#o/p= Good Day, Harry
#Thankyou
#ok
