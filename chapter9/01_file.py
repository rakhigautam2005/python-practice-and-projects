'''
a = "a very long string with emails"
emails = []#emails generated 
3 seconds
'''
#to  store the data that we generated in program we need to use  the file only then our data will get persist or saved
# the RAM mis volatile, and all itscontents are lost once a program terminates in order to persist the data forever,we use files
#a file is a data storage device. A python program talk to the fileby reading content from its and writing content to it.  
# types of files are of two
# Text Files (.txt,.c, etc.)
#Binary Files(.ipg,.dat,etc.)

#how to read from a file
f = open("file.txt","r")
data = f.read()
print(data)
f.close()