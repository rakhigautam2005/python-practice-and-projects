#wap using functions to find the greatest of three numbers
def greatest (a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
a = 1
b = 24
c = 3
print(greatest(a,b,c))