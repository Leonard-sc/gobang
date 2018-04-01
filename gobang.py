import sys
import pygame
import game_functions as gf
from settings import  Settings
from chessboard import Chessboard

def run_game():

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_heigh))
    chessboard = Chessboard(screen,settings)
    white = pygame.image.load('./images/white.png')


    while 1:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT,pygame.KEYDOWN):
                sys.exit()
        gf.update_screen(screen,settings,chessboard)




run_game()