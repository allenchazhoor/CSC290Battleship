import pygame, crayons

class App:

    fill_color = (0, 0, 0) # RGB black

    def __init__(self):
        self._running = False
        self.size = self.width, self.height = (1000, 1000)

        print(crayons.green('Instantiated App'))

    def start(self):

        pygame.init()

        pygame.font.init()

        print(crayons.green('Initialized PyGame'))

        self.arial = pygame.font.SysFont("Arial", 30)

        pygame.display.set_caption('DreadNought')

        self.screen = pygame.display.set_mode(self.size)

        self._running = True

        self.loop()

    def keyboard(self, event):
        if event.key == pygame.K_q:
            print(crayons.red('Q key pressed, exit'))
            self._running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(crayons.red('Exit requested'))
                self._running = False
            elif event.type == pygame.KEYDOWN:
                self.keyboard(event)

    def cleanup(self):

        pygame.quit()
        
        print(crayons.green('Game loop exited, PyGame quit'))


    def logic(self):
        pass

    def render(self):
        
        self.screen.fill( self.fill_color ) # Clear screen

        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 100, 100))

        pygame.display.flip() # Render

    def loop(self):

        while self._running:
            
            self.handle_events()

            self.logic()

            self.render()
        
        self.cleanup()

if __name__ == '__main__':

    app = App()

    app.start()