# Author RTS 3/16/22

# Defining function
def build_vehicle():
    print("Your car is {0}, has {1} wheels, has {2} axels, and {3} doors.".format(color, wheels, axels, doors)) 

# Create variables 
axels = input("How many axels would you like?")
doors = input("How many doors would you like?")
color = input("What color would you like?")
wheels = input("How many wheels would you like?")

#Test
build_vehicle() 
