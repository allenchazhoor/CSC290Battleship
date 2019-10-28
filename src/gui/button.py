import pygame, gui.app

class Button:

    def __init__(self, x, y, width, height, color, text, on_click):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.on_click = on_click
    
    def check_mouse(self, mouse):

        x = mouse[0]
        y = mouse[1]

        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.on_click()

    def render(self):
        pygame.draw.rect(gui.app.App.instance.screen, self.color, (self.x, self.y, self.width, self.height))