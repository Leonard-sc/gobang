class Settings():

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_heigh = 600
        self.board_size = 9
        self.bg_color = (230,230,230) # 屏幕背景色
        self.chessman_size = 15 # 绘制棋子大小

        self.user_round = True

    def set_user_round(self,user_round):
        """user_round 为True时玩家可下"""
        self.user_round = user_round