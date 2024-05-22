# THE VOID
[The Void Text Adventure Game Link Deployed on Heroku](https://project-3-space-rpg-3626c6806454.herokuapp.com/)
## Table of Contents
- [Introduction](#introduction)
- [Player Experience](#player-experience)
- [Game Flowcharts](#game-flowchart)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Known Issues](#known-issues)
- [Resources](#resources)
- [Credits & Acknowledgements](#credits--acknowledgements)

## Introduction 

Looking at previous examples and having a lifelong interest in storytelling and gaming, I decided to make a text adventure.

**Idea:** A text adventure set in space where you name and create a character and have three encounters while on a spaceship. The game follows standard RPG mechanics such as health, usable items, and dice rolls to do certain actions in the style of Dungeons and Dragons.

I started off with a map of the starting room and three rooms with three connecting corridorsI wanted to combine the lohgic of getting a dice roll to infleuence player outcomes.

## Player Experience

**Map of Game**
![Game Map](https://github.com/donaltwo/project3-space-rpg/assets/155965788/5b180691-6315-49e8-a8b5-b7906bd7bd81)


I like games where there are multiple branches that you can experience to maximize replayability. I like games that allow choice and freedom to explore. I like games that surprise me.

## Game Flowcharts
![Game Logic](https://github.com/donaltwo/project3-space-rpg/assets/155965788/51ade94f-9414-4770-aceb-47abed9cf0f4)

Started out with an initial flowchart of the game design.

## Features

## **Implemenented Features**
**Character Creation:** 

Players can create their own  unique characters with allocated stats. They can choose a name, race, and allocate points to attributes like health, attack, and luck.
Races have different stat bonuses and penalties.

**Room and Inventory Management:** 

Rooms are represented as objects with names, descriptions, and items.
Players can search rooms for items and add them to their inventory.
Inventory management allows adding and removing items, as well as displaying the inventory.

**Combat System:** 
Players can encounter enemies and choose to fight or flee.
Combat involves rolling dice to determine outcomes, adding an element of chance to the battles.

**Game Flow:** 

The game progresses through various rooms and encounters, providing choices for the player at each stage.
The story changes based on the player's decisions, leading to different outcomes and endings.

**User Interaction:** 

The game utilizes user input to navigate through choices and actions.
Input validation ensures that only valid commands are accepted from the player.


**Restart and Quit Functionality:**

Players can restart the game or quit when their character dies by calling the restart_game function.


**Future Features**
-Due to time constarints the stats don't influence the combat there is no battle system I have butil out a stat allocation system but not where it impacts the game. This was a real lesson for me in working backwards first to avoid this outcome.
- Again due to time I also planned to perhaps implement aGoogle sheets API that would record in a table how players game sesssions went.

- 
**ASCII Text Art generated from [Patorjk](https://patorjk.com/):**

![LOGO](https://github.com/donaltwo/project3-space-rpg/assets/155965788/7fe5a3dc-5928-4d1c-8e64-ed5e7d2c9510)

**I decided the best way to make the deciated aspects of the game into classes such as characters rooms, inventory as these I could go back and add further elements with set values .**

![Character Class](https://github.com/donaltwo/project3-space-rpg/assets/155965788/3f11e5ae-f16f-45fa-8200-d800a8ca1535)


**Functions for handling player interactivity with the text adventure**

![Functions](https://github.com/donaltwo/project3-space-rpg/assets/155965788/a501a3f8-0a3d-49a8-9172-389aa65b3071)

**Customer character creation and racial bonus error + error handling logic**

![Character stats racial bonus](https://github.com/donaltwo/project3-space-rpg/assets/155965788/7ab5dea1-9d96-4948-b486-aef490294499)


## Testing

## Testing Table
| Action                           | Input                             | Output                                                                                                    | Pass/Fail |
|----------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `create_player()`                | `Name`                            | Creates a character named by the player.                                                                          | Pass      |
| `choose_race()`                  | `1` (Earthling)                   | Returns race string "Earthling - Human who once lived on Earth. +3 Luck -1 Attack" and choice number 1. | Pass      |
| `choose_race()`                  | `2` (Martian)                     | Returns race string "Martian - Human from the Mars colony +4 Attack -2 Health" and choice number 2.     | Pass      |
| `choose_race()`                  | `3` (Gorbling)                    | Returns race string "Gorbling, Feline aliens from deep space. +3 Luck -3 Attack" and choice number 3.   | Pass      |
| `choose_race()`                  | `4` (Chutuleon)                   | Returns race string "Chutuleon, Tentacled squid-like cosmic terror +5 Attack -5 Luck" and choice number 4.| Pass      |
| `create_character()`             | `Player Name`, `1`, `Health: 4`, `done` | Creates a character named with Player Name with the specified race and health points.                  | Pass      |
| `clear_screen()`                 | None                              | Clears the terminal screen.                                                                              | Pass      |
| `dice_roll()`                    | None                              | Returns a random integer between 1 and 20 simulating a D20 roll.                                         | Pass      |
| `player_input()`                 | `   `                             | Prompts again for input as if user enters only whitespace.                                                          | Pass      |
| `Inventory.add_item()`           | `Laser Gun`                       | Adds "Laser Gun" to the inventory and prints "You found a Laser Gun."                                    | Pass      |
| `Inventory.remove_item()`        | `Laser Gun`                       | Removes "Laser Gun" from the inventory if it exists, prints "You used Laser Gun."                        | Pass      |
| `Inventory.display_inventory()`  | None                              | Displays the items currently in the inventory.                                                            | Pass      |
| `Room.add_item()`                | `Laser Gun`                       | Adds "Laser Gun" to the room's item list.                                                                 | Pass      |
| `intro()`                        | None                              | Displays intro ASCII art and messages, calls `create_character()`.                                         | Pass      |
| `main()`                         | `search`                          | Returns "search".                                                                                         | Pass      |
| `main()`                         | `exit`                            | Returns "exit".                                                                                           | Pass      |
| `main()`                         | `invalid`                         | Prompts again for valid input ("search" or "exit").                                                       | Pass      |
| `direction()`                    | `left`                            | Returns "left".                                                                                           | Pass      |
| `direction()`                    | `straight ahead`                  | Returns "straight ahead".                                                                                 | Pass      |
| `direction()`                    | `right`                           | Returns "right".                                                                                          | Pass      |
| `direction()`                    | `invalid`                         | Prompts again for valid input ("left", "straight ahead", or "right").                                     | Pass      |
| `air_lock_luck_check()`          | `1` (search)                      | Searches the room, rolls a dice, and prints results.                                                      | Pass      |
| `air_lock_luck_check()`          | `2` (inspect panel)               | Prompts user to press a button, processes the input, and prints results.                                   | Pass      |
| `air_lock_luck_check()`          | `3` (exit)                        | Prints "You exit the room."                                                                               | Pass      |
| Fight encounter (fight/flee)     | `fight`                           | Initiates combat, rolls a dice, and prints combat outcome.                                                | Pass      |
| Fight encounter (fight/flee)     | `flee`                            | Attempts to flee, rolls a dice, and prints flee outcome.                                                  | Pass      |
| Interaction (talk/attack/flee)   | `talk`                            | Initiates conversation, rolls a dice, and prints interaction outcome.                                     | Pass      |

## Lighthouse Scoring

![Lighthouse Result](https://github.com/donaltwo/project3-space-rpg/assets/155965788/f08f0e71-def4-40b7-9718-64476ffd7408)

## Code Insitute Python PEP 8 Code Linter Result

![image](https://github.com/donaltwo/project3-space-rpg/assets/155965788/f58256ce-f5bb-4c17-abfd-4b35b742e9eb)

**Results:
All clear, no errors found**


## Deployment

**Heroku Deployment**

- From Heroku Dashboard created new app.
- Named the app Space RPG and selected Europe as region.
- Went to Settings tab.
- Ad key PORT 8000 to config variable.
- Ad python and node.js buildpacks ensuring python buildpack is on top.
- Connected with Github in deploy section.
- Manually deploy the branch by clicking and have it be built with logs deployed game is able to be viewed & played.

## Known Issues
-**Github committs** I frequently do not use descriptive commit messages as I'm changing a typo when or minor fix therefore I have updated run.py commits as well as updated readme commits. Something that has been pointed out in feedback from my mentor and I'll endavour to work on going forward.
- **Feature creep.** This is my main issue with my project is that I came up with mutiple ideas based off more complicated games and not being a game designer or that advanaced a developer it really slowed my progress.
- **Scope.** The scope is too advanced for my skillset I have created elements together to make a deployed python app that handles inputs and logic but ulimately falls short of being a complete narrative game experience. 

## Resources

- [Python Package Index (PyPI)](https://pypi.org/)
- [Code Instiute PEP 8 Heroku APP](https://pep8ci.herokuapp.com/)
- [PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [ASCII Text Art Generator](https://patorjk.com/software/taag/#p=display&f=Small&t=Party)
- [Python Text Adventure Game Tutorial](https://www.makeuseof.com/python-text-adventure-game-create/)
- [Yolkaris Odyssey](https://github.com/patrickhladun/yolkaris-odyssey)
- [Python Text-Based Adventure Game Tutorial Video](https://www.youtube.com/watch?v=pSYeMdIrKQw)

## Credits & Acknowledgements
- Thank you to my mentor Rory Patrick Sherdian for his feedback and engouragement on this project.
