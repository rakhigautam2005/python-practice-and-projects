# open file
f = open("file.txt")

# read all lines as list
lines = f.readlines()
print(lines, type(lines))

# move pointer back to start of file
f.seek(0)

# read lines one by one
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

# if file ends it gives empty string
line6 = f.readline()
print(line6 == "")   # returns True

# reading file using while loop
f.seek(0)
line = f.readline()

while line != "":
    print(line)
    line = f.readline()

# close file
f.close()