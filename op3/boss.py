import pygame

class Boss(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT, current_level):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.current_level = current_level
        self.font = pygame.font.Font('freesansbold.ttf', 10)
        if self.current_level == 5:
            super(Boss, self).__init__()
            x_pos_boss = self.WIDTH-55
            y_pos_boss = self.HEIGHT-60
            self.surface = pygame.image.load('bosses/open.PNG').convert()
            self.rect = pygame.Rect(x_pos_boss, y_pos_boss, self.surface.get_width(), self.surface.get_height())
            
            x_lb_w_boss = x_pos_boss+10
            y_lb_w_boss = y_pos_boss-20
            self.life_bar_surf_w = pygame.Surface((50, 15))
            self.life_bar_surf_w.fill((255, 255, 255))
            self.life_bar_rect_w = pygame.Rect(x_lb_w_boss, y_lb_w_boss, self.life_bar_surf_w.get_width(), self.life_bar_surf_w.get_height())
            
            x_lb_r_boss = x_lb_w_boss+2
            y_lb_r_boss = y_lb_w_boss+3
            self.life_bar_surf_r = pygame.Surface((45, 10))
            self.life_bar_surf_r.fill((255, 000, 000))
            self.life_bar_rect_r = pygame.Rect(x_lb_r_boss, y_lb_r_boss, self.life_bar_surf_r.get_width(), self.life_bar_surf_r.get_height())
            
            self.boss_life = 50
            self.life_no = self.font.render(f'{self.boss_life}/50', True, (000, 000, 000))
            self.life_no_rect = pygame.Rect(x_lb_r_boss+10, y_lb_r_boss, self.life_bar_surf_r.get_width(), self.life_bar_surf_r.get_height())
            
            self.right = 'right'
            self.top = 'top'
            self.left = 'left'
            self.bottom = 'bottom'
            self.direction = ''
            self.boss_prev_direction = ''
            self.prev_rect = False
    
    def collission_bullet(self, collisions):
        #collisions a dictionary {key: 'bullet', value: 'bullet_obj'}
        key = collisions['key']
        is_hit = False
        if key == 'bullet':
            player_bullet_group = collisions['value']#player_bullet_group
            for pbg in player_bullet_group:
                diff_x = self.rect.centerx-pbg.rect.centerx
                diff_y = self.rect.centery-pbg.rect.centery
                if abs(diff_x) < self.rect.height and abs(diff_y) < self.rect.width:
                    pbg.kill()
                    is_hit = True
                    break
        return is_hit
    def collission_ship(self, collisions):
        #{'key': 'ship', value: 'ship_obj'}
        key = collisions['key']
        if key == 'ship':
            player = collisions['value']#player
            diff_x = self.rect.centerx-player.rect.centerx
            diff_y = self.rect.centery-player.rect.centery
            if abs(diff_x) < self.rect.height and abs(diff_y) < self.rect.width:
                return True
            else:
                return
    def update(self, new_life, boss_move):
        if self.current_level == 5:
            self.life_no = self.font.render(f'{self.boss_life}/50', True, (000, 000, 000))
            self.life_no_rect = pygame.Rect(self.life_bar_rect_r.x+10, self.life_bar_rect_r.y, self.life_bar_surf_r.get_width(), self.life_bar_surf_r.get_height())
            if boss_move == 'forward':
                if self.rect.x > 3:
                    self.life_bar_rect_w.move_ip(-3, 0)
                    self.life_bar_rect_r.move_ip(-3, 0)
                    self.life_no_rect.move_ip(-3, 0)
                    self.rect.move_ip(-3, 0)
                    self.boss_prev_direction = 'forward'
            elif boss_move == 'backward':
                if self.rect.x < self.WIDTH-55:
                    self.life_bar_rect_w.move_ip(3, 0)
                    self.life_bar_rect_r.move_ip(3, 0)
                    self.life_no_rect.move_ip(3, 0)
                    self.rect.move_ip(3, 0)
                    self.boss_prev_direction = 'backward'
            elif boss_move == 'plain_attack':
                if self.life_bar_rect_w.y == self.HEIGHT-80: #[from bottom to top]
                    self.direction = self.top
                if self.life_bar_rect_w.y == 22: #[from top to bottom]
                    self.direction = self.bottom
                
                if self.direction == self.top:
                    self.life_bar_rect_w.move_ip(0, -3)
                    self.life_bar_rect_r.move_ip(0, -3)
                    self.life_no_rect.move_ip(0, -3)
                    self.rect.move_ip(0, -3)
                    self.boss_prev_direction = ''
                elif self.direction == self.bottom:
                    self.life_bar_rect_w.move_ip(0, 3)
                    self.life_bar_rect_r.move_ip(0, 3)
                    self.life_no_rect.move_ip(0, 3)
                    self.rect.move_ip(0, 3)
                    self.boss_prev_direction = ''
        #end of boss level 5