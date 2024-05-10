### Imported Python librabries random for random integers for dice rolls 
## Time for timer
import random,time,sys
# Python typing text effect from 101 Computing.net
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

### Intro Message ASCII Art

intro_art = r"""                                                                                                                                                                            

░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░       
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░              ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░         ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░               ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░               ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░         ░▒▓██▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░                                                                                                                                                                                  
"""
print(intro_art)

# Welcome Message
print("Welcome to Space RPG Alone In The Void!")
print("Please follow the instructions to create your own character for this story, good luck out there spacefarer!")

# Character Creation creates a unique character by name , racial background

class Character:
    def __init__(self, name, race, health, attack, luck):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.luck = luck
    
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Luck: {self.luck}")

def create_player():
    name = input("Name your character: ")
    return name

def choose_race():
    races = ["Earthling - you're a human who's ancestors once lived on Earth.", 
             "Martian - you're tenth generation from the Mars colonly.", 
             "Gorbling - a feline species from deep space small and blue in colour."]
    
    print("Select your race:")
    for i, race in enumerate(races, 1):
        print(f"{i}. {race}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(races):
                return races[choice - 1]
            else:
                print("Invalid choice. Please enter a number corresponding to a race.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Stat Allocation. Give your character additional points as you wish.")
available_points = 10
name = "Player Name"
attributes = {"Health": 5, "Attack": 3, "Luck": 2}

while available_points > 0:
    print(f"\nPoints Remaining: {available_points}")
    print("Allocate points to attributes:")
    for attribute in attributes:
        print(f"{attribute}: {attributes[attribute]}")
    attribute_choice = input("Enter attribute to allocate points (or 'done' to finish): ").capitalize()

    if attribute_choice == "Done":
        break

    if attribute_choice not in attributes:
        print("Invalid attribute. Please choose from Health, Attack, or Luck.")
        continue

    points_to_allocate = int(input("Enter points to allocate: "))
    if points_to_allocate <= available_points:
        attributes[attribute_choice] += points_to_allocate
        available_points -= points_to_allocate
    else:
        print("Not enough points. Try again.")
name = create_player()
race = choose_race()
player = Character(name, race, attributes["Health"], attributes["Attack"], attributes["Luck"])
print(f"\nCharacter {player.name} created with stats: Health: {player.health}, Attack: {player.attack}, Luck: {player.luck}")


class Rooms:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# Creating rooms and managing them all
def create_rooms():
    rooms = []

    # Adding rooms to the map
    rooms.append(Rooms("Supply Closet", "A small closet overloaded with cleaning supplies."))
    rooms.append(Rooms("Air Lock", "A chamber with a door that opens to  the crushing void of space."))
    rooms.append(Rooms("Escape Pod", "A small pod for emergency escape, you're only hope for survival."))
    rooms.append(Rooms("Crew Quarters", "Abandoned living quarters for the crew members."))

    # Adding items to individual rooms
    rooms[0].add_item("Laser Gun")
    rooms[0].add_item("Security Badge Pass")
    rooms[1].add_item("Air Lock Control Panel")
    rooms[1].add_item("Air Lock Control Manual")
    rooms[2].add_item("Escape Pod Controls")

    return rooms

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You found a {item}.")

# Start Game
print("Your eyes adjust as you open them to a dim room full of cleaning supplies.") 
print("Blinking, you wince in pain as you touch your forehead.") 
print("Looking at your hand, you can see drying blood.")
print("How did I get here...? Why am I not able to remember where I am?")
print("Search the room?")

# Defining dice roll asking it to randomize a number between 1-20 to simulate throwing a D20
def dice_roll():
    return random.randint(1, 20)

# Print function to show dice result to the user
result = dice_roll()
("You rolled a:", result)

# Prompt user for choice to search room or exit

def main():
    while True:
        player_input = input("Please choose what you wish to do search or exit the supply closet: ").lower()
        if player_input in ["search", "exit"]:
            return player_input
        else:
            print("Invalid command. Please type 'search' or 'exit'.")

if __name__ == "__main__":
    answer = main()

    if answer == "search":
        print("You begin to rummage through the room")
        # Dice roll to search room
        result = dice_roll()

        if result <= 9:
            # PASS 
            print("You find a laser gun with 2 ammo left and a badge pass and exit the room.")
        else:
            # FAIL
            print("You find nothing, frustrated, you exit the room")

    elif answer == "exit":
        print("You leave the room without searching")
    else:
        print("Please select a valid option.")

# Character route selection 3 corridors 
print("You see three corridors ahead of you one to your left, straight ahead and one to your right")
print("Which path will you take?")

def direction():
        while True:
         player_input = input("Please choose which way to go left, straight ahead, or right: ").lower()
         if player_input in ["left","straight ahead","right"]:
            return player_input
         else:        
            print("Invalid direction please try again from left, right or straight.")

# Right corridor headed to Air lock
print("You decide to proceed by going down the right corridor.")
print("You find some blood streaks on the walls and ground but no corpses")
print("You Pick up your walking pace as panic creeps in.")
print("Spriting you run to the door at the end of the corridor.")
print("You notice the sign Air Lock and notice three buttons coloured red, yellow and green on a control panel")
# Newline escape sequence to present the options
print("\nWhat do you choose to do?")
print("1. Search the room.")
print("2. Inspect the control panel.")
print("3. Search the room.")

action = input("Enter your choice (1, 2, 3,): ")
if action == "1":
    print("You begin to look around the room.")
    result = dice_roll()
    print("You rolled a:", result)
    if result <=5:
         # FAIL 
        print("You find nothing.")
         # PASS
    if result <=6: 
        print("You find an air lock manual.")
        print("You decide to read the manual.")
        print("Green- Open Lock")
        print("Yellow- Timed Open for 15 seconds Lock")
        print("Red - Close Lock")
    if action =="2":
        print("You see the three buttons")
        # Needs to be expanded
# Straight ahead to Escape Pod
print("You proceeed straight ahead.")
print("There's a eerie quiet as the lights flicker on the ship.")
print("You noticed another figure slumped against a wall panting heavily.")
print("'Stop!' the figure exclaims. You notice a beam of a laser rifle hover in fron of your vision")
print("")
# Prompt user for choice to talk to , attack the figure or run away
answer = input("Choose 'talk', 'attack' or flee")

if answer == "talk":
    print("You tell the figure that you mean them no harm")
    result = dice_roll()
    print("You rolled a:", result)
    if result <=10:
        # FAIL TALK CHECK
        print("You start to ty and negotiate but it's hopeless")
        print("The last thing you hear is the laser shot exploding")
        print("You have failed to escpae the ship and it's now your grave")
        print("You are dead.")
        print("Try again? Select restart or quit")
        answer = input("restart or quit game?")
    if result <=11:
        # PASS TALK CHECK
        print("The figure heisates lowering their weapon")
        print("You slowly approach each other")
        print("'You're on the crew!' You see that this is a fellow crew member.")
        print("She is bleeding from her side panting.")
        print("'I'm Sam, don't think we've met'She saltues you.")
        print("We need a security badge to get the hell outta here, you don't have one to do you?")
        # Check if badge pass is in user inventory 
        if answer =="attack":
            print("You lunge at your assailant")
            result =  dice_roll()
            print("You rolled a:", result)
    if answer == "flee":
        print("You turn on your heel and begin to try and run away")
        result = dice_roll()
        print("You rolled a:", result)
if result <=7:
        # FAIL FLEE CHECK
        print("You try to escape in time for naught.")
        print("'Pathetic' are the last word you hear as your vision dims.")
        print("You are dead.")
        print("Try again? Select restart or quit")
        answer = input("restart or quit game?")
        # PASS FLEE CHECK
        print("Your legs pump as you hear the figure shuting at you.")
        print("A shot is fired hitting the celing.")
        print("You have survived and are now outside where you began.")
        print("'I need a weapon to defend myself if I want to go again.'you mutter to yourself.")

# Left to Crew Quarters

# Hallway encounter with an alien bounty hunter if you decide to go left Crew Quarters
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
