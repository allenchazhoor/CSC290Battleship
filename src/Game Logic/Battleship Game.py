"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for a Battleship Game.
It is responsible for initializing an instance of a Battleship Game and its
supporting methods.
"""
import Board

P1_number_of_hits = 0
P2_number_of_hits = 0

P1_Battle_Plan_Board = Board()
P1_Battle_Field_Board = Board()

P2_Battle_Plan_Board = Board()
P2_Battle_Field_Board = Board()

def get_whos_turn():





def place_ships():



def is_ship_hit():


def is_ship_sunk():



def move_hit() -> Bool:
    """
    Make a move for player
    Update number of hits
    Update Battle_Field_Board

    Return whether the move was successfully made.

    :return: True or False
    """

def is_game_over() -> Bool:
    """
    return whether the game is over or not

    :return: True or False
    """
    return (P1_number_of_hits == 17) or (P2_number_of_hits ==  17)

def get_winner():
    """
    Get the winner of the game

    :return: P1 or P2
    """
    if P1_number_of_hits == 17:
        return P1

    if P2_number_of_hits == 17:
        return P2



