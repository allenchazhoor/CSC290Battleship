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

        self._board = []
        self._player = player
        
        # creates the 11 by 11 board with coordinates on the sides displayed 
        for i, k in enumerate(range(0, 10)):   
            self.board.append([str(k)] + [" "]*10)
        self.board.insert(0, [" "] + ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
        
        self._size = len(self.board) 

    def get(self, coord: tuple[int, int]) -> str:
        """
        Return what is located at given coordinate
        :param coord: coordinates for the board at ROW, COL
        :return: SUBMARINE, DESTROYER, CARRIER, BATTLESHIP, PATROL_BOAT, EMPTY
        """
  
        return self.board[coord[0]][coord[1]]


    def valid_coordinate(coord: tuple[int, int]) -> bool:
        """
        Checks a position and see if it is valid 
        :param coord: coordinates for the board at ROW, COL
        :return: true or false 
        """
        return coord[0] < self.size and coord[1] < self.size and coord[0] > 0 and coord[1] > 0 


class BattlePlan(Board):

    """
    A board that stores where the ships are located

    """

    def __init__(self):

        """
        Initialize the board
        """

        Board.__init__(self, player)
    
    
    def get_ship_size(ship:str) -> int: 
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
        Modifies the board to display whether it was a hit ("x") or miss ("O")
        
        :param coord: Takes in an x and y coordinate 
        :return: None 
        """
        row, col = coord
        if self.valid_coordinate(coord) and Board.get((row,col)) != Board.EMPTY:
            self.board[row][col] = Board.HIT
            
        if self.valid_coordinate(coord) and Board.get((row,col)) == Board.EMPTY:
            self.board[row][col] = Board.MISS
         
   
