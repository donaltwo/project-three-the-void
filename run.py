
### Imported Python librabries random for random integers for dice rolls 
import os
import random
import time

### Intro Message ASCII Art

INTRO_ART = r"""                                                                                                                                                                            
 _____ _   _  _____   _   _  _____ ___________ 
|_   _| | | ||  ___| | | | ||  _  |_   _|  _  \
  | | | |_| || |__   | | | || | | | | | | | | |
  | | |  _  ||  __|  | | | || | | | | | | | | |
  | | | | | || |___  \ \_/ /\ \_/ /_| |_| |/ / 
  \_/ \_| |_/\____/   \___/  \___/ \___/|___/  
                                                                                                                                                                                                                                                                    
"""


# Inventory class for player character and enemies
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
# Inventory class for player items
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You found a {item}.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"You used {item}.")
        else:
            print(f"You don't have {item} in your inventory.")

    def display_inventory(self):
        if self.items:
            print("Inventory:")
            for item in self.items:
                print("-", item)
        else:
            print("Your inventory is empty.")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")

# Game Logic

def dice_roll():
    """
    Function to simulate rolling a D20 dice.
    """
    return random.randint(1, 20)

def player_input(prompt):
    """
    Function to get input from the player with whitespace handling.
    """
    while True:
        player_input = input(prompt).strip()
        if player_input and not player_input.isspace():
            return player_input
        else:
            print("You have not entered any text characters, please try again.")

def create_player():
    """
    Function to create a player by asking for their name.
    """
    name = player_input("Name your character: ")
    return name

def choose_race():
    """
    Function to allow the player to choose their race.
    """
    race_options = ["Earthling - you're a human whose ancestors once lived on Earth. +3 Luck -1 Attack", 
                    "Martian - you're tenth generation from the Mars colony. +4 Attack -2 Health", 
                    "Gorbling - a feline species from deep space, small and blue in color. +3 Luck -3 Attack",
                    "Chutuleon- You're a tentacled squid like cosmic terror +5 Attack -5 Luck"]
    print("Select your race:")
    for i, race in enumerate(race_options, 1):
        print(f"{i}. {race}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(race_options):
                return race_options[choice - 1], choice
            else:
                print("Invalid choice. Please enter a number corresponding to a race.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_character():
    """
    Function to create a character with allocated stats.
    """
    print("Stat Allocation. Give your character additional points as you wish.")
    available_points = 10
    attributes = {"Health": 5, "Attack": 3, "Luck": 2}

    name = create_player()
    race_str, race_choice = choose_race()

    # Stat bonusesfor attributes based on race choice
    if race_choice == 1:  # Earthling
        attributes["Luck"] += 3
        attributes["Attack"]-= 1

    elif race_choice == 2:  # Martian
        attributes["Attack"] += 2
        attributes["Health"]-= 2

    elif race_choice == 3:  # Gorbling
        attributes["Luck"] += 3
        attributes["Attack"] -= 3

    elif race_choice == 4: #Cthuleon
        attributes ["Attack"] += 5
        attributes ["Luck"] -= 5

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

        try:
            points_to_allocate = int(input("Enter points to allocate: "))
            if points_to_allocate <= available_points:
                attributes[attribute_choice] += points_to_allocate
                available_points -= points_to_allocate
            else:
                print("Not enough points. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player = Character(name, race_str, attributes["Health"], attributes["Attack"], attributes["Luck"])
    print(f"\nCharacter {player.name} created with stats: Health: {player.health}, Attack: {player.attack}, Luck: {player.luck}")

    

def intro():
    """
    Function to display the introduction and game instructions.
    """
    print(INTRO_ART)
    print("Welcome to a text adventure Space RPGT he Void!")
    print("You will find items, encounter enemies and roll a 20 sided dice like in games such as Dungeon & Dragons!")
    print("Please follow the instructions to create your own character for this story, good luck out there spacefarer!")
    print("You have various words you can type to help you navigate this adventure. Please check for typos before entering your commands.")
    print("Search - search the area for items")
    print("Exit - leave the current area")
    print("Talk - speak to another character")
    print("Attack - enter into combat with the character")
    time.sleep(3)
    create_character()

intro()

# Creating rooms and managing them all

def create_room():
    room = []

    # Adding rooms to the map
    room.append(Room("Supply Closet", "A small closet overloaded with cleaning supplies."))
    room.append(Room("Air Lock", "A chamber with a door that opens to  the crushing void of space."))
    room.append(Room("Escape Pod", "A small pod for emergency escape, you're only hope for survival."))
    room.append(Room("Crew Quarters", "Abandoned living quarters for the crew members."))

    # Adding items to individual rooms

    room[0].add_item("Laser Gun")
    room[0].add_item("Security Badge Pass")
    room[1].add_item("Air Lock Control Panel")
    room[1].add_item("Air Lock Control Manual")
    room[2].add_item("Escape Pod Controls")

    return room

# Combat system for when players encounter enemies
def fight(self,enemy):
    print(f"{self.name} damages {enemy.name}!")
    enemy.health -= self.attackPower
    print(f"{enemy.name}'s has {enemy.health} left.")

def flee(self):
    if dice_roll() <=10:
      print(f"{self.name} successfully flees from the enemy!")
      return True
    else:
      print(f"{self.name} fails to flee from the enemy!")
      return False
    
# Charcter list of encountare non playable characters 
alien = Character("Bounty Hunter", "Chutuleon", 20, 15, 0)
sam = Character("Sam","Human", 15,10,0)


# Start Game
print("Your eyes adjust as you open them to a dim room full of cleaning supplies.") 
print("Blinking, you wince in pain as you touch your forehead.") 
print("Looking at your hand, you can see drying blood.")
print("How did I get here...? Why am I not able to remember where I am?")
print("Search the room?")


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
        print("You rolled a:", result)

        if result >= 9:
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


# Call the direction function to get user choice
chosen_direction = direction()

# Use the chosen direction 

if chosen_direction == "right":
    print("You decide to proceed by going down the right corridor.")
    # Air Lock Scenario
def air_lock_luck_check(character): 
    print( "You arrive to a door with an Air Lock sign, you enter eploring further.")
    print("You notice the sign Air Lock and notice three buttons coloured red, yellow and green on a control panel")
    print("\nWhat do you choose to do?")
    print("1. Search the room.")
    print("2. Inspect the control panel.")
    print("3. Exit the room.")

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
    elif action =="2":
        print("You see the three buttons")
        print("\nWhich button will you press?")
        print("1.Press the red button.")
        print("2.Press the yellow button.")
        print("3.Press the green button.")
        print("4. You decide to print none of the buttons")
        button_choice = input("Enter your choice (red, yellow, green, none): ").strip()
        if not button_choice:
            print("Invalid choice! You have entered please enter the word for your choice")
        if button_choice.lower() not in ['red','yellow','green''none']:

            if button_choice.lower() ==" red":
                print("The air lock makes a loud hum")
                print("'Air lock  staus sealed' a ship system confirms to you in a flat tone. ")

        elif button_choice.lower() == "yellow":
            print("'Timed air lock sequence initiated")
            print("You freeze as you see the air lock lights flash.")
            print("You need to get out of here now!!")
            if "Luck">=9:
                print("You snap back to realilty. from your fear paralysis.")
                print("You throw yourself through the door back into the corridor")
                print("The door seals itself as the air lock")
                print("Panting you pick yourself up and walk back towards the supply closet")
                print("Time to pick a diffreent path")

        elif button_choice.lower() == "green":
            print("You hit the green button")
            print("Air lock openeing")
            print("Your eyes bulge in dread")
            print("The last thing you ever experience is the sensation fo imploding")
            print("You are dead")
            print("Restart or quit?")

            print("Invalid choice please type the colour red, yellow, green or none to continue")
        else:
            pass
    else:
        print("Invalid choice. Please enter 1,2 or 3.")

    if action =="3":
        print("You exit the room.")

elif chosen_direction == "left":
    print("You decide to proceed by going down the left corridor.")
    print("You find some blood streaks on the walls and ground but no corpses")
    print("You Pick up your walking pace as panic creeps in.")
    print("Spriting you run to the door at the end of the corridor.")
else:
    print("You decide to proceed straight ahead.")
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
    print("You rolled a:", result)
    if result >=11:
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
        

# 3 advantage to roll outcome if you have a laser gun object

print("You detangle yourself from the alien suddenly")
print("Being back on your feet, you point your gun at the alien's face")
print("You pull the trigger as the laser melts the alien's face into a sizzling pool of blue liquid")

# Straight ahead to Escape Pod

print("You proceeed straight ahead.")
print("There's a eerie quiet as the lights flicker on the ship.")
print("You noticed another figure slumped against a wall panting heavily.")
print("'Stop!' the figure exclaims. You notice a beam of a laser rifle hover in fron of your vision")

# Prompt user for choice to talk to , attack the figure or run away

answer = input("Choose 'talk', 'attack' or flee")

if answer == "talk":
    print("You tell the figure that you mean them no harm")
    result = dice_roll()
    print("You rolled a:", result)
    if result <=10: # FAIL TALK CHECK

        print("You start to ty and negotiate but it's hopeless")
        print("The last thing you hear is the laser shot exploding")
        print("You have failed to escpae the ship and it's now your grave")
        print("You are dead.")
        print("Try again? Select restart or quit")
        answer = input("restart or quit game?")

    if result <=11: # PASS TALK CHECK

        print("The figure heisates lowering their weapon")
        print("You slowly approach each other")
        print("'You're on the crew!' You see that this is a fellow crew member.")
        print("She is bleeding from her side panting.")
        print("'I'm Sam, don't think we've met'She saltues you.")
        print("We need a security badge to get the hell outta here, you don't have one to do you?")

        # Check if badge pass is in user inventory 

        if answer =="attack":  # COMBAT CHECK
            print("You lunge at your assailant")
            result =  dice_roll()
            print("You rolled a:", result)

    if answer == "flee": # ESCAPE CHECK
        print("You turn on your heel and begin to try and run away")
        result = dice_roll()
        print("You rolled a:", result)

if result <=7: # FAIL ESCAPE CHECK
        print("You try to escape in time for naught.")
        print("'Pathetic' are the last word you hear as your vision dims.")
        print("You are dead.")
        print("Try again? Select restart or quit")
        answer = input("restart or quit game?")

        if result <=8: # PASS ESCAPE CHECK
            print("Your legs pump as you hear the figure shuting at you.")
            print("A shot is fired hitting the celing.")
            print("You have survived and are now outside where you began.")
            print("'I need a weapon to defend myself if I want to go again.'you mutter to yourself.")

if __name__ == "__main__":
    intro()
