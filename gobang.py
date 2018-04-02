import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import  Settings
from chessboard import Chessboard


def run_game():

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_heigh))
    chessboard = Chessboard(screen,settings)
    chessmans = Group()
    while 1:
        gf.check_events(screen,settings,chessmans,chessboard)
        gf.update_screen(screen,settings,chessmans,chessboard)





run_game()