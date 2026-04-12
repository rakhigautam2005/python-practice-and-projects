#a file contains a word 'donkey' multiple times .You need to wap which replaces this word with ##### by updating the same file.
word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()#read the content of file
contentNew = content.replace(word, "#####")#replaced the word 

with open("file.txt", "w") as f:
    f.write(contentNew)#then again write it into file.txt
    