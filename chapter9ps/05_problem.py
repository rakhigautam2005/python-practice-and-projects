#repeat the program 4 for a list of such words to be censored.
words = ["Donkey","dirty","ganda","bad"]

with open("file.txt", "r") as f:
    content = f.read()#read the content of file
for word in words:
    content = content.replace(word, "#" *len(word))#content is replaced with the word acc to its length

with open("file.txt", "w") as f:
    f.write(content)#then again write it into file.txt
    