import pygame
from pygame.sprite import Sprite
class Chessman(Sprite):
    def __init__(self,screen,color,position,settings):
        super().__init__()
        if color == 'white':
            self.color = (255,255,255)
        elif color == 'black':
            self.color = (0,0,0)
        self.screen = screen
        self.settings = settings
        self.position = position

    def blitme(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.settings.chessman_size)

    def pin_drawloc(self):
        # TODO: 计算真正绘制坐标
        pass