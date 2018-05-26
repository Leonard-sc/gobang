import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import  Settings
from chessboard import Chessboard
from cueboard import Cueboard

def run_game():

    pygame.init()
    settings = Settings()
    settings.player_color = "white"
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_heigh))
    chessboard = Chessboard(screen,settings)
    chessmans = Group()
    cue_stats = 'player'
    while 1:
        stats = gf.check_events(screen,settings,chessmans,chessboard)
        if 'win' not in cue_stats:
            if stats:
                cue_stats = stats
            cue_board = Cueboard(settings, screen, cue_stats)
            gf.update_screen(screen,settings,chessmans,chessboard,cue_board)






run_game()