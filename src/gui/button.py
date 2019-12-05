import pygame
import gui.app
from collections import namedtuple

Style = namedtuple("Style", "bg hbg tcolor")


class Button:

    def __init__(self, x, y, width, height, text, font, on_click,
                 style=Style((255, 255, 255), (255, 255, 255), (0, 0, 0))):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style
        self.text = font.render(text, True, style.tcolor)
        self.text_size = font.size(text)
        self.text_pos = (self.x+(self.width-self.text_size[0])//2,
                         self.y+(self.height-self.text_size[1])//2)
        self.on_click = on_click
        self.disabled = False

    def check_bounds(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + \
               self.height

    def handle_click(self, mouse):

        if self.disabled:
            return

        x = mouse[0]
        y = mouse[1]

        if self.check_bounds(x, y):
            self.on_click()

    def render(self):

        if self.disabled:
            return

        x, y = pygame.mouse.get_pos()

        pygame.draw.rect(gui.app.App.instance.screen,
                         self.style.hbg if
                         self.style.hbg and
                         self.check_bounds(x, y)
                         else self.style.bg,
                         (self.x, self.y, self.width, self.height))

        if self.text:
            gui.app.App.instance.screen.blit(self.text, self.text_pos)