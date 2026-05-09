#sum: computer +you ,#lets assume you =-you and then sum :
if(computer == -1 and you ==1): 0 ,-2
        print("You win!")
    elif(computer == -1 and you == 0): -1 ,-1
        print("You lose!")
    elif(computer == 1 and you == -1): 0 ,2
        print("You lose!")
    elif(computer == 1 and you == 0): 1 ,1
        print("You win!")
    elif(computer == 0 and you == -1): -1, 1
        print("You win!")
    elif(computer == 0 and you == 1): 1, -1
        print("You lose!")
    else:
        print("something went wrong!")#just incase
    
if((computer - you) == -1 or (computer - you) == 2):
    print("you lose")
else:
    print("you win")
       