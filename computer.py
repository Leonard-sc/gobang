import copy
from regulation import Regulation

class Node():
    def __init__(self,settings,parent,board):
        self.settings = settings
        self.parent = parent
        #if board == None:
        #    self.board = [[0 for i in range(settings.board_size)] for i in range(settings.board_size)]
        #else:
        self.board = copy.deepcopy(board)
        self.child = []
        self.color = None  #刚刚落子导致产生本节点的落子颜色
        self.state = None  # 0-computer 1-player
        self.result = None  # "win"
        self.available_loc = []

    def set_available_loc(self):
        for i in range(self.settings.board_size):
            for j in range(self.settings.board_size):
                if(self.board[i][j]==0): self.available_loc.append([i,j])

class Computer():
    def __init__(self,settings,chessboard):
        self.settings = settings
        self.chessboard = copy.deepcopy(chessboard.array_cb)
        self.root = Node(settings,None,self.chessboard)
        self.root.set_available_loc()
        self.root.state = 0
        # print("available_loc num=",self.root.available_loc)

    # def expand_tree(self,node):
    #     if node.state == "win" or len(node.available_loc) == 0 :
    #         print("搜到底一次")
    #         return
    #     for x,y in node.available_loc:
    #         child = Node(self.settings, node, node.board)
    #         child.state = 1-node.state  # reverse player
    #         color = self.settings.computer_color if child.state==0 else self.settings.player_color
    #         child.board[x][y] = 1 if color == 'white' else -1
    #         child.available_loc = node.available_loc[:]
    #         child.available_loc.remove([x,y])
    #         #if(check_win(self.settings,child.board,[x,y],color)):
    #         #    child.state = "win"
    #         node.child.append(child)
    #         # self.expand_tree(child)
    #     # print(node.available_loc)
    #     # print(node.child[0].available_loc)

    def max_min_search(self,settings,node,deep):
        loc_list = []
        best = -999999
        computer_color = -1 if  settings.computer_color=='black' else 1
        for x,y in node.available_loc:
            board = copy.deepcopy(node.board)
            board[x][y]=computer_color
            child = Node(settings,node,board)
            child.available_loc = node.available_loc[:]
            child.available_loc.remove([x,y])
            temp_max = self.min_search(settings,child,deep-1)
            if temp_max==best:
                loc_list.append([x,y])
            if temp_max>best:
                best = temp_max
                loc_list.clear()
                loc_list.append([x,y])
        return loc_list

    def max_search(self,settings,node,deep):# ,alpha,beta
        computer_color = -1 if settings.computer_color == 'black' else 1
        player_color = -1 if settings.player_color == 'black' else 1
        score1 = Score.get_board_score(settings,node.board,computer_color)
        score2 = Score.get_board_score(settings,node.board,player_color)
        if deep<=0:
            # print(score1-score2)
            return score1-score2
        best =-999999
        for x,y in node.available_loc:
            board = copy.deepcopy(node.board)
            board[x][y]=computer_color
            child = Node(settings,node,board)
            child.available_loc = node.available_loc[:]
            child.available_loc.remove([x,y])
            temp_max = self.min_search(settings,child,deep-1)#,alpha,best if best>beta else beta
            if temp_max>best:
                best = temp_max
            # if temp_max>alpha:
            #     break
        return best

    def min_search(self,settings,node,deep):#,alpha,beta
        computer_color = -1 if settings.computer_color == 'black' else 1
        player_color = -1 if settings.player_color == 'black' else 1
        score1 = Score.get_board_score(settings,node.board,computer_color)
        score2 = Score.get_board_score(settings,node.board,player_color)
        if deep<=0:
            return score1-score2
        best =999999
        for x,y in node.available_loc:
            board = copy.deepcopy(node.board)
            board[x][y]=player_color
            child = Node(settings,node,board)
            child.available_loc = node.available_loc[:]
            child.available_loc.remove([x,y])
            temp_min = self.max_search(settings,child,deep-1)# ,best if best<alpha else alpha,beta
            if temp_min<best:
                best = temp_min
            # if temp_min<beta:
            #     break
        # print(best)
        return best

    # def max_min_search(self,settings,node,max_min,deep):
    #     color = None
    #     computer_color =  -1 if self.settings.computer_color=='black' else 1
    #     if node == self.root:
    #         if settings.player_round:
    #             color = 1 if self.settings.player_color=='white' else -1
    #         else:
    #             color = -1 if self.settings.computer_color=='black' else 1
    #         node.color = color
    #     else:
    #         if node.color == 1: #min时color为玩家color；max时color为computer的color
    #             color= -1
    #         else:
    #             color = 1
    #     if node==self.root:
    #         print(settings.player_round)
    #         print(color)
    #     if(max_min=='min'):
    #         min_score = 999999
    #         # color = 1 if self.settings.player_color=='white'else -1
    #     else:
    #         max_score = 0
    #         # color = -1 if self.settings.computer_color=='black'else 1
    #     # print(color)
    #     if node != self.root:
    #         score = Score.get_board_score(settings,node.board,computer_color)
    #         # print(max_min)
    #         # print(score)
    #         if deep<=0:
    #             return score
    #     if node == self.root:
    #         loc_list = []
    #     count=0
    #     for x,y in node.available_loc:
    #         board = copy.deepcopy(node.board)
    #         board[x][y]=color
    #         child = Node(self.settings, node, board)
    #         child.color = color
    #         child.available_loc = node.available_loc[:]
    #         child.available_loc.remove([x,y])
    #         # print(count)
    #         if(max_min=='min'):
    #             # print('-----min-----')
    #             temp_min = self.max_min_search(settings,child,'max',deep-1)
    #             if temp_min<min_score :
    #                 min_score=temp_min
    #                 if node==self.root:
    #                     loc_list.clear()
    #                     loc_list.append([x,y])
    #             elif node==self.root and temp_min == min_score:
    #                 loc_list.append([x,y])
    #
    #         else:
    #             # print('-----max-----')
    #             temp_max = self.max_min_search(settings,child,'min',deep-1)
    #             if temp_max>max_score :
    #                 max_score=temp_max
    #                 if node==self.root:
    #                     loc_list.clear()
    #                     loc_list.append([x,y])
    #             elif node==self.root and temp_max == max_score:
    #                 loc_list.append([x,y])
    #             print([x, y])
    #             print(temp_max)
    #     if node==self.root:
    #         return loc_list
    #     else:
    #         if (max_min == 'min'):
    #             print('###min-score###')
    #             print(min_score)
    #             print('###min-score###')
    #             return min_score
    #         else:
    #             print('###max-score###')
    #             print(max_score)
    #             print('###max-score###')
    #             return max_score





class Score():
    @classmethod
    def get_board_score(cls,settings,board,color):
        max_score = 0
        for i in range(settings.board_size):
            for j in range(settings.board_size):
                if board[i][j] == color:
                    # print(str(i) + "," + str(j))
                    part = Score.get_board_part(settings,board,color,i,j)
                    score = Score.get_score(part)
                    # if i==3 and j==4:
                    #     print(str(i)+","+str(j))
                    #     print(part)
                    #     print(score)
                    if score > max_score:
                        max_score = score
        return max_score

    @classmethod
    def get_score(cls,all_part):
        '''
        为欲落子的落子后情况进行评分
        :param all_part:片段
        :return: 评分
        '''
        '''
        参考https://www.cnblogs.com/songdechiu/p/5768999.html
        参考https://tieba.baidu.com/p/2180847383?red_tag=3138977931
        +=白子 -=黑子 o=空位置
        5:胜利
        live4:活4 左右均空 o++++o
        rush4:冲4 -++++o 或 +++o+ 或 ++o++
        live3:活3 o+++o 或 ++o+ 可以形成活4或冲4
        sleep3:眠3 -+++oo 或 -++o+o 或 -+o++o 或 ++oo+ 或 +o+o+ 或 -o+++o-  只能形成冲4
        live2:活2 oo++oo 或 o+o+o 或 +oo+
        sleep2:眠2 -++ooo 或 -+o+oo 或 -+oo+o 或 +ooo+
        '''
        templet = {
            '5': ['+++++'],
            'live4': ['o++++o'],
            'rush4': [ '-++++o','#++++o','+++o+','++o++'],
            'live3': ['o+++o','++o+'],
            'sleep3': ['-+++oo','#+++oo','-++o+o','#++o+o','-+o++o','#+o++o','++oo+','+o+o+','-o+++o-','#o+++o-'],
            'live2': ['oo++oo','o+o+o','+oo+'],
            'sleep2': ['-++ooo','#++ooo','-+o+oo','#+o+oo','-+oo+o','#+oo+o','+ooo+']
        }

        score_dic = {'5':100000,'live4':10000,'rush4':500,'live3':1000,'sleep3':300,'live2':200,'sleep2':100}
        max_score = 1 # nothing
        for part in all_part:
            for status,mod in templet.items():
                for each_mod in mod:
                    if (each_mod in part) or (each_mod[::-1] in part) :
                        max_score = score_dic[status]
        return max_score


    @classmethod
    def get_board_part(cls,settings,chessboard,color,x,y):
        """返回此次落子所有方向的片段以待匹配计分"""
        all_part =[]  # 存放所有方向的片段
        for direct in range(4):
            part = ''  # 棋子片段用于后续匹配模板计算分数
            for j in range(-4,5):
                search_x = x
                search_y = y
                # print(search_x)
                # print(search_y)
                if (direct == 0):  # 从上往下扫
                    search_x  = search_x+j
                elif(direct==1):  # 这样/从右上往左下扫
                    search_x = search_x + j
                    search_y = search_y - j
                elif(direct==2):  # 这样-从左往右扫
                    search_y = search_y + j
                elif(direct==3):  # 这样\从左上往右下扫
                    search_x = search_x + j
                    search_y = search_y + j
                if search_x>=0 and search_x<settings.board_size and search_y>=0 and search_y<settings.board_size:
                    if chessboard[search_x][search_y] == color:
                        part+='+'  # 我方
                    elif chessboard[search_x][search_y]==0:
                        part+='o'  # 空
                    else:
                        part+='-'  # 对方
                else:
                    part+='#'  # 边界外
                # print(part)
            all_part.append(part)

        return all_part