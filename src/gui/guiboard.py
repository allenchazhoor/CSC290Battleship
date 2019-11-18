import pygame, gui.app
from enum import Enum

class guiboard:

    class player(Enum):
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

    active_player = player.p1

    ships = []

    def __init__(self):
        if guiboard.instance:
            raise Exception

        guiboard.letters = [(let, gui.app.App.board_font.render(let, True, (0,0,0))) for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

        guiboard.nums = [(n, gui.app.App.board_font.render(n, True, (0,0,0))) for n in list("123456789") + ['10', '11']]

    def init():
        guiboard.instance = guiboard()

    def square_coords(row, col):

        drow = guiboard.height / guiboard.rows
        dcol = guiboard.height / guiboard.cols

        return (guiboard.x + row * dcol + guiboard.line_thickness, guiboard.y + col * drow + guiboard.line_thickness, dcol - guiboard.line_thickness, drow - guiboard.line_thickness)

    def render(self):
        
        #pygame.draw.rect(gui.app.App.instance.screen, (0,0,0), (guiboard.x, guiboard.y, guiboard.width, guiboard.height))

        drow = guiboard.height / guiboard.rows
        dcol = guiboard.height / guiboard.cols

        for r in range(guiboard.rows + 1):

            if r == guiboard.rows:
                pygame.draw.rect(gui.app.App.instance.screen, (0,0,0),
                (guiboard.x,
                guiboard.y + r * drow, guiboard.width + guiboard.line_thickness,
                guiboard.line_thickness))

            else:
                pygame.draw.rect(gui.app.App.instance.screen, (0,0,0),
                (guiboard.x,
                guiboard.y + r * drow, guiboard.width,
                guiboard.line_thickness))

                wid = gui.app.App.board_font.size(guiboard.nums[r][0])[0]

                gui.app.App.instance.screen.blit(guiboard.nums[r][1], (guiboard.x - (wid/2) - 50, guiboard.y + r * drow + (dcol / 4)))

        for c in range(guiboard.cols + 1):

            if c != guiboard.cols:

                wid = gui.app.App.board_font.size(guiboard.letters[c][0])[0]

                gui.app.App.instance.screen.blit(guiboard.letters[c][1], (guiboard.x + c * dcol + ((dcol+guiboard.line_thickness) / 2) - (wid / 2), guiboard.y - 50))
            
            pygame.draw.rect(gui.app.App.instance.screen, (0,0,0), (guiboard.x + c * dcol, guiboard.y, guiboard.line_thickness, guiboard.height))

        px, py = self.get_coords(pygame.mouse.get_pos())

        print(f"({px}, {py})")

        if px is not None and py is not None:
            pygame.draw.rect(gui.app.App.instance.screen, (3, 148, 252), guiboard.square_coords(px, py))

        for sq in guiboard.clicked:
            pygame.draw.rect(gui.app.App.instance.screen, (255, 0, 0), guiboard.square_coords(sq[0], sq[1]))

    def get_coords(self, mouse):
        
        if not self.check_bounds(*mouse):
            return None, None

        drow = guiboard.height / guiboard.rows
        dcol = guiboard.height / guiboard.cols

        x= (mouse[0] - guiboard.x)//(drow)# + guiboard.line_thickness)
        y = (mouse[1] - guiboard.y)//(dcol)# + guiboard.line_thickness)

        if (x > guiboard.cols):
            x = guiboard.cols

        if (y > guiboard.rows):
            y = guiboard.rows

        return x, y

    def check_bounds(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def handle_click(self, mouse):

        if self.disabled:
            return

        x, y = self.get_coords(mouse)

        print(f"Clicked: ({x},{y})")

        if x is not None and y is not None:
            guiboard.clicked.append((x, y))
        
        if guiboard.placing_ships:
            if len(guiboard.ships) >= 2:
                guiboard.ships = [(x,y)]
            
            else:
                guiboard.ships.append[(x,y)]