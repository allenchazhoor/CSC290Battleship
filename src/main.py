import pygame
import crayons

if __name__ == '__main__':

    pygame.font.init()

    pygame.init()

    print(crayons.green('Initialized PyGame'))

    from gui.app import App

    app = App()

    app.start()
