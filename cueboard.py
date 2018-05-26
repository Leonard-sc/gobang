import pygame.font

class Cueboard():
    '''提示胜负及谁的回合'''

    def __init__(self,settings,screen,stats):
        self.settings = settings
        self.screen = screen
        self.stats = stats  # 'player' 'computer' 'player-win' 'computer-win'
        self.screen_rect = screen.get_rect()

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,20)

        self.prep_cue()
    def prep_cue(self):
        if self.stats=='player':
            cue_str = "your turn"
        elif self.stats=='computer':
            cue_str = "computer's turn"
        elif self.stats=='player-win':
            cue_str = "you win"
        elif self.stats=='computer-win':
            cue_str = "you lose"
        self.cue_image =self.font.render(cue_str,True,self.text_color,self.settings.bg_color)

        self.cue_rect = self.cue_image.get_rect()
        self.cue_rect.right = self.screen_rect.right - 50
        self.cue_rect.top = (self.screen_rect.bottom - self.screen_rect.top)/2

    def show_cue(self):
        self.screen.blit(self.cue_image,self.cue_rect)