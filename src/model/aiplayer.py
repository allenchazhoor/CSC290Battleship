"""CSC290 Project: Battleship - Dreadnought


=== Module Description ===
This module is the currently unattached AI Player of the game. It is designed to
provide an outline for a game specific
implementation of an automated opponent for the human player.
"""
from random import random


class AIPlayer:

    def __init__(self, board) -> None:
        """
        Initialize AIPlayer with the beginning state attributes
        :param board: Board Object we are playing on
        """
        # list of possible coordinates to attack, initialized to everything
        self.poss_moves = []
        for i in range(10):
            for j in range(10):
                self.poss_moves.append((i, j))

        # list of plausible hits
        self.poss_hits = []

        # list of missed coordinates
        self.misses = []

        # list of known hits
        self.hits = []

        # ship health is 17 (5+4+3+3+2)
        self.health = 17

        # AIPlayer's ship's coordinates
        self.ship_coords = []

        # AIPlayer's board to play on
        self.board = board

        # AIPlayer is alive
        self.alive = True

        # We will make AIPlayer to be player 2
        self.name = 'P2'

    def move(self)->(int, int):
        """
        return a random co-ordinate if no plausible hits are found, or return
        the first plausible hit in possHits
        :return: Co-ordinates to attack in tuple form or (-1, -1) to indicate
        no valid moves, therefore game over
        """
        if self.poss_moves is []:
            return -1, -1
        if self.poss_hits is []:
            x = -1
            y = -1
            while (x, y) not in self.poss_moves:
                x = random.randint(9)
                y = random.randint(9)
            self.poss_moves.remove((x, y))
            return x, y
        else:
            m = self.poss_hits[0]
            self.poss_moves.remove(m)
            self.poss_hits.remove(m)
            return m

    def hurt(self, x, y) ->None:
        """
        remove hit ship co-ordinates from remaining ships and decrease life
        :param x: x-coordinate of own hit ship
        :param y: y-coordinate of own hit ship
        """
        self.health -= 1
        self.ship_coords.remove((x, y))
        if self.health == 0:
            self.alive = False

    def hit(self, x, y) -> None:
        """
        add hit coordinates to known ship hits
        look for plausible hits surrounding x,y
        :param x: x-coordinate of other player's hit ship
        :param y: y-coordinate of other player's hit ship
        """
        self.hits.append((x, y))
        if (x, y + 1) in self.poss_moves:
            self.poss_hits.append((x, y + 1))
        if (x, y - 1) in self.poss_moves:
            self.poss_hits.append((x, y - 1))
        if (x + 1, y) in self.poss_moves:
            self.poss_hits.append((x + 1, y))
        if (x - 1, y) in self.poss_moves:
            self.poss_hits.append((x - 1, y))

    def miss(self, x, y) -> None:
        """
        add x,y to missed coordinates
        :param x: x-coordinate of own miss
        :param y: y-coordinate of own miss
        """
        self.misses.append((x, y))
