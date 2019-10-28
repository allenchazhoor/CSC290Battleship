import pygame
import crayons


class App:

    fill_color = (0, 0, 0)  # RGB black

    def __init__(self):
        self._running = False
        self.size = self.width, self.height = (1000, 1000)

        print(crayons.green('Instantiated App'))

    def start(self):
        """Display the window and start the game"""

        pygame.init()

        pygame.font.init()

        print(crayons.green('Initialized PyGame'))

        self.arial = pygame.font.SysFont("Arial", 30)

        pygame.display.set_caption('DreadNought')

        self.screen = pygame.display.set_mode(self.size)

        self._running = True

        self.loop()

    def keyboard(self, event):
        """Handle a keyboard event"""

        if event.key == pygame.K_q:
            print(crayons.red('Q key pressed, exit'))
            self._running = False

    def handle_events(self):
        """Loops through pygame events and handle them"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(crayons.red('Exit requested'))
                self._running = False
            elif event.type == pygame.KEYDOWN:
                self.keyboard(event)

    def cleanup(self):
        """Quits pygame and cleans up"""

        pygame.quit()

        print(crayons.green('Game loop exited, PyGame quit'))

    def logic(self):
        """Handles the game logic on each loop"""
        pass

    def render(self):

        self.screen.fill(self.fill_color)  # Clear screen
        title_screen_rendered = False

        # Begin drawing code
        if title_screen_rendered:
            # Render Game
            pass
        else:
            # Render Title Screen
            background = pygame.image.load('background.jpg')
            title = pygame.image.load('title.png')
            play_button = pygame.image.load('play.png')
            info_button = pygame.image.load('info.png')
            self.screen.blit(background, (0, 0))
            self.screen.blit(title, (235, 150))
            self.screen.blit(play_button, (300, 450))
            self.screen.blit(info_button, (300, 600))

        # End drawing code

        pygame.display.flip()  # Render

    def loop(self):
        """Main game loop"""

        while self._running:

            self.handle_events()

            self.logic()

            self.render()

        self.cleanup()


if __name__ == '__main__':

    app = App()

    app.start()
