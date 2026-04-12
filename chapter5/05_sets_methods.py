s = {1,8,90 ,9 ,7 ,9 ,5 ,5 ,"harry"}
print(s,type(s))
s.add(899)
print(s,type(s))
#sets are unordered
#sets are unindexed ,cannot access elements by index
#there is no way to change items in sets
#sets cannot contain duplicate values
s = {1, 2, 3}
s.add(4)
print(s)
s.update([5, 6])
print(s)
s.remove(2)
print(s)
s.discard(10)  # no error
s.pop()
print(s)
s.clear()
print(s)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
a.issubset(b)
a.issuperset(b)
