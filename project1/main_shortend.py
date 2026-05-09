import random
'''
 1 for snake 
 -1 for water 
 0 for gun
 '''
computer = random.choice([-1,0,1])#here  we have imported random module to generate  values randomy
youstr = input("enter your choice:")#here  to enter any choice in s,w,g 
youDict = {"s":1, "w": -1, "g": 0}#here we have taken the input as in form of s, g and w and then converted it into as given equals to what
reverseDict = {1: "Snake", -1: "water", 0: "gun"}#it will conver the numbers into snake water gun.
you = youDict[youstr]

#By now we have two numbers (variables),you and computer

print(f" you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")#here we have used reverseDict instead of using youDict because it can convert 1,0,-1 into snake ,gun and water respectively

if(computer == you):#if equals 
    print("it's a draw!")
else:
    '''
    if(computer == -1 and you ==1):(computer - you) = - 2
        print("You win!")
    elif(computer == -1 and you == 0):(computer - you) = -1
        print("You lose!")
    elif(computer == 1 and you == -1):(computer - you) = 2
        print("You lose!")
    elif(computer == 1 and you == 0):(computer - you) = 1
        print("You win!")
    elif(computer == 0 and you == -1):(computer - you) = 1
        print("You win!")
    elif(computer == 0 and you == 1):(computer - you) = -1
        print("You lose!")
        
        The below logic is written on the basis of the value of computer - you
        '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("you lose!")
    else:
        print("you win!")
       