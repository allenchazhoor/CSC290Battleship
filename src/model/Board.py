"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for the Battleship Board.
It is responsible for initializing an instance of a Battleship Board and its
supporting methods.
"""
from __future__ import annotations


class Board:
    """
    A board for a battleship game
    Super class for BattlePlan and BattleField

    === Private Attributes ===
    _board:
        The 11 by 11 board used for the game
    _player:
        The current player
    _size:
        The size of the board
    """
    # === Class Attributes ===
    # String representation of each unique ship piece on the Board
    SUBMARINE = 'S'  # length 3
    DESTROYER = 'D'  # length 3
    BATTLESHIP = 'B'  # length 4
    CARRIER = 'C'  # length 5
    PATROL_BOAT = 'P'  # length 2
    EMPTY = " "

    P1 = 'P1'
    P2 = 'P2'

    HIT = 'X'
    MISS = 'O'

    def __init__(self, player: str):
        """
        A board is represented as a nested list where the first index is the ROW
        and the second is the COLUMN. A board IS 10X10.

        Player corresponds to which player the board belongs (P1 or P2)
        """
        # creates the 11 by 11 board with coordinates on the sides displayed
        self._board = []
        self._player = player

        # creates the 11 by 11 board with coordinates on the sides displayed
        for i, k in enumerate(range(0, 10)):
            self._board.append([str(k)] + [" "]*10)
        self._board.insert(0, [" "] + ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

        self._size = len(self._board)

    def get(self, coord: tuple[int, int]) -> str:
        """
        Return what is located at given coordinate
        :param coord: coordinates for the board at ROW, COL
        :return: SUBMARINE, DESTROYER, CARRIER, BATTLESHIP, PATROL_BOAT, EMPTY
        """

        return self._board[coord[0]][coord[1]]

    def valid_coordinate(self, coord: tuple[int, int]) -> bool:
        """
        Checks a position and see if it is valid
        :param coord: coordinates for the board at ROW, COL
        :return: true or false
        """
        return coord[0] < self._size and coord[1] < self._size and coord[0] > 0\
               and coord[1] > 0

    def get_board(self) -> list[list[str]]:
        return self._board


class BattlePlan(Board):

    """
    A board that stores where the ships are located

    """

    def __init__(self, player):

        """
        Initialize the board
        """

        Board.__init__(self, player)

    @staticmethod
    def get_ship_size(ship: str) -> int:
        """
        Returns the size of each unique ships' string representation
        """
        if ship == Board.SUBMARINE:
            return 3
        if ship == Board.DESTROYER:
            return 3
        if ship == Board.BATTLESHIP:
            return 4
        if ship == Board.CARRIER:
            return 5
        if ship == Board.PATROL_BOAT:
            return 2
        else:
            return 0

    def can_place(self, coord: tuple[int, int], ship: str, dx: int, dy: int) -> bool:
        """
        Sees if you can place the ship in that coordinate in a specific direction

        """
        row, col = coord

        # checks each position up until the ships size and sees if the
        #  coordinate is a valid placement
        while self._size < self.get_ship_size(ship) and\
                self.valid_coordinate(coord) and self.get(coord) != self.EMPTY:
            row += dx
            col += dy

        return self.valid_coordinate(coord) and self.get(coord) != self.EMPTY
        # If the loop ends the you can't place it if the current
        # coordinate is either invalid or not EMPTY

    def place_ship(self, coord: tuple[int, int], ship: str, dx: int, dy: int)\
            -> bool:
        """
        Modifies the board by placing the ship onto the original board
        Returns True if the ship was successfully placed. False otherwise.
        """

        row, col = coord
        size = 0
        while size < self.get_ship_size(ship):
            if not self.can_place(coord, ship, dx, dy):
                return False
            self.get_board()[row][col] = ship
            row += dx
            col += dy
            size += 1

        return True


class BattleField(Board):
    """
    A board that stores where the player shot and how many hits the player has

    """

    def __init__(self, player, _number_of_hits):
        """
        Initialize the board

        """

        Board.__init__(self, player)
        self._number_of_hits = 0

        #  self.battle_plan = Battle_Plan

    def hit(self, coord: tuple[int, int]):
        """
        Modifies the board to display whether it was a hit ("x") or miss ("O").
        Also updates number of hits.

        :param coord: Takes in an x and y coordinate
        :return: None
        """
        row, col = coord
        if self.valid_coordinate(coord) and self.get(coord) != Board.EMPTY:
            self.get_board()[row][col] = Board.HIT
            self._number_of_hits += 1

        self.get_board()[row][col] = Board.MISS

    def get_nb_of_hits(self):
        """
        Return the number of hits recorded

        :return: Number of hits
        """
        return self._number_of_hits




