#Question 2
    #Task 1
# Code Correction : Identify errors and fix the buggy code.

#attendees = input("Enter number of attendees: ") # this line there needs to be integer as part of the input so that the code can run properly because it is running as a string 
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)
#I belive that was the only error, but in the task explaination it stated specifically that there were "errors" as in plural but i cannot find any other errors

#solution:

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2

#solution: i hope i did this properly i tried a few other ways and ultimately settled on this just adding the 2 new strings with if and else with outputs per choice based on attendees
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
audio_system = "Stage speaker setup" if attendees > 100 else "small speaker setup"
projector = "premium projector and large screen" if attendees > 100 else "cheap projector with the normal screen size"
print("This is the audio/video setup we will use.")
print(audio_system)
print(projector)


#Task 3 
#Ask the user if they want vegetarian food. Reccomend veggie delight caterers if ys other wise gourmet meals caterers

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
audio_system = "Stage speaker setup" if attendees > 100 else "small speaker setup"
projector = "premium projector and large screen" if attendees > 100 else "cheap projector with the normal screen size"
print("This is the audio/video setup we will use.")
print(audio_system)
print(projector)

#solution i just used an input string for if they wanted veg or non veg and a print statement for if and else


catering_choice = input("Would you like Vegetarian? veg/non-veg: ")
if catering_choice == "veg":
    print("Let's go with Veggie Delight Caterers then!")
else:
    print("We'll go with Gourmet Meals Caterers then!")