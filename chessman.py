import pygame
class Chessman():
    def __init__(self,color):
        self.color = color
        if self.color == 'white':
            self.image = pygame.image.load('./images/white.png')
        elif self.color == 'black':
            self.image = pygame.image.load('./images/black.png')

    def put_chessman(self,):
        pass

    def blitme(self):
        pass
