import sys
import random

ans = True

while ans:
    question = input("Try to concentrate on the question...Ready? Ask the magic ball: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("You are lacky!It's yes!")
    
    elif answers == 2:
        print ("100% Everything will be as you want!")
    
    elif answers == 3:
        print ("The future is in your hands! Stop sitting in front of the monitor! Go to your work!")
    
    elif answers == 4:
        print ("Try to be more active in order to fight for the future!")
    
    elif answers == 5:
        print ("Ask again when the moon will cross the street!")
    
    elif answers == 6:
        print ("Try again in next life :-)")
    
    elif answers == 7:
        print ("Even don't try! It's hard NO!")
    
    elif answers == 8:
        print ("NO! NO And NO!")

