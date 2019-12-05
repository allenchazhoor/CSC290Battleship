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
