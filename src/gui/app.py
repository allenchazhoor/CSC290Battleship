import pygame, crayons
from gui.button import Button, Style
from enum import Enum

class App:

    instance = None

    fill_color = (0, 0, 0) # RGB black

    background = pygame.image.load('resources/background.jpg')
    title = pygame.image.load('resources/title.png')
    play_button = pygame.image.load('resources/play.png')
    info_button = pygame.image.load('resources/info.png')

    arial = pygame.font.SysFont("Arial", 30)

    button_font = pygame.font.SysFont("Calibri", 30)

    class mode(Enum):
        title_screen = 0
        game = 1
        settings = 2

    def __init__(self):

        App.instance = self
        
        self._running = False
        
        self.size = self.width, self.height = (1000, 1000)
        
        self.mode = App.mode.title_screen

        self.button = Button(100, 100, 100, 100,
            "abc", lambda: print(crayons.cyan('clicked!')), Style(bg = (255,255,255), hbg = (0,0,0), tcolor = (255,0,0)))

        self.exit = Button(0, 0, 200, 70,
            "Exit", lambda: App.instance.stop(), Style(bg = (233, 30, 99), hbg = (255, 96, 144), tcolor = (0,0,0)))

        self.play_button = Button(300, 450, 300, 200, "Play", lambda: App.instance.set_mode(App.mode.game))

        

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

        if self.mode == App.mode.game:
            self.button.handle_click(pos)
        elif self.mode == App.mode.title_screen:
            self.play_button.handle_click(pos)
        
        self.exit.handle_click(pos)

    def handle_events(self):
        """Loops through pygame events and handle them"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(crayons.red('Exit requested'))
                self._running = False
            elif event.type == pygame.KEYDOWN:
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
        if self.mode == App.mode.title_screen:
            # Render Title Screenpasspasspass
            
            self.screen.blit(App.background, (0, 0))
            self.screen.blit(App.title, (235, 150))
            self.screen.blit(App.play_button, (300, 450))
            self.screen.blit(App.info_button, (300, 600))
            self.play_button.render()
        elif self.mode == App.mode.game:
            # Render game
            
            self.button.render()

        elif self.mode == App.mode.settings:
            pass

        self.exit.render()

        # End drawing code

        pygame.display.flip()  # Render

    def loop(self):
        """Main game loop"""

        while self._running:

            self.handle_events()

            self.logic()

            self.render()
        
        self.cleanup()