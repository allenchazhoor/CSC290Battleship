import pygame, gui.app
from collections import namedtuple

Style = namedtuple("Style", "bg hbg tcolor")

class Button:

    def __init__(self, x, y, width, height, style, text, on_click):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style
        self.text = gui.app.App.button_font.render(text, True, (0, 0, 0)) if text else None
        self.text_size = gui.app.App.button_font.size(text)
        self.text_pos = ((self.x+self.width-self.text_size[0])//2, (self.y+self.height-self.text_size[1])//2)
        self.on_click = on_click

    def check_bounds(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def handle_click(self, mouse):

        x = mouse[0]
        y = mouse[1]

        if self.check_bounds(x, y):
            self.on_click()

    def render(self):
        
        x, y = pygame.mouse.get_pos()

        pygame.draw.rect(gui.app.App.instance.screen, self.style.hbg if self.check_bounds(x,y) else self.style.bg, (self.x, self.y, self.width, self.height))
        
        if self.text:
            gui.app.App.instance.screen.blit(self.text, self.text_pos)