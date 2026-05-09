marks = {
 "harry": 100,
    "shubh": 56,
    "roh": 23
}

#list of key value pairs
print(marks,type(marks))
#print(marks[0])#key error 
print(marks["harry"])
#marks = [["harry",100],]#list of list is allowed but in this way cannot get the value of harry by taking the name harry  as it will be computational  expensive when we write complex logic.
a = {"key":"value",
     "harry": "code",
     "marks":"100",
     "list":[1, 2, 9]
}
a["key"]#prints "value"
a[list] # prints[1,2,9]
#properties of python dictionaries
#unordered
#mutable
#indexed
#can not contain duplicate keys