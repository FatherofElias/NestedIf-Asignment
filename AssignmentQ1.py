#Question 1
    #Task 1: Code correction: Identify errors and fix the buggy code.

#This is my explaination of my work below i apologize if it doesn't make good sense in advancve!

#place = input("Choose a place: forest or cave? ")

#if place = "forest": # On this line the "=" is not proper and should be "==" for proper syntax
#    action = input("climb a tree or cross a river?") # On this line the error i believe is that the code is just stacked weird it probably will run okay but this line should really be under the first line with the other user input question
#    if action = "climb a tree": #as far as i can see it is just the same error from line with the first error
#        print("You found a bird's nest!")
#   else action = "cross a river": # The "action = "cross a river": is not need because the else statement that comes before and will not run as written
#        print("You found a boat!")
#elif place = "cave":
#    print("You find a hidden treasure!")


#Solution
place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")