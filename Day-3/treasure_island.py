#day-3 project

print("Welcome to treasure Island \nYour mission is to cross through the door alive")

direction=input("You are at cross road.Where you want to go? Type 'left' or 'right'\n")

if(direction=='left' or direction=='Left'):
    print("You come to a lake.\nThere is an island in the middle of the lake.")
    boat_wait=input("Type 'wait' to wait for a boat.Type 'Swim' to swim across.\n")

    if (boat_wait=='wait' or boat_wait=='Wait'):
        print("You arrived at the island unharmed.\nThere is a houses with 3 doors.")
        doors=input("One red,one yellow and one blue.Which gate you want to enter\n")

        if(doors == 'yellow' or doors == 'Yellow'):
            print("You entered the house and won the game")

        elif (doors == 'blue' or doors == 'Blue' or doors == 'red' or doors == 'red'):
            print("wrong gate.Game over")

        else:
            print("Invalid input")

    elif(boat_wait=='swim' or boat_wait=='Swim'):
        print("There was crocodile in the water,you died, Game Over")

    else:
        print("Invalid input")

elif(direction=='right' or direction=='Right'):
    print("meet with an accident and died,Game Over")

else:
    print("Invalid output")