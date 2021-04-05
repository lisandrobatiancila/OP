import pygame
import sys

class Response:
    
    def __init__(self, screen, WIDTH, HEIGHT):
        self.font_size_15 = pygame.font.Font('freesansbold.ttf', 15)
        self.font_size_10 = pygame.font.Font('freesansbold.ttf', 10)
        self.font_size_20 = pygame.font.Font('freesansbold.ttf', 20)
        self.font_size_25 = pygame.font.Font('freesansbold.ttf', 25)
        self.font_size_30 = pygame.font.Font('freesansbold.ttf', 30)
        self.font_size_40 = pygame.font.Font('freesansbold.ttf', 40)
        self.font_size_50 = pygame.font.Font('freesansbold.ttf', 50)
        self.font_size_60 = pygame.font.Font('freesansbold.ttf', 60)
        self.font_size_100 = pygame.font.Font('freesansbold.ttf', 100)
        
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.level_numbers = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']
        self.game_current_level = 1
        self.is_active = True        
    def game_title(self):
        is_running = True
        game_title = self.font_size_100.render('OP', True, (255, 255, 255))
        game_rect = game_title.get_rect()
        game_rect.center = (self.WIDTH/2, self.HEIGHT-180)
        sub_title = self.font_size_20.render('Out of Place', True, (255, 255, 255))
        sub_rect = sub_title.get_rect()
        sub_rect.center = (game_rect.x+80, game_rect.y+120)
        press_any_key = self.font_size_15.render('Press G to continue', True, (000, 255, 000))
        press_key_rect = press_any_key.get_rect()
        press_key_rect.bottomleft = (self.WIDTH-150, self.HEIGHT-20)
        
        is_quit = False
        while is_running:
            self.screen.fill((000, 000, 000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    is_quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        is_running = False                        
            if not is_quit:
                self.screen.blit(game_title, game_rect)
                self.screen.blit(sub_title, sub_rect)
                self.screen.blit(press_any_key, press_key_rect)
                pygame.display.flip()
            else:
                pygame.quit()
                sys.exit()
    def levels(self, level):
        if level == 1 and self.is_active:
            self.game_current_level = 1
            self.screen.fill((000, 000, 000))
            level_text = self.font_size_30.render(self.level_numbers[0], True, (255, 255, 255))
            level_rect = level_text.get_rect()
            level_rect.center = (self.WIDTH-250, self.HEIGHT-150)
            self.screen.blit(level_text, level_rect)
            please_wait = self.font_size_15.render('Please wait...', True, (255, 255, 255))
            please_wait_rect = please_wait.get_rect()
            please_wait_rect.bottomleft = (self.WIDTH-100, self.HEIGHT-15)
            self.screen.blit(please_wait, please_wait_rect)
            
            pygame.display.flip()
            pygame.time.wait(1500)
        elif level == 2 and self.is_active:
            self.game_current_level = 2
            self.screen.fill((000, 000, 000))
            level_text = self.font_size_30.render(self.level_numbers[1], True, (255, 255, 255))
            level_rect = level_text.get_rect()
            level_rect.center = (self.WIDTH-250, self.HEIGHT-150)
            self.screen.blit(level_text, level_rect)
            please_wait = self.font_size_15.render('Please wait...', True, (255, 255, 255))
            please_wait_rect = please_wait.get_rect()
            please_wait_rect.bottomleft = (self.WIDTH-100, self.HEIGHT-15)
            self.screen.blit(please_wait, please_wait_rect)
            
            pygame.display.flip()
            pygame.time.wait(1500)
        elif level == 3 and self.is_active:
            self.game_current_level = 3
            self.screen.fill((000, 000, 000))
            level_text = self.font_size_30.render(self.level_numbers[2], True, (255, 255, 255))
            level_rect = level_text.get_rect()
            level_rect.center = (self.WIDTH-250, self.HEIGHT-150)
            self.screen.blit(level_text, level_rect)
            please_wait = self.font_size_15.render('Please wait...', True, (255, 255, 255))
            please_wait_rect = please_wait.get_rect()
            please_wait_rect.bottomleft = (self.WIDTH-100, self.HEIGHT-15)
            self.screen.blit(please_wait, please_wait_rect)
            
            pygame.display.flip()
            pygame.time.wait(1500)
        elif level == 4 and self.is_active:
            self.game_current_level = 4
            self.screen.fill((000, 000, 000))
            level_text = self.font_size_30.render(self.level_numbers[3], True, (255, 255, 255))
            level_rect = level_text.get_rect()
            level_rect.center = (self.WIDTH-250, self.HEIGHT-150)
            self.screen.blit(level_text, level_rect)
            please_wait = self.font_size_15.render('Please wait...', True, (255, 255, 255))
            please_wait_rect = please_wait.get_rect()
            please_wait_rect.bottomleft = (self.WIDTH-100, self.HEIGHT-15)
            self.screen.blit(please_wait, please_wait_rect)
            
            pygame.display.flip()
            pygame.time.wait(1500)
        
        elif level == 5 and self.is_active:
            self.game_current_level = 5
            self.screen.fill((000, 000, 000))
            level_text = self.font_size_30.render(self.level_numbers[4], True, (255, 255, 255))
            level_rect = level_text.get_rect()
            level_rect.center = (self.WIDTH-250, self.HEIGHT-150)
            self.screen.blit(level_text, level_rect)
            please_wait = self.font_size_15.render('Please wait...', True, (255, 255, 255))
            please_wait_rect = please_wait.get_rect()
            please_wait_rect.bottomleft = (self.WIDTH-100, self.HEIGHT-15)
            self.screen.blit(please_wait, please_wait_rect)
            
            pygame.display.flip()
            pygame.time.wait(1500)
    def scores(self, scores):
        if self.game_current_level == 1:
            score = self.font_size_20.render(f'Scores: {scores}', True, (255, 255, 255))
            score_rect = score.get_rect()
            score_rect.topleft = (self.WIDTH-120, 0)
            self.screen.blit(score, score_rect)
        if self.game_current_level == 2:
            score = self.font_size_20.render(f'Scores: {scores}', True, (255, 255, 255))
            score_rect = score.get_rect()
            score_rect.topleft = (self.WIDTH-120, 0)
            self.screen.blit(score, score_rect)
        if self.game_current_level == 3:
            score = self.font_size_20.render(f'Scores: {scores}', True, (255, 255, 255))
            score_rect = score.get_rect()
            score_rect.topleft = (self.WIDTH-120, 0)
            self.screen.blit(score, score_rect)
        if self.game_current_level == 4:
            score = self.font_size_20.render(f'Scores: {scores}', True, (255, 255, 255))
            score_rect = score.get_rect()
            score_rect.topleft = (self.WIDTH-120, 0)
            self.screen.blit(score, score_rect)
        if self.game_current_level == 5:
            score = self.font_size_20.render(f'Scores: {scores}', True, (255, 255, 255))
            score_rect = score.get_rect()
            score_rect.topleft = (self.WIDTH-120, 0)
            self.screen.blit(score, score_rect)
    def game_over(self):
        g_text = self.font_size_50.render('Game', True, (255, 000, 000))
        g_text_rect = g_text.get_rect()
        g_text_rect.center = (self.WIDTH-250, self.HEIGHT-200)
        o_text = self.font_size_50.render('Over', True, (255, 000, 000))
        o_text_rect = o_text.get_rect()
        o_text_rect.center = self.WIDTH-250, self.HEIGHT-150
        press_any_key = self.font_size_15.render('Press any key to continue', True, (255, 255, 255))
        press_key_rect = press_any_key.get_rect()
        press_key_rect.bottomleft = (self.WIDTH-200, self.HEIGHT-20)
        is_quit = False
        is_running = True
        is_continue = False
        self.is_active = True
        while is_running:
            self.screen.fill((000, 000, 000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    is_quit = True
                if event.type == pygame.KEYDOWN:
                    is_running = False
                    is_continue = True
            if not is_quit:
                self.screen.blit(g_text, g_text_rect)
                self.screen.blit(o_text, o_text_rect)
                self.screen.blit(press_any_key, press_key_rect)
                pygame.display.flip()
            else:
                pygame.quit()
                sys.exit()
        return is_continue
    def level_cleared(self):
        is_running = True
        is_quit = False
        congrats = self.font_size_30.render('Congratulations', True, (255, 255, 255))
        congrats_rect = congrats.get_rect()
        congrats_rect.center = (self.WIDTH-240, self.HEIGHT-180)
        
        win = self.font_size_20.render('You Win!', True, (000, 255, 000))
        win_rect = win.get_rect()
        win_rect.center = (self.WIDTH-240, self.HEIGHT-140)
        
        press_any_key = self.font_size_15.render('Press any key to quit!', True, (255, 255, 255))
        press_key_rect = press_any_key.get_rect()
        press_key_rect.bottomleft = (self.WIDTH-200, self.HEIGHT-20)
        
        while is_running:
            self.screen.fill((000, 000, 000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    is_quit = True
                if event.type == pygame.KEYDOWN:
                    is_running = False
                    pygame.time.wait(1500)
            self.screen.blit(press_any_key, press_key_rect)
            self.screen.blit(congrats, congrats_rect)
            self.screen.blit(win, win_rect)
            if is_quit:
                pygame.quit()
                sys.exit()
            pygame.display.flip()
        return True