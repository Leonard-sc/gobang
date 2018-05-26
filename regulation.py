class Regulation():

    @classmethod
    def check_win(cls,settings, chessboard, chess_loc, color):
        '''
        检查此次走子后胜负状况
        :param settings:游戏设置
        :param chessboard:棋盘
        :param chess_loc:新棋子位置
        :param color:棋子颜色
        :return:
        '''
        x = chess_loc[0]
        y = chess_loc[1]
        return cls.check_line(settings, chessboard, x, y, color, 0) or cls.check_line(settings, chessboard, x, y, color,
                                                                              1) or cls.check_line(settings, chessboard, x,
                                                                                               y, color,
                                                                                               2) or cls.check_line(
            settings, chessboard, x, y, color, 3)

    @classmethod
    def check_line(cls,settings, chessboard, x, y, color, direct):
        '''
        判断一条直线是否五子
        :param settings:
        :param chessboard:
        :param x:
        :param y:
        :param color:
        :param direct:0|，1/，2-,3\
        :return:
        '''
        chess_num = 0
        for i in range(2):
            search_x = x
            search_y = y
            for j in range(5):
                if (direct == 0):
                    if i == 0:  # 先往上扫
                        # print(str(chess_num)+':'+str(search_x)+','+str(search_y)+'-color:'+str(color))
                        if search_x >= 0 and chessboard[search_x][search_y] == color:
                            chess_num += 1
                            search_x -= 1
                            # print('inner:'+str(chess_num)+':'+str(search_x)+','+str(search_y))
                        else:
                            break
                    else:  # 再往下扫
                        if search_x < settings.board_size and chessboard[search_x][search_y] == color:
                            if (search_x != x): chess_num += 1  # 跳过重复统计中心节点
                            search_x += 1
                            # print('inner:'+str(chess_num)+':'+str(search_x)+','+str(search_y))
                        else:
                            break
                elif (direct == 1):
                    if i == 0:  # 先往右上扫
                        if search_x >= 0 and search_y < settings.board_size and chessboard[search_x][search_y] == color:
                            chess_num += 1
                            search_x -= 1
                            search_y += 1
                        else:
                            break
                    else:  # 再往左下扫
                        if search_x < settings.board_size and search_y >= 0 and chessboard[search_x][search_y] == color:
                            if (search_x != x and search_y != y): chess_num += 1  # 跳过重复统计中心节点
                            search_x += 1
                            search_y -= 1
                        else:
                            break
                elif (direct == 2):
                    if i == 0:  # 先往右侧扫
                        if search_y < settings.board_size and chessboard[search_x][search_y] == color:
                            chess_num += 1
                            search_y += 1
                        else:
                            break
                    else:  # 再往左侧扫
                        if search_y >= 0 and chessboard[search_x][search_y] == color:
                            if (search_y != y): chess_num += 1  # 跳过重复统计中心节点
                            search_y -= 1
                        else:
                            break
                elif (direct == 3):
                    if i == 0:  # 先往左上扫
                        if search_x >= 0 and search_y >= 0 and chessboard[search_x][search_y] == color:
                            chess_num += 1
                            search_x -= 1
                            search_y -= 1
                        else:
                            break
                    else:  # 再往右下扫
                        if search_x < settings.board_size and search_y < settings.board_size and chessboard[search_x][
                            search_y] == color:
                            if (search_x != x and search_y != y): chess_num += 1  # 跳过重复统计中心节点
                            search_x += 1
                            search_y += 1
                        else:
                            break
        if chess_num == 5:
            return True
        else:
            return False