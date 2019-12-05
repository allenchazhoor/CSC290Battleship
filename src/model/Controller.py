"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for a Battleship Game.
It is responsible for initializing an instance of a Battleship Game and its
supporting methods.
"""
from __future__ import annotations

from model.Board import Board, BattleField, BattlePlan


class Controller:

    """
    Class controller. Plays a battleship game with official battleship rules
    between 2 human players. Used by GUI.

    === Private Attributes === # Variables to keep track of the game.

    _P1_Battle_Plan_Board: P1's ship locations
    _P1_Battle_Field_Board: P1's hits and misses

    _P2_Battle_Plan_Board: P2's ship locations
    _P2_Battle_Field_Board P2's hits and misses

    _whos_turn: who plays next

    """

    def __init__(self):
        """
        Initializes the controller with the appropriate boards for each player.

        """

        self._P1_Battle_Plan_Board = Board(Board.P1)
        self._P1_Battle_Field_Board = Board(Board.P1)

        self._P2_Battle_Plan_Board = Board(Board.P2)
        self._P2_Battle_Field_Board = Board(Board.P2)

        self._whos_turn = Board.P1  # Player One starts

    def get_whos_turn(self):
        """
        Return whose turn it is

        :return: P1 or P2
        """
        return self._whos_turn

    def place_ship(self, start: tuple[int, int], end: tuple[int, int],
                   ship: str) -> bool:
        """
        Place a ship on P1's or P2's Board.
        Return true if ship was placed.


        :param start: coordinate of the first piece of the ship
        :param end: coordinate of the last piece of the ship
        :param ship: the ship that's going to be placed.

        :return: True if ship was successfully placed False otherwise
        """
        dx = 0
        dy = 0
        diff = 0

        if start[0] == end[0]:
            diff = abs(end[1] - start[1])
            if end[1] > start[1]:
                dy = 1

            else:
                dy = -1

        if start[1] == end[1]:
            diff = abs(end[0] - start[0])
            dy = 0
            if end[0] > start[0]:
                dx = 1
            else:
                dx = -1

        if (dx == 0 and dy == 0) or (diff != BattlePlan.get_ship_size(ship)):
            return False

        if self._whos_turn == Board.P1:
            return self._P1_Battle_Plan_Board.place_ship(start, ship, dx, dy)
        else:
            return self._P2_Battle_Plan_Board.place_ship(start, ship, dx, dy)

    def valid_move(self, player: str, coord: tuple[int, int]) -> bool:
        """
        Check if coord is a valid move for player: inside the board and player
        has not hit there before (so that player does not hit twice the same
        place).
        :param player:
        :param coord: move location
        :return: True if valid, false otherwise
        """

        if not self._P1_Battle_Field_Board.valid_coordinate(coord):
            return False    # coord not inside board

        if player == Board.P1:
            if self._P1_Battle_Field_Board.get() != Board.EMPTY:
                return False
            return True

        else:
            if self._P2_Battle_Field_Board.get() != Board.EMPTY:
                return False
            return True

    def move_hit(self, player: str, coord: tuple[int, int]) -> bool:
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
            if self._P2_Battle_Plan_Board.get(coord) != Board.EMPTY:
                self._P1_Battle_Field_Board.hit(coord)
                is_hit = True

        if player == Board.P2:
            if self._P1_Battle_Plan_Board.get(coord) != Board.EMPTY:
                self._P2_Battle_Field_Board.hit(coord)
                is_hit = True

        return is_hit

    def is_game_over(self) -> bool:
        """
        Return whether the game is over or not
        Game is over if all the ships of the opponent were sunk ie, number
        of hits equals 17

        :return: True or False
        """
        return (self._P1_Battle_Field_Board.get_nb_of_hits() == 17) or\
               (self._P2_Battle_Field_Board.get_nb_of_hits() == 17)

    def get_winner(self):
        """
        Return the winner of the game

        :return: P1 or P2
        """
        if self._P1_Battle_Field_Board.get_nb_of_hits() == 17:
            return Board.P1

        if self._P2_Battle_Field_Board.get_nb_of_hits() == 17:
            return Board.P2



