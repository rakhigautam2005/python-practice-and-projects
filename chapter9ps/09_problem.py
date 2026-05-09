#wap to find out whether a file is idenwtical and matches the content of another file.
with open("file.txt") as f:
    content1 = f.read()
with open("poem.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print(" yes these files are identical")
else:
    print("no these files are not identical")