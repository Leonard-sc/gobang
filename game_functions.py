import pygame
import sys
from chessman import Chessman

def check_events(screen,settings,chessmans,chessboard):
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            put_chessman(screen,'white',[mouse_x,mouse_y],settings,chessmans,chessboard)

def update_screen(screen,settings,chessmans,chessboard):
    screen.fill(settings.bg_color)
    chessboard.blitme()
    for chessman in chessmans:
        chessman.blitme()
    pygame.display.update()

def put_chessman(screen,color,position,settings,chessmans,chessboard):
    # TODO: 此处判断游戏是否分出胜负

    real_pos = cal_realpos(settings, position, chessboard)
    print(real_pos)
    if real_pos[0]!=None and real_pos[1]!=None and can_put(settings,chessboard,real_pos):
        new_chessman = Chessman(screen,color,position,settings)
        if color == 'white':
            chessboard.array_cb[real_pos[0]][real_pos[1]] = 1
        elif color == 'black':
            chessboard.array_cb[real_pos[0]][real_pos[1]] = -1
        chessmans.add(new_chessman)

def can_put(settings,chessboard,real_pos):
    """判断该位置是否在可放子范围内以及是否已经有子"""
    # TODO:判断是否在可放子范围
    if chessboard.array_cb[real_pos[0]][real_pos[1]]!=0:
        return False
    else:
        return True

def cal_realpos(settings,position,chessboard):
    real_x,real_y = None,None
    index = 0
    for i in chessboard.pos_map['screen_pos']:
        if (position[0] < (i + int(chessboard.gap/2)) ) and (position[0] >(i - int(chessboard.gap/2))):
            real_x = index
        if (position[1] < (i + int(chessboard.gap/2)) ) and (position[1] >(i - int(chessboard.gap/2))):
            real_y = index
        index += 1
    return [real_x,real_y]