import pygame
import sys
from chessman import Chessman
from computer import Computer,Score
from regulation import  Regulation
import random
def check_events(screen,settings,chessmans,chessboard):
    '''
    检查输入输出状态
    :param screen:界面引用
    :param settings:游戏设置
    :param chessmans:棋子group
    :param chessboard:棋盘
    :return:
    '''
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, ):#pygame.KEYDOWN
            sys.exit()
        elif settings.player_round and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            return put_chessman(screen,settings.player_color,[mouse_x,mouse_y],settings,chessmans,chessboard)
        elif settings.player_round == False:
            computer = Computer(settings, chessboard)
            # # if(color_num==1):
            computer_act_list = computer.max_min_search(settings, computer.root, 2)
            # print(computer_act_list)
            computer_act = random.choice(computer_act_list)
            print(computer_act)
            return put_chessman(screen, settings.computer_color, computer_act, settings, chessmans, chessboard)
        return None
        # elif settings.player_round == False and event.type == pygame.MOUSEBUTTONDOWN:# 临时启用
        #     mouse_x,mouse_y = pygame.mouse.get_pos()
        #     put_chessman(screen,settings.computer_color,[mouse_x,mouse_y],settings,chessmans,chessboard)

def update_screen(screen,settings,chessmans,chessboard,cue_board):
    '''
    更新屏幕内容
    :param screen:界面引用
    :param settings:游戏设置
    :param chessmans:棋子group
    :param chessboard:棋盘
    :return:
    '''
    screen.fill(settings.bg_color)   # 刷新背景色
    chessboard.blitme()  # 绘制棋盘
    for chessman in chessmans:
        chessman.blitme()  # 绘制棋子
    cue_board.show_cue() # 绘制提示
    pygame.display.update()  # 更新显示

def put_chessman(screen,color,position,settings,chessmans,chessboard):
    '''
    放子
    :param screen:界面引用
    :param color:该子的颜色
    :param position:该子的位置
    :param settings:游戏设置
    :param chessmans:棋子group
    :param chessboard:棋盘
    :return:
    '''
    if color==settings.player_color:
        real_pos,draw_pos = cal_realpos_and_drawpos(position, chessboard)
    else:
        real_pos = position
        draw_pos = cal_drawpos(position, chessboard)

    #print(real_pos)
    #print(draw_pos)
    print(color)
    color_num = 1 if color == 'white' else -1
    if real_pos[0]!=None and real_pos[1]!=None and can_put(chessboard,real_pos):
        settings.set_player_round(not settings.player_round)
        new_chessman = Chessman(screen,color,draw_pos,settings)
        chessboard.array_cb[real_pos[0]][real_pos[1]] = color_num
        chessmans.add(new_chessman)
        #print(chessboard.array_cb)


        if Regulation.check_win(settings, chessboard.array_cb, real_pos, color_num):
            if color == settings.player_color:
                return 'player-win'
            else:
                return 'computer-win'
    if color == settings.player_color:
        return 'computer'
    else:
        return 'player'



def can_put(chessboard,real_pos):
    """判断该位置是否已经有子"""
    if chessboard.array_cb[real_pos[0]][real_pos[1]]!=0:
        return False
    else:
        return True

def cal_realpos_and_drawpos(position,chessboard):
    '''
    通过坐标计算棋子在棋盘上的位置
    :param position:屏幕坐标
    :param chessboard:棋盘引用
    :return:[real_x,real_y]棋盘位置,[draw_x,draw_y]棋子绘图位置
    '''
    real_row,real_column = None,None
    draw_x,draw_y = None,None
    index = 0
    # Notice: 屏幕坐标xy与行列相反,为x《-》列，y《-》行
    print(chessboard.pos_map)
    for i in chessboard.pos_map['screen_pos']:
        if (position[1] < (i + int(chessboard.gap/2)) ) and (position[1] >(i - int(chessboard.gap/2))):
            real_row = index
            draw_y = i
        if (position[0] < (i + int(chessboard.gap/2)) ) and (position[0] >(i - int(chessboard.gap/2))):
            real_column = index
            draw_x = i
        index += 1
    return [real_row,real_column],[draw_x,draw_y]

def cal_drawpos(position,chessboard):
    draw_x,draw_y = None,None
    # Notice: 屏幕坐标xy与行列相反,为x《-》列，y《-》行
    print(chessboard.pos_map['real_pos'])
    for i in chessboard.pos_map['real_pos']:
        if position[0]==i:
            print('draw_y')
            print(i)
            draw_y = chessboard.pos_map['screen_pos'][i]
            print(draw_y)
        if position[1]==i:
            print('draw_x')
            print(i)
            draw_x = chessboard.pos_map['screen_pos'][i]
            print(draw_x)
    return [draw_x,draw_y]