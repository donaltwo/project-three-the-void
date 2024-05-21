# The VOID

## Table of Contents
- [Introduction](#introduction)
- [Player Experience](#player-experience)
- [Game Flowcharts](#game-flowchart)
- [How to Play](#how-to-play)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Known Issues](#known-issues)
- [Resources](#resources)
- [Credits & Acknowledgements](#credits--acknowledgements)

## Introduction 

Looking at previous examples and having a lifelong interest in storytelling and gaming, I decided to make a text adventure.

**Idea:** A text adventure set in space where you name and create a character and have three encounters while on a spaceship. The game follows standard RPG mechanics such as health, usable items, and dice rolls to do certain actions in the style of Dungeons and Dragons.

I started off with a map of the starting room and three rooms with three connecting corridors.

## Player Experience

**Map of Game**
![Game Map](https://github.com/donaltwo/project3-space-rpg/assets/155965788/5b180691-6315-49e8-a8b5-b7906bd7bd81)

I like games where there are multiple branches that you can experience to maximize replayability. I like games that allow choice and freedom to explore. I like games that surprise me.

## Game Flowcharts
![Game Logic](https://github.com/donaltwo/project3-space-rpg/assets/155965788/51ade94f-9414-4770-aceb-47abed9cf0f4)

Started out with an initial flowchart of the game design.

## Features

**ASCII Text Art generated from [Patorjk](https://patorjk.com/):**
![LOGO](https://github.com/donaltwo/project3-space-rpg/assets/155965788/7fe5a3dc-5928-4d1c-8e64-ed5e7d2c9510)

**I decided the best way to make the deciated aspects of the game into classes.**
![Character Class](https://github.com/donaltwo/project3-space-rpg/assets/155965788/3f11e5ae-f16f-45fa-8200-d800a8ca1535)


**Functions for handling palyer interactivity with the text adventure**
![Functions](https://github.com/donaltwo/project3-space-rpg/assets/155965788/a501a3f8-0a3d-49a8-9172-389aa65b3071)

**Customer character creation and racial bonus error + error handling logic**
![Character stats racial bonus](https://github.com/donaltwo/project3-space-rpg/assets/155965788/7ab5dea1-9d96-4948-b486-aef490294499)


## Testing

## Lighthouse Scoring
![Lighthouse Result](https://github.com/donaltwo/project3-space-rpg/assets/155965788/f08f0e71-def4-40b7-9718-64476ffd7408)

## Code Insitute Python PEP 8 Code Linter Result 
![image](https://github.com/donaltwo/project3-space-rpg/assets/155965788/f58256ce-f5bb-4c17-abfd-4b35b742e9eb)

Results:
All clear, no errors found


## Deployment
**Heroku Deployment**

- From Heroku Dashboard created new app.
- Named the app Space RPG and selected Europe as region.
- Went to Settings tab.
- Added key PORT 8000 to config variable.
- Added python and node.js buildpacks ensuring python buildpack is on top.
- Connected with Github in deploy section.
- Manually deploy the branch by clicking and have it be built with logs deployed game is able to be viewed & played.

## Known issues
- Feature creep. This is my main issue with my project is that I came up with mutiple ideas based off more complicated games and not being a game designer or that advanaced a developer it really slwoed my progress.
- Scope. The scope is too advanced for my skillset I have created elements tofgeter to make a deployed python app that handles inputs and logic but ulimately falls short of being a complete game experience. 


## Resources

- [Python Package Index (PyPI)](https://pypi.org/)
- [Code Instiute PEP 8 Heroku APP](https://pep8ci.herokuapp.com/)
- [PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [ASCII Text Art Generator](https://patorjk.com/software/taag/#p=display&f=Small&t=Party)
- [Python Text Adventure Game Tutorial](https://www.makeuseof.com/python-text-adventure-game-create/)
- [Yolkaris Odyssey](https://github.com/patrickhladun/yolkaris-odyssey)
- [Python Text-Based Adventure Game Tutorial Video](https://www.youtube.com/watch?v=pSYeMdIrKQw)

## Credits & Acknowledgements
- Thank you to my mentor Rory Patrick Sherdian for his feedback and advice on this project.
