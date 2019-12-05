# DreadNought - Readme

[toc]

## Screenshots

| ![](dread7.jpg) | ![](dread2.png) |
| --------------- | --------------- |
| ![](dread3.png) | ![](dread6.png) |

## Introduction

**DreadNought** is a game based upon well-known classic game of **[Battleship](https://en.wikipedia.org/wiki/Battleship)**. In this two-player game you place *ships* of varying lengths onto a grid of 10x10 tiles. In this game each player is not allowed to see the other player's board, instead the players take turns firing *missiles* onto the opponents board and are told if they hit a ship or not. ***The objective of the game*** is to sink all of your opponents ships, at which point you have won. 

## Installing and Running

1. Ensure you have [Python](https://www.python.org/) installed (version `3.4.0` or newer!)

2. Download this repository (zip or clone) from this page

3. Run the launch script

   - **Windows users**: `launch.bat`

      - If you dont have Python on your path, the script will attempt to locate it automatically, note that this can take some time. If it fails to find the executable, please [add it to you path](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path).

   - **Mac OSX and Linux users**: `launch.sh`

      - **Linux users**: Note that this script launches `setup.py` which will attempt to install missing modules for you using Python's pip (namely, `pygame` and `crayons`). If you install Python modules using a different package manager or to a different location, feel free to modify the setup file accordingly **or**:

         ```bash
         cd src
         python3 main.py
         ```
         
### Individual Contributions

#### George Lewis

> I contributed most of what can be found in in the `gui` folder under `src` including the `App` class and `Button` class. Additionally, I am solely responsible for the system used to launch the game, namely: `launch.bat`, `launch.sh`, and `setup.py`. In terms of this document I wrote (with help from Allen) the sections **Introduction** and **Installing and Running**.

#### Allen
> I chose the name for the game. I set up the Github repository on my account, and created the rebrand.ly shortcut to assist with easy installation. I developed and coded all of the AIPlayer class and its methods. I helped discover bugs in the overall running of the game model. I assisted in the creation and and brainstorming of the project plan, design review presentation, final presentation and now the final project repository. I created and organized the outline for the README. I helped write the instructions on how to download and install the game in the README as well as chose the licence for the repository. I added the screenshots to the repository. I outlined in detail the nature of AIPlayer class here in the README and offered it as an example for extension.