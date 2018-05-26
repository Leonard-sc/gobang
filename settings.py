class Settings():
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_heigh = 600
        self.board_size = 9
        self.bg_color = (230,230,230) # 屏幕背景色
        self.chessman_size = 15 # 绘制棋子大小

        self.player_round = True
        self.player_color = 'white' # default 1
        self.computer_color = 'black' # -1

    def set_player_round(self,player_round):
        """user_round 为True时玩家可下"""
        self.player_round = player_round

    def set_player_color(self,color):
        if color == 'white':
            self.player_color = color
            self.computer_color = 'black'
        else:
            self.player_color = color
            self.computer_color = 'white'