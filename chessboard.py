import pygame
class Chessboard():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.board_size = settings.board_size
        self.min_edge = int(settings.screen_heigh * 0.1)
        self.max_edge = int(settings.screen_heigh - self.min_edge)
        self.line_color = (60,60,60)

        # 数组形态
        self.array_cb = None


    def blitme(self):
        # 绘制棋盘
        gap = int(self.max_edge/self.board_size)
        line_length = self.max_edge-self.min_edge
        for i in range(self.min_edge,self.max_edge+1,gap):
            line_x = pygame.Rect(i, self.min_edge, 1, line_length)
            line_y = pygame.Rect(self.min_edge, i, line_length, 1)
            pygame.draw.rect(self.screen,self.line_color,line_x)
            pygame.draw.rect(self.screen,self.line_color,line_y)

        # 绘制分割线
        gap_line = pygame.Rect(self.max_edge+self.min_edge,0,1,self.settings.screen_heigh)
        pygame.draw.rect(self.screen,self.line_color,gap_line)