#the game() functio  in  a program lets a user  play a game and returns the score as an integer.You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to WAP to update the  Hi-score  whenever the game() function breaks the Hi-score.
import random

def game():
    print("you are playing the game")
    score = random.randint(1, 62)# to accesss random integers 
    #fetch the hiscore 
    with open("hiscore.txt")as f:
        hiscore = f.read()
        if(hiscore!=""):#if file contains something then convert it into integers and accept it as a high score.
            hiscore = int(hiscore)
        else:
            hiscore = 0#if file is empty
    print(f"your score:{score}")
    if(score>hiscore or hiscore==""):#if score is greater than hiscore then write that hiscore to hiscore.txt file
        
        #write this hiscore to the file.
        with open("hiscore.txt","w")as f:
            f.write(str(score))# as a string
game()
    