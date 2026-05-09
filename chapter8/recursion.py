'''
factorial(0) =0
factorial(1) = 1
factorial(2) = 2x1
factorial(3) = 3x2x1
factorial(4) = 4x3x2x1
factorial(5) = 5x4x3x2x1
factorial(n) = nxn-1x....3x2x1
factorial(n) = n*factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n= int(input("enter a number:"))
print(f"the factorial of this number is:{factorial(n)}")
    
