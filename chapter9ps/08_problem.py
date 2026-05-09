#wap  to make a copy of file "this.
with open("this.txt")as f:
    content = f.read()#reads the file
with open("this_copy.txt", "w") as f:
    f.write(content)#copies the file
    