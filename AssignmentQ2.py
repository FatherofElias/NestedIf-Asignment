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

