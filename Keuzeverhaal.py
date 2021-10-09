import os
import sys

def restartprogram(): 
    restart = input("Want to Restart? (y/n)")
    if restart == "y":
            os.execl(sys.executable, sys.executable, *sys.argv)


answer1 = input("You walking across the street and u see a kid trying to cross a street, but a truck is driving full speed and is about to hit the child. What are u going to do? \na. run toward the child and push the child away \nb. just stand and watch what is going to happen \nc. yell to kid to get out of the way \nAnswer: ")
if answer1 == "a":
   print("U SAVED THE CHILD! but u pissed ur self in shock and died....")
   print("u saved the child but u died and pissed your self. HAHAHHAHAHAH I'm sorry... you wake up in a dark room with a goddess right in front off you. she explains how u died (giggle).")
   answer2 = input("she ask u if u want to go heaven or be reincarnated to a game and defeat the demon king. u can take one thing with u what will you choose? \na.  A powerful sword. \nb. the strongest armor \nc. the goddess... \nAnswer: ")
   if answer2 == "a":
       print(" pfft Beta here take your sword. Sorry we ran out of swords")
       restartprogram()
   elif answer2 == "b":
        print("mhm okay here is your dragon skin armor. SIKE I LIED ")
        restartprogram()
   if answer2 == "c":
        print("the goddess laughed and said no but a other goddess comes in and says to her that she is going with you. you both got send to the game. The goddess cries")
        answer3 = input("You and the goddes got send to a diffrent world. you awoke from a deep sleep in a shack, you looked around and saw the goddes still sleeping next to you. confused you went out side and saw alot of monsters.\nWhat will you do:\nA. Fight the like a Sigma Male\nB. Scream for help so someone might come and rescue you \nC. Go Back inside and hope the monsters haven't noticed you.\nAnswer: ")
        if answer3 == "a":
            print("You tried to fight all of the monsters but you realised you aint that guy. You died ")
            restartprogram()
        if answer3 == "b":
            print("you Screamed your lungs out and cried like a sussy baka but nobody came.... \n\n\nExcept the goddes and she destroyed every single monster with a flick of her finger ")
        if answer3 == "c":
            print("You went back inside and you hoped that the monsters didnt notice you. They broke the door down and sliced your head off and took it as a trophy")
            restartprogram()
        else:
            print("not a valid response")
            restartprogram()
   else:
        print("not a valid response")       
        restartprogram()

        

    
    
elif answer1 == "b":
    print("the poor little child died. how dare u stand there and do nothing >:(")
    restartprogram()
elif answer1 == "c":
     print("The kid didn't hear u and died...")
     restartprogram()

else:
    print("not a valid response")
    restartprogram()
