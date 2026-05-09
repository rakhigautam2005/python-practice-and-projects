d = {}#empty dicttionary
d = {"name": "Rakhi", "age": 20}
print(d.keys())#returns all keys in dic
print(d.values())#returns all values in dic
print(d.items())#returns key value pairs
print(d.get("name"))#returns value of given key
print(d.get("city"))  # not present
d.update({"city": "Lucknow"})
#print(d)#update the dic
d.pop("age")
#print(d)#removes the given key and returns its value
d.popitem()
#print(d)#removes and return the last inserted key value pair
d.clear()
#print(d)
new_d = d.copy()
#print(new_d)#returns a copy of dictionary
d.setdefault("country", "India")
print(d)#returns value of key and if key is not present than inserts it with default value pair