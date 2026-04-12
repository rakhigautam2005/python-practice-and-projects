a = int(input("Enter your age: "))
 
 # if elif else ladder
 #if statement no.1
if(a%2 == 0):
    print("a is even")
#end of if statement no.1
#if statement no.2
if (a>=18):
    print("you are above the age of concent")
    print("Good for you")
#end of if statement no.2

elif(a<0):
    print("you are entering an invalid age")
    
elif(a==0):
    print("you are entering 0  which is not  a valid age")
    
else:
    print("you are below the age of concent")
     
print("end of program")

#there can be any number of elif statements
#last else is executed only if all the  conditions inside elif fails.