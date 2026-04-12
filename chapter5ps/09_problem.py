#can you change the values inside a list which is contained in set s?
s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9
#list is  not hashable even if it cannot be done 
# as you can't have a list as an element in a set because  sets in python requires all their elements to be immutable and  hashable.
#lists are  not hashale  and mutable so they can't be added to a set