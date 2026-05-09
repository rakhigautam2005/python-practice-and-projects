#wap to print the greatest number of four numbers entered by the user.
a1 =  int(input("enter number 1:"))
a2 =  int(input("enter number 2:"))
a3 =  int(input("enter number 3:"))
a4 =  int(input("enter number 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("the greatest number is a1:", a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("the greatest number is a2:", a2)
if(a3>a1 and a3>a2 and a3>a4):
    print("the greatest number is a3:", a3)
if(a4>a1 and a4>a2 and a4>a3):
    print("the greatest number is a4:", a4)

    