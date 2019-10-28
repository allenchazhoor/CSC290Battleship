import pygame, crayons
from gui.button import Button
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

    class render_option(Enum):
        title_screen = 0
        game = 1
        settings = 2

    def __init__(self):

        App.instance = self
        
        self._running = False
        
        self.size = self.width, self.height = (1000, 1000)
        
        self.render_opt = App.render_option.title_screen

        self.button = Button(100, 100, 100, 100, (255,255,255), "abc", lambda: print(crayons.cyan('clicked!')))

        self.exit = Button(0, 0, 200, 70, (233, 30, 99), "Exit", lambda: App.instance.stop())

        print(crayons.green('Instantiated App'))

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

        if self.render_opt == App.render_option.game:
            self.button.check_mouse(pos)
        
        self.exit.check_mouse(pos)

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
        if self.render_opt == App.render_option.title_screen:
            # Render Title Screen
            
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.title, (235, 150))
            self.screen.blit(self.play_button, (300, 450))
            self.screen.blit(self.info_button, (300, 600))
        elif self.render_opt == App.render_option.game:
            # Render game
            
            self.button.render()

        elif self.render_opt == App.render_option.settings:
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