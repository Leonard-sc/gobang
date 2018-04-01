import pygame

def update_screen(screen,settings,chessboard):
    screen.fill(settings.bg_color)
    chessboard.blitme()
    pygame.display.update()