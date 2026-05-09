#wap to find out the line number  where python is present from ques 6.

with open("log.txt") as f:
    lines = f.readline()#reads lines
lineno = 1#start from line 1
for line in lines:#used for loop 
    if ("python" in line):#if present in line
        print(f"yes python is present. Line no: {lineno}")
        break#if break works else will not and if whole loop has worked  or exhausts only then else will work 
    lineno +=1
    
else:
    print("no python is not present")