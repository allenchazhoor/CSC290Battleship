from Board import BattlePlan, BattleField, Board


class DreadnoughtController:

    def __init__(self):
        self.player1setup = BattlePlan(Board.P1)
        self.player2setup = BattlePlan(Board.P2)
        self.player1play = BattleField(Board.P1)
        self.player2play = BattleField(Board.P2)
        self.whosTurn = Board.P1  # Player 1 goes first
        self.num_ships = ["S", "D", "B", "C", "P"]

    def get_player(self):
        return self.whosTurn

    def get_board(self, player = None):
        pass

    def move(self, x, y):
        pass

    def fire(self, x, y):
        if self.whosTurn == Board.P1:
            self.player1play.shoot((x, y))
        else:
            self.player2play.shoot((x, y))

    def place_ships(self, x, y):
        if self.whosTurn == Board.P1 and self.num_ships is not None:
            for ship in self.num_ships:
                self.player1setup.place_ship((x, y), ship, 1, 0)

        elif self.whosTurn == Board.P2 and self.num_ships is not None:
            for ship in self.num_ships:
                self.player1setup.place_ship((x, y), ship, 1, 0)

        return None

