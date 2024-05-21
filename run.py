# Imported Python libraries for random integers for dice rolls

import os
import random
import time

# Intro Message ASCII Art

INTRO_ART = r"""
 _____ _   _  _____   _   _  _____ ___________
|_   _| | | ||  ___| | | | ||  _  |_   _|  _ \
  | | | |_| || |__   | | | || | | | | | | | | |
  | | |  _  ||  __|  | | | || | | | | | | | | |
  | | | | | || |___  \ \_/ /\ \_/ /_| |_| |/ /
  \_/ \_| |_/\____/   \___/  \___/ \___/|___/

"""


class Character:
    """Represents a character in the game."""

    def __init__(self, name, race, health, attack, luck):
        """
        Initializes a character with the given attributes.

        Args:
            name (str): The name of the character.
            race (str): The race of the character.
            health (int): The health points of the character.
            attack (int): The attack points of the character.
            luck (int): The luck points of the character.
        """
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.luck = luck

    def display_stats(self):
        """Display the stats of the character."""
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Luck: {self.luck}")


class Inventory:
    """Represents the inventory of a character."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.items = []

    def add_item(self, item):
        """Adds an item to the inventory."""
        self.items.append(item)
        print(f"You found a {item}.")

    def remove_item(self, item):
        """Removes an item from the inventory."""
        if item in self.items:
            self.items.remove(item)
            print(f"You used {item}.")
        else:
            print(f"You don't have {item} in your inventory.")

    def display_inventory(self):
        """Displays the items in the inventory."""
        if self.items:
            print("Inventory:")
            for item in self.items:
                print("-", item)
        else:
            print("Your inventory is empty.")


class Room:
    """Represents a room in the game."""

    def __init__(self, name, description):
        """
        Initializes a room with the given name and description.

        Args:
            name (str): The name of the room.
            description (str): The description of the room.
        """
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        """Adds an item to the room."""
        self.items.append(item)


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def dice_roll():
    """Simulates rolling a D20 dice."""
    return random.randint(1, 20)


def player_input(prompt):
    """Gets input from the player with whitespace handling."""
    while True:
        user_input = input(prompt).strip()
        if user_input and not user_input.isspace():
            return user_input
        else:
            print("You have not entered any text characters! Try again.")


def create_player():
    """Creates a player by asking for their name."""
    name = player_input("Name your character: ")
    return name


def choose_race():
    """
    Function to allow the player to choose their race.
    """
    race_options = [
        "Earthling - Human who once lived on Earth. +3 Luck -1 Attack",
        "Martian - Human from the Mars colony +4 Attack -2 Health",
        "Gorbling, Feline aliens from deep space. +3 Luck -3 Attack",
        "Chutuleon, Tentacled squid-like cosmic terror +5 Attack -5 Luck",
    ]
    print("Select your race:")
    for i, race in enumerate(race_options, 1):
        print(f"{i}. {race}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(race_options):
                return race_options[choice - 1], choice
            else:
                print("Invalid choice. Please enter a number to pick a race.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def create_character():
    """
    Function to create a character with allocated stats.
    """
    print("Stat Allocation. Give your character additional points.")
    available_points = 10
    attributes = {"Health": 5, "Attack": 3, "Luck": 2}

    name = create_player()
    race_str, race_choice = choose_race()

    # Stat bonuses for attributes based on race choice

    if race_choice == 1:  # Earthling
        attributes["Luck"] += 3
        attributes["Attack"] -= 1
    elif race_choice == 2:  # Martian
        attributes["Attack"] += 4
        attributes["Health"] -= 2
    elif race_choice == 3:  # Gorbling
        attributes["Luck"] += 3
        attributes["Attack"] -= 3
    elif race_choice == 4:  # Chutuleon
        attributes["Attack"] += 5
        attributes["Luck"] -= 5
    while available_points > 0:
        print(f"\nPoints Remaining: {available_points}")
        print("Allocate points to attributes:")
        for attribute in attributes:
            print(f"{attribute}: {attributes[attribute]}")
        attribute_choice = input(
            "Enter attribute to allocate points (or 'done' to finish): "
        ).capitalize()

        if attribute_choice == "Done":
            break
        if attribute_choice not in attributes:
            print("Invalid attribute. Type Health, Attack, or Luck.")
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
    player = Character(
        name, race_str, attributes["Health"],
        attributes["Attack"], attributes["Luck"]
    )
    print(f"\n{player.name})
    print("Health:{player.health} ,Attack:{player.attack}, Luck:{player.luck}")


def intro():
    """
    Function to display the introduction and game instructions.
    """
    print(INTRO_ART)
    print("Welcome to a text adventure Space RPG The Void!")
    print("You will find items, encounter enemies and roll a 20-sided dice")
    print("Like classic games such as Dungeons & Dragons")

    """
    Function to display the introduction and game instructions.
    """
    print(INTRO_ART)
    print("Welcome to a text adventure Space RPG The Void!")
    print("You will find items, encounter enemies and explore!")
    print("Roll a dice for outcomes like in Dungeons & Dragons!")
    print("Please create your own unique character for this story")
    print("Good luck out there spacefarer!")
    print("You have various words to help you navigate this adventure.")
    print("Please check for typos before entering your commands.")
    print("Search - search the area for items")
    print("Exit - leave the current area")
    print("Talk - speak to another character")
    print("Attack - enter into combat with the character")
    time.sleep(3)
    create_character()


intro()

# Creating rooms and managing them all


def create_room():
    rooms = []

    # Adding rooms to the map

    rooms.append(
        Room("Supply Closet", "A small closet with cleaning supplies.")
    )
    rooms.append(
        Room(
            "Air Lock",
            "A chamber with a door that opens to the crushing void of space.",
        )
    )
    rooms.append(
        Room(
            "Escape Pod",
            "A small pod for emergency escape, your only hope for survival.",
        )
    )
    rooms.append(
        Room("Crew Quarters", "Abandoned living quarters for crew members.")
    )

    # Adding items to individual rooms

    rooms[0].add_item("Laser Gun")
    rooms[0].add_item("Security Badge Pass")
    rooms[1].add_item("Air Lock Control Panel")
    rooms[1].add_item("Air Lock Control Manual")
    rooms[2].add_item("Escape Pod Controls")

    return rooms


# Combat system for when players encounter enemies


def fight(self, enemy):
    print(f"{self.name} damages {enemy.name}!")
    enemy.health -= self.attack
    print(f"{enemy.name} has {enemy.health} health left.")


def flee(self):
    if dice_roll() <= 10:
        print(f"{self.name} successfully flees from the enemy!")
        return True
    else:
        print(f"{self.name} fails to flee from the enemy!")
        return False


# Character list of encounter non-playable characters

alien = Character("Bounty Hunter", "Chutuleon", 20, 15, 0)
sam = Character("Sam", "Human", 15, 10, 0)

# Start Game

print("Your eyes adjust as you open them to a dim room of cleaning supplies.")
print("Blinking, you wince in pain as you touch your forehead.")
print("Looking at your hand, you can see drying blood.")
print("How did I get here...? Why am I not able to remember where I am?")
print("Search the room?")

# Prompt user for choice to search room or exit


def main():
    while True:
        choice = input(
            "Please choose what to do: search or exit the supply closet: "
        ).lower()
        if choice in ["search", "exit"]:
            return choice
        else:
            print("Invalid command. Please type 'search' or 'exit'.")


if __name__ == "__main__":
    answer = main()

    if answer == "search":
        print("You begin to rummage through the room.")
        # Dice roll to search room

        result = dice_roll()
        print("You rolled a:", result)
        if result >= 10:
            print("You find a Laser Gun!")
        else:
            print("Nothing of use was found.")
    elif answer == "exit":
        print("You exit the supply closet.")
        # More game logic for exiting the room and encountering enemies
    if answer == "search":
        print("You begin to rummage through the room")
        # Dice roll to search room

        result = dice_roll()
        print("You rolled a:", result)

        if result >= 9:
            # PASS
            print("You find a laser gun with 2 ammo left.")
            print("You also get a badge pass and exit the room.")
        else:
            # FAIL

            print("You find nothing, frustrated, you exit the room")
    elif answer == "exit":
        print("You leave the room without searching")
    else:
        print("Please select a valid option.")

# Dice roll function


def dice_roll():
    return random.randint(1, 20)


# Character route selection: 3 corridors
    print("You see three corridors ahead of you:")
    print("One to your left, straight ahead, and one to your right.")
    print("Which path will you take?")


def direction():
    while True:
        player_input = input(
            "Please choose which way to go: left, straight ahead, or right: "
        ).lower()
        if player_input in ["left", "straight ahead", "right"]:
            return player_input
        else:
            print("Invalid direction, type left, right, or straight.")


# Call the direction function to get user choice

chosen_direction = direction()

# Use the chosen direction

if chosen_direction == "right":
    print("You decide to proceed by going down the right corridor.")

    def air_lock_luck_check(character):
        print("You arrive at a door with an Air Lock sign.")
        print("You enter, exploring further.")
        print("You notice the sign 'Air Lock' and see three buttons.")
        print("They're colored red, yellow, and green on a control panel.")
        print("\nWhat do you choose to do?")
        print("1. Search the room.")
        print("2. Inspect the control panel.")
        print("3. Exit the room.")

        action = input("Enter your choice (1, 2, 3): ")
        if action == "1":
            print("You begin to look around the room.")
            result = dice_roll()
            print("You rolled a:", result)
            if result <= 5:
                print("You find nothing.")
            elif result >= 6:
                print("You find an air lock manual.")
                print("You decide to read the manual.")
                print("Green - Open Lock")
                print("Yellow - Timed Open for 15 seconds Lock")
                print("Red - Close Lock")
        elif action == "2":
            print("You see the three buttons.")
            print("\nWhich button will you press?")
            print("1. Press the red button.")
            print("2. Press the yellow button.")
            print("3. Press the green button.")
            print("4. Press none of the buttons.")
            button_choice = (
                input("Enter your choice (red, yellow, green, none): ")
                .strip().lower()
            )
            if button_choice not in ["red", "yellow", "green", "none"]:
                print(
                    "Invalid choice! Choose red, yellow, green, or none."
                )
            elif button_choice == "red":
                print("The air lock makes a loud hum.")
                print("'Air lock status sealed,'")
                print("A ship system echoes the update in a flat tone.")
            elif button_choice == "yellow":
                print("'Timed air lock sequence initiated.'")
                print("You freeze as you see the air lock lights flash.")
                print("You need to get out of here now!")
                if character.luck >= 9:
                    print("You snap back to reality from your fear paralysis.")
                    print("You throw yourself through the door.")
                    print("Back into the corridor.")
                    print("The door seals itself as the air lock activates.")
                    print("Panting, you pick yourself up.")
                    print("You walk back towards the supply closet.")
                    print("Time to pick a different path.")
            elif button_choice == "green":
                print("You hit the green button.")
                print("Air lock opening.")
                print("Your eyes bulge in dread.")
                print("The last thing you ever experience is implosion.")
                print("You are dead.")
                print("Restart or quit?")
            else:
                pass
        elif action == "3":
            print("You exit the room.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

elif chosen_direction == "left":
    print("You decide to proceed by going down the left corridor.")
    print("You find some blood streaks on the walls and ground but no bodies.")
    print("You pick up your walking pace as panic creeps in.")
    print("Sprinting, you run to the door at the end of the corridor.")
else:
    print("You decide to proceed straight ahead.")
# Hallway encounter with an alien bounty hunter if you decide to(Crew Quarters)

print("You exit the supply closet and step into a hallway.")
print("You notice you're on a spaceship.")
print("You also notice you're not alone!")
print("A tall blue alien bounty hunter is 10 feet away.")
print("You start to panic and need to make a decision quickly.")

# Prompt user for choice to fight alien or to flee

answer = input("Enter 'fight' or 'flee': ").lower()

if answer == "fight":
    print("You lunge at the alien, knocking them back.")
    print("You bothstart grappling on the ground.")
    print("You struggle as it attempts to push you off.")

    # Roll the dice again to determine fight outcome

    result = dice_roll()
    print("You rolled a:", result)
    if result >= 11:
        print("You headbutt the alien, stunning it and making it motionless.")
        print("You pick yourself up and start running.")
    else:
        print("You feebly struggle with the alien.")
        print("Your strength weakens and you feel blinding pain in your neck.")
        print("The alien eviscerates you.")
        print("You are dead.")
        print("Play again? Select restart or quit.")
        answer = input("Restart or quit game? ").lower()
        if answer == "restart":
            # Restart the game

            pass
        elif answer == "quit":
            print("Thanks for playing. Better luck next time!")
elif answer == "flee":
    print("You try to escape from the alien.")
    result = dice_roll()
    print("You rolled a:", result)
    if result <= 10:
        print("You try to escape but fail.")
        print("The alien catches you and you feel blinding pain in your neck.")
        print("You are dead.")
        print("Play again? Select restart or quit.")
        answer = input("Restart or quit game? ").lower()
    else:
        print("You manage to escape from the alien.")
        print("You run back to the supply closet.")
# Advantage to roll outcome if you have a laser gun object

print("You detangle yourself from the alien suddenly.")
print("Being back on your feet, you point your gun at the alien's face.")
print("You pull the trigger!")
print("The laser melts the alien's face into a sizzling pool of blue liquid.")

# Straight ahead to Escape Pod

print("You proceed straight ahead.")
print("There's an eerie quiet as the lights flicker on the ship.")
print("You notice another figure slumped against a wall, panting heavily.")
print("'Stop!' the figure exclaims.")
print("You notice a beam of a laser rifle hover in front of your vision.")

# Prompt user for choice to talk to, attack the figure, or run away

answer = input("Choose 'talk', 'attack', or 'flee': ").lower()

if answer == "talk":
    print("You tell the figure that you mean them no harm.")
    result = dice_roll()
    print("You rolled a:", result)
    if result <= 10:  # FAIL TALK CHECK
        print("You start to try and negotiate but it's hopeless.")
        print("The last thing you hear is the laser shot exploding.")
        print("You have failed to escape the ship and it's now your grave.")
        print("You are dead.")
        print("Try again? Select restart or quit.")
        answer = input("Restart or quit game? ").lower()
    else:  # PASS TALK CHECK
        print("The figure hesitates, lowering their weapon.")
        print("You slowly approach each other.")
        print("'You're on the crew!'")
        print("You see that this is a fellow crew member.")
        print("She is bleeding from her side, panting.")
        print("'I'm Sam, don't think we've met.' She salutes you.")
        print("'We need a security badge to get the hell outta here!")
        print("'You don't have one, do you?'")
        # Check if badge pass is in user inventory

        if "Security Badge Pass" in Inventory:
            print("Oh thank god you do")
            print("You hand over the badge pass")
            print("You and same escape to the planet Lur")
            print("You have survived!")
        else:
            print("You do not have the badge pass")
            print("Sams eyes bulge in rage.")
            print("you hear a sickening crack as the ship explodes.")
            print("You are dead. And liquid.")
            print("Play again? Select restart or quit.")
            answer = input("Restart or quit game? ").lower()
elif answer == "attack":  # COMBAT CHECK
    print("You lunge at your assailant.")
    result = dice_roll()
    print("You rolled a:", result)
elif answer == "flee":  # ESCAPE CHECK
    print("You turn on your heel and begin to try and run away.")
    result = dice_roll()
    print("You rolled a:", result)
    if result <= 7:  # FAIL FLEE CHECK
        print("You try to escape but fail.")
        print("'Pathetic,' are the last words you hear as your vision dims.")
        print("You are dead.")
        print("Play again? Select restart or quit.")
        answer = input("Restart or quit game? ").lower()
    else:  # PASS FLEE CHECK
        print("Your legs pump as you hear the figure shouting at you.")
        print("A shot is fired, hitting the ceiling.")
        print("You have survived for now.")
