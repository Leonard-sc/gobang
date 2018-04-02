import pygame
from pygame.sprite import Sprite
class Chessman(Sprite):
    def __init__(self,screen,color,draw_pos,settings):
        super().__init__()
        if color == 'white':
            self.color = (255,255,255)
        elif color == 'black':
            self.color = (0,0,0)
        self.screen = screen
        self.settings = settings
        self.draw_pos = draw_pos

    def blitme(self):
        pygame.draw.circle(self.screen,self.color,self.draw_pos,self.settings.chessman_size)
