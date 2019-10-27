"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module contains the main program code for the Battleship Board.
It is responsible for initializing an instance of a Battleship Board and its
supporting methods.
"""


class Board:
    """
    A board for a battleship game
    Super class for BattlePlan and BattleField

    """
    SUBMARINE = 'S'  # length 3
    DESTROYER = 'D'  # length 3
    BATTLESHIP = 'B'  # length 4
    CARRIER = 'C'  # length 5
    PATROL_BOAT = 'P'  # length 2
    EMPTY = ''

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

        self.board = []
        self.player = player

        for i in range(10):
            self.board.append([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,EMPTY, EMPTY, EMPTY,])

    def get(self, coord: tuple[int, int]) -> str:
        """
        Return what is located at given coordinate
        :param coord: coordinates for the board at ROW, COL
        :return: SUBMARINE, DESTROYER, CARRIER, BATTLESHIP, PATROL_BOAT, EMPTY
        """
        row, col = coord

        return self.board[row][col]


def valid_coordinate(coord: tuple[int, int]) -> bool:
    row, col = coord

    if row > 9 or col > 9 or row < 0 or col < 0:
        return False
    else:
        return True


class BattlePlan(Board):

    """
    A board that stores where the ships are located

    """

    def __init__(self):

        """
        Initialize the board
        """

        Board.__init__(self, player)

    def place_ship(self, coord: tuple[int, int], ship: str, direction: str, lenght: int):

        row, col = coord

        possible_row = row
        possible_col = col
        while self.board[row][col] == EMPTY and self.valid_coordinate((possible_row, possible_col)):



class BattleField(Board):
    """
    A board that stores where the player shot

    """

    def __init__(self):
        """
        Initialize the board

        """

        Board.__init__(self, player)
        #self.battle_plan = Battle_Plan

    def hit(self, coord: tuple[int, int]):
        """

        :param coord:
        :return:
        """
        row, col = coord
        if self.valid_coordinate(coord):
            self.board[row][col] = X

    def miss(self, coord: tuple[int, int]):
        """

        :param coord:
        :return:
        """
        row, col = coord
        if self.valid_coordinate(coord):
            self.board[row][col] = O
