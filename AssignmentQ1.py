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

    #Task 2
    #Expand the game aske the user if they choose cave if they want to light a torch or proceed int he dark and provide feedback responses for each decision

#solution: I aded an input for user_choice inside of the cave elif and then and if statement dependent upon the user input "Light a torch" with a response and then and else statement for any other user input other than light a torch.

    place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    user_choice = input("light a torch or proceed in the dark?: ")
    if user_choice == ("light a torch"):
        print("Great you can see the treasure clearly now!")
    else:
        print("Oh no! I found the treasure but its too dark to see!")


# Task 3 Default path i had the redo some of my previous code for this to work properly i changed my original else statements to elifs and then for the unknown user input error pass statements i used else and pass
place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass #this is for the invalid user input    
elif place == "cave":
    print("You find a hidden treasure!")
    user_choice = input("light a torch or proceed in the dark?: ")
    if user_choice == ("light a torch"):
        print("Great you can see the treasure clearly now!")
    elif user_choice == "proceed in the dark":
        print("Oh no! I found the treasure but its too dark to see!")
    else:
        pass #this is also for invalid user input where input is wanted
else:
    pass #to handle overall user input error
