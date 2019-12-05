import pygame
import gui.app
import crayons
from enum import Enum


class GuiBoard:

    class Player(Enum):
        p1 = 0,
        p2 = 1

    instance = None

    rows = 10
    cols = 10

    line_thickness = 5

    x = 100
    y = 150

    width = 800
    height = 800

    disabled = False

    placing_ships = True

    active_player = Player.p1

    ships_list = 'SDBCP'

    ships_index = 0

    ships = []

    def __init__(self):
        if GuiBoard.instance:
            raise Exception

        GuiBoard.letters = [(let,
                             gui.app.App.board_font.render(let,
                                                           True,
                                                           (0, 0, 0)))
                            for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

        GuiBoard.nums = [(n, gui.app.App.board_font.render(n, True, (0, 0, 0)))
                         for n in list("123456789") + ['10', '11']]

    def init():
        GuiBoard.instance = GuiBoard()

    def square_coords(row, col):

        drow = GuiBoard.height / GuiBoard.rows
        dcol = GuiBoard.height / GuiBoard.cols

        return (GuiBoard.x + row * dcol + GuiBoard.line_thickness, GuiBoard.y +
                col * drow + GuiBoard.line_thickness, dcol -
                GuiBoard.line_thickness, drow - GuiBoard.line_thickness)

    def render(self):

        drow = GuiBoard.height / GuiBoard.rows
        dcol = GuiBoard.height / GuiBoard.cols

        for r in range(GuiBoard.rows + 1):

            if r == GuiBoard.rows:
                pygame.draw.rect(gui.app.App.instance.screen,
                                 (0, 0, 0), (GuiBoard.x,
                                             GuiBoard.y + r * drow,
                                             GuiBoard.width +
                                             GuiBoard.line_thickness,
                                             GuiBoard.line_thickness))

            else:
                pygame.draw.rect(gui.app.App.instance.screen,
                                 (0, 0, 0),
                                 (GuiBoard.x, GuiBoard.y + r * drow,
                                  GuiBoard.width, GuiBoard.line_thickness))

                wid = gui.app.App.board_font.size(GuiBoard.nums[r][0])[0]

                gui.app.App.instance.screen.blit(GuiBoard.nums[r][1],
                                                 (GuiBoard.x - (wid/2)
                                                  - 50, GuiBoard.y +
                                                  r * drow + (dcol / 4)))

        for c in range(GuiBoard.cols + 1):

            if c != GuiBoard.cols:

                wid = gui.app.App.board_font.size(GuiBoard.letters[c][0])[0]

                gui.app.App.instance.screen.blit(GuiBoard.letters[c][1],
                                                 (GuiBoard.x + c * dcol +
                                                  ((dcol +
                                                    GuiBoard.line_thickness)
                                                   / 2) -
                                                  (wid / 2), GuiBoard.y - 50))

            pygame.draw.rect(gui.app.App.instance.screen,
                             (0, 0, 0),
                             (GuiBoard.x + c * dcol,
                              GuiBoard.y,
                              GuiBoard.line_thickness,
                              GuiBoard.height))

        px, py = self.get_coords(pygame.mouse.get_pos())

        #print(f"({px}, {py})")

        if px is not None and py is not None:
            pygame.draw.rect(gui.app.App.instance.screen, (3, 148, 252),
                             GuiBoard.square_coords(px, py))

        for sq in GuiBoard.ships:
            pygame.draw.rect(gui.app.App.instance.screen, (255, 0, 0),
                             GuiBoard.square_coords(sq[0], sq[1]))

    def get_coords(self, mouse):

        if not self.check_bounds(*mouse):
            return None, None

        drow = GuiBoard.height / GuiBoard.rows
        dcol = GuiBoard.height / GuiBoard.cols

        x= (mouse[0] - GuiBoard.x)//drow  # + GuiBoard.line_thickness)
        y = (mouse[1] - GuiBoard.y)//dcol  # + GuiBoard.line_thickness)

        if x > GuiBoard.cols:
            x = GuiBoard.cols

        if y > GuiBoard.rows:
            y = GuiBoard.rows

        return x, y

    def check_bounds(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + \
               self.height

    def handle_click(self, mouse):

        if self.disabled:
            return

        x, y = self.get_coords(mouse)

        print(f"Clicked: ({x},{y})")

        if x is None and y is None:
            return
        #    GuiBoard.clicked.append((x, y))

        if GuiBoard.placing_ships:
            if len(GuiBoard.ships) >= 2:
                GuiBoard.ships = [(x,y)]

            else:
                GuiBoard.ships.append((x,y))

            if len(GuiBoard.ships) == 2:

                if gui.app.App.instance.game.place_ship(GuiBoard.ships[0],
                                                        GuiBoard.ships[1],
                                                        GuiBoard.ships
                                                        [GuiBoard.ships_index]):
                    GuiBoard.ships_index += 1

                    print(crayons.red(f'Placed ship at {GuiBoard.ships}'))

                    if GuiBoard.ships_index == 5:
                        GuiBoard.placing_ships = False
