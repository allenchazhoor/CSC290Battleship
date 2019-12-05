import pygame
import crayons
from gui.button import Button, Style
from gui.guiboard import GuiBoard
from enum import Enum
from model.controller import Controller
import pathlib


def relative(fn):
    return str(pathlib.Path(__file__).parent.parent / fn)


class App:

    instance = None

    fill_color = (255, 255, 255)  # RGB white

    print(relative('resources/background.jpg'))

    background = pygame.image.load(relative('resources/background.jpg'))
    title = pygame.image.load(relative('resources/title.png'))

    arial = pygame.font.SysFont("Arial", 30)

    button_font = pygame.font.SysFont("Calibri", 30)

    title_screen_button_font = pygame.font.SysFont("Calibri", 80)

    board_font = pygame.font.SysFont("Calibri", 50)

    message = "Place your ships!"

    pause = False

    class Mode(Enum):
        title_screen = 0
        game = 1
        settings = 2
        info = 3

    def __init__(self):

        if App.instance:
            raise Exception

        GuiBoard.init()  # Initialize GuiBoard singleton

        App.instance = self

        self._running = False

        self.game = Controller()

        self.size = self.width, self.height = (1000, 1000)

        self.mode = App.Mode.title_screen

        self.button = Button(100, 100, 100, 100,
                             "abc", App.button_font, lambda:
                             print(crayons.cyan('clicked!')),
                             Style(bg=(255, 255, 255),
                                   hbg=(0, 0, 0), tcolor=(255, 0, 0)))

        self.button.disabled = True

        self.exit = Button(0, 0, 200, 70,
                           "Exit", App.button_font, lambda:
                           App.instance.stop(), Style(bg=(233, 30, 99),
                                                      hbg=(255, 96, 144),
                                                      tcolor=(0, 0, 0)))

        self.exit.disabled = True

        s = Style((10, 123, 209), (10, 123, 209), (255,255,255))

        self.play_button = Button(300, 450, 400, 125,
                                  "Play", App.title_screen_button_font, lambda:
                                  App.instance.set_mode(App.Mode.game), style=s)

        self.info_button = Button(300, 600, 400, 125, "Info",
                                  App.title_screen_button_font, lambda:
                                  App.instance.set_mode(App.Mode.info),
                                  style=s)

        print(crayons.green('Instantiated App'))

    def set_mode(self, mode):
        self.mode = mode

    def stop(self):
        self._running = False

    def start(self):
        """Display the window and start the game"""

        pygame.display.set_caption('DreadNought')

        self.screen = pygame.display.set_mode(self.size)

        self._running = True

        self.loop()

    def keyboard(self, event):
        """Handle a keyboard event"""

        if event.key == pygame.K_q:
            print(crayons.red('Q key pressed, exit'))
            self._running = False

    def click(self, event):

        pos = pygame.mouse.get_pos()

        if self.mode == App.Mode.game:
            self.button.handle_click(pos)
            GuiBoard.instance.handle_click(pos)
        elif self.mode == App.Mode.title_screen:
            self.play_button.handle_click(pos)
            self.info_button.handle_click(pos)

        self.exit.handle_click(pos)

    def handle_events(self):
        """Loops through pygame events and handle them"""

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.ACTIVEEVENT:
                if event.state == 1:
                    if event.gain == 0: # Mouse has left the game
                        App.pause = True
                    elif event.gain == 1:
                        App.pause = False
            elif event.type == pygame.QUIT:
                print(crayons.red('Exit requested'))
                self._running = False

        if App.pause:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keyboard(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click(event)

    def cleanup(self):
        """Quits pygame and cleans up"""

        pygame.quit()

        print(crayons.green('Game loop exited, PyGame quit'))

    def logic(self):
        """Handles the game logic on each loop"""
        pass

    def render(self):

        self.screen.fill(self.fill_color)  # Clear screen

        # Begin drawing code
        if self.mode == App.Mode.title_screen:
            # Render Title Screen

            self.screen.blit(App.background, (0, 0))
            self.screen.blit(App.title, (235, 150))
            self.play_button.render()
            self.info_button.render()
        elif self.mode == App.Mode.game:
            # Render game

            GuiBoard.instance.render()

            self.button.render()

            self.screen.blit(App.board_font.render(App.message,
                                                   True, (0, 0, 0)),
                             ((self.size[0]
                               - App.board_font.size(App.message)[0])/2, 30))

        elif self.mode == App.Mode.settings:
            pass

        self.exit.render()

        # End drawing code

        pygame.display.flip()  # Render

    def loop(self):
        """Main game loop"""

        while self._running:

            self.handle_events()

            if App.pause:
                continue

            self.logic()

            self.render()

        self.cleanup()
