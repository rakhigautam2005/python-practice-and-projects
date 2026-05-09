#write a program to input name, marks and phone number of a student and format it using the format function like below:
#s = "The name of the student  is Rakhi Gautam ,her marks are 79 and phone number is 99999888"

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, her marks are {} and phone number is {}".format(name, marks, phone)

print(s)