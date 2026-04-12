#wap to find out whether a  student has passed or failed if it requires  a total of 40 % and at least 33% in each subject to pass .assume 3 subjects  and take  marks as  an input from user.
marks1 =  int(input("enter marks 1: "))
marks2 =  int(input("enter marks 2: "))

marks3 =  int(input("enter marks 3: "))

#check for total percentage
total_percentage = 100*((marks1 + marks2 + marks3)/300)
if (total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you are pass")

else:
    print("you failed, try again next year!")