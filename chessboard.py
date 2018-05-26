import pygame

class Chessboard():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.board_size = settings.board_size
        self.min_edge = int(settings.screen_heigh * 0.1)
        self.max_edge = int(settings.screen_heigh - self.min_edge)
        self.line_length = self.max_edge-self.min_edge
        self.line_color = (60,60,60)
        self.gap = int(self.max_edge / self.board_size) # 线间距离
        # 数组形态的棋盘
        self.array_cb = [[0 for i in range(self.board_size)] for i in range(self.board_size)]
        self.pos_map={'screen_pos':[0 for i in range(self.board_size)],'real_pos':[i for i in range(self.board_size)]}
        self.set_map() # 初始话屏幕坐标与棋盘的映射关系
        # print (self.pos_map)
    def blitme(self):
        # 绘制棋盘
        for i in self.pos_map['screen_pos']:
            line_x = pygame.Rect(i, self.min_edge, 1, self.line_length)
            line_y = pygame.Rect(self.min_edge, i, self.line_length, 1)
            pygame.draw.rect(self.screen,self.line_color,line_x)
            pygame.draw.rect(self.screen,self.line_color,line_y)

        # 绘制分割线
        gap_line = pygame.Rect(self.max_edge+self.min_edge,0,1,self.settings.screen_heigh)
        pygame.draw.rect(self.screen,self.line_color,gap_line)

    def set_map(self):
        index = 0
        for i in range(self.min_edge,self.max_edge+1,self.gap):
            self.pos_map['screen_pos'][index]=i
            index+=1