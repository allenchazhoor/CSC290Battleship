"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for a Battleship Game.
It is responsible for initializing an instance of a Battleship Game and its
supporting methods.
"""
import Board

# === Private Attributes ===
# Variables to keep track of the game.
_P1_number_of_hits = 0
_P2_number_of_hits = 0

_P1_Battle_Plan_Board = Board()
_P1_Battle_Field_Board = Board()

_P2_Battle_Plan_Board = Board()
_P2_Battle_Field_Board = Board()

_whosturn = Board.P1 # Player One starts

def get_whos_turn():
    """
    Return whose turn it is
    
    :return: P1 or P2
    """
    return _whosturn

def place_ship(coord: tuple[int, int], ship: str, dx: int, dy: int) -> Bool:
    """
    Place a ship on P1's or P2's Board.
    Return true if ship was placed.

    :param coord: Where to place tip of the ship
    :param ship: the ship that's going to be placed.
    :param dx, dy: direction
    :return: True if ship was successfully placed False otherwise
    """
    if _whosturn == Board.P1:
        return _P1_Battle_Plan_Board.place_ship(coord, ship, dx, dy)
    else:
        return _P2_Battle_Plan_Board.place_ship(coord, ship, dx, dy)
    # Still need to change method place_ship in Board.py so that it returns a bool
    
def is_ship_sunk(board: Board, ship: str) -> bool:
    """
    Return whether ship was sunk

    :param board: The board on which the ship is located: either
    :param ship: The given ship
    :return: True or False
    """
    # Not sure if we need this method - Does the player need to anounce if his ship was sunk.
    

def move_hit(player: str, coord: tuple[int, int]) -> Bool:
    """
    Make a move for player
    Update number of hits
    Update Battle_Field_Board

    Return whether a ship was hit.
    
    :param coord: Where to hit on opponents Board
    :param coord: Player that is hitting: either P1 or P2
    :return: True or False
    """

def is_game_over() -> Bool:
    """
    Return whether the game is over or not
    Game is over if all the ships of the opponent were sunk ie, number of hits equals 17

    :return: True or False
    """
    return (P1_number_of_hits == 17) or (P2_number_of_hits ==  17)

def get_winner():
    """
    Return the winner of the game

    :return: P1 or P2
    """
    if P1_number_of_hits == 17:
        return Board.P1

    if P2_number_of_hits == 17:
        return Board.P2



