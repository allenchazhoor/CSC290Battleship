"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for a Battleship Game.
It is responsible for initializing an instance of a Battleship Game and its
supporting methods.
"""
from __future__ import annotations

import Board

# === Private Attributes ===
# Variables to keep track of the game.

_P1_Battle_Plan_Board = Board()
_P1_Battle_Field_Board = Board()

_P2_Battle_Plan_Board = Board()
_P2_Battle_Field_Board = Board()

_whos_turn = Board.P1  # Player One starts


def get_whos_turn():
    """
    Return whose turn it is

    :return: P1 or P2
    """
    return _whos_turn


def place_ship(coord: tuple[int, int], ship: str, dx: int, dy: int) -> bool:
    """
    Place a ship on P1's or P2's Board.
    Return true if ship was placed.

    :param coord: Where to place tip of the ship
    :param ship: the ship that's going to be placed.
    :param dy: direction
    :param dx: direction
    :return: True if ship was successfully placed False otherwise
    """
    if _whos_turn == Board.P1:
        return _P1_Battle_Plan_Board.place_ship(coord, ship, dx, dy)
    else:
        return _P2_Battle_Plan_Board.place_ship(coord, ship, dx, dy)
    # Still need to change method place_ship in Board.py so that
    #  it returns a bool


def is_ship_sunk(board: Board, ship: str) -> bool:
    """
    Return whether ship was sunk

    :param board: The board on which the ship is located: either
    :param ship: The given ship
    :return: True or False
    """
    # Not sure if we need this method - Does the player need to anounce
    #  if his ship was sunk?
    pass


def valid_move(player: str, coord: tuple[int, int]) -> bool:
    """
    Check if coord is a valid move for player: inside the board and player has
    not hit there before (so that player does not hit twice the same place)
    :param player:
    :param coord: move location
    :return: True if valid, false otherwise
    """

    if not _P1_Battle_Field_Board.valid_coordinate(coord): # coord not inside board
        return False

    if player == Board.P1:
        if _P1_Battle_Field_Board.get() != Board.EMPTY:
            return False
        return True

    else:
        if _P2_Battle_Field_Board.get() != Board.EMPTY:
            return False
        return True


def move_hit(player: str, coord: tuple[int, int]) -> bool:
    """

    Coord is a VALID move

    Make a move for player
    Update number of hits
    Update Battle_Field_Board

    Return whether a ship was hit.

    :param coord: Where to hit on opponents Board
    :param player: Player that is hitting: either P1 or P2
    :return: True if a ship was hit, False otherwise
    """
    is_hit = False

    if player == Board.P1:
        if _P2_Battle_Plan_Board.get(coord) != Board.EMPTY:
            _P1_Battle_Field_Board.hit(coord)
            is_hit = True

    if player == Board.P2:
        if _P1_Battle_Plan_Board.get(coord) != Board.EMPTY:
            _P2_Battle_Field_Board.hit(coord)
            is_hit = True

    return is_hit


def is_game_over() -> bool:
    """
    Return whether the game is over or not
    Game is over if all the ships of the opponent were sunk ie, number of hits equals 17

    :return: True or False
    """
    return (_P1_Battle_Field_Board.get_nb_of_hits() == 17) \
                            or (_P2_Battle_Field_Board.get_nb_of_hits() == 17)


def get_winner():
    """
    Return the winner of the game

    :return: P1 or P2
    """
    if _P1_Battle_Field_Board.get_nb_of_hits() == 17:
        return Board.P1

    if _P2_Battle_Field_Board.get_nb_of_hits() == 17:
        return Board.P2



