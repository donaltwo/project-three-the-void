import random

### Intro Message
print("Welcome to Space RPG!")
print("Please follow the instructions, good luck out there spacefarer!")

# Defining dice roll asking it to randomize a number between 1-20 to simulate throwing a D20
def dice_roll():
    return random.randint(1, 20)

# Print function to show dice result to the user
result = dice_roll()
print("You rolled a:", result)

# Name your Character

# Character class

class Character:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health

player = Character(5, 15)
hunter = Character(10, 10)
print(player)

# Start Game
print("Your eyes adjust as you open them to a dim room full of cleaning supplies.") 
print("Blinking, you wince in pain as you touch your forehead.") 
print("Looking at your hand, you can see drying blood.")
print("How did I get here...? Why am I not able to remember where I am?")
print("Search the room?")

# Prompt user for choice to search room or exit
answer = input("Enter 'search' or 'exit': ").lower()

if answer == "search":
    print("You begin to rummage through the room")
    # Dice roll to search room
    result = dice_roll()

    if result <= 9:
        # PASS 
        print("You find a laser gun with 2 ammo left and a badge pass and exit the room.")
    # FAIL
    else:
        print("You find nothing, frustrated, you exit the room")

elif answer == "exit":
    print("You leave the room without searching")
else:
    print("Please select a valid option.")

# Hallway encounter with an alien bounty hunter
print("You exit the supply closet and step into a hallway.")
print("You notice you're on a spaceship")
print("You also notice you're not alone!")
print("A tall blue alien bounty hunter is 10 feet away")
print("You start to panic and need to make a decision quick")

# Prompt user for choice to fight alien or to flee
answer = input("Enter 'fight' or 'flee': ").lower()

if answer == "fight":
    print("You lunge at the alien, knocking them back and start grappling on the ground.")
    print("You struggle as it attempts to push you off")
    # Roll the dice again to determine fight outcome 
    result = dice_roll()
    if result <=11:
        # PASS 
        print("You headbutt the alien stunning it and making it motionless")
        print("You pick yourself and start running")
else:
    print("You feebly struggle with the alien")
    print("Your strength weakens and you feel blinding pain your neck")
    print("The alien eviscerates you")
    print("You are dead.")
    print("Do you wish to continue?")
    answer = input("Enter 'yes' or 'no'").lower()
    if answer == "yes":
        # Restart the game
        pass
    elif answer == "no":
        print("Thanks for playing better luck next time!")
        exit()
# 3 advantage to roll outcome if you have a laser gun object
print("You detangle yourself from the alien suddenly")
print("Being back on your feet, you point your gun at the alien's face")
print("You pull the trigger as the laser melts the alien's face into a sizzling pool of blue liquid")
