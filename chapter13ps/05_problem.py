#write a program  to find the maximum numbers in a list using the reduce function.
from functools import reduce
l = [111, 234, 2, 65, 89908, 74, 55, 786, 90]

def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater, l))
     
