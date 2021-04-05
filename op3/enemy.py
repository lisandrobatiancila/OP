import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, game_level):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.game_level = game_level
        super(Enemy, self).__init__()
        y_rand = random.randint(0, 20)
        enemy_x_pos = self.WIDTH-20
        enemy_y_pos = y_rand * 15
        self.up_down = random.randint(0, 2) #[if 0 up, elif 1 mid, elif 2 for down] for level 2
        if self.game_level == 1:
            self.surf = pygame.image.load('circ_antagonist.PNG').convert()
            self.rect = pygame.Rect(enemy_x_pos, enemy_y_pos, self.surf.get_width(), self.surf.get_height())
        elif self.game_level == 2:
            self.surf = pygame.image.load('enlv2.PNG').convert()
            self.rect = pygame.Rect(enemy_x_pos, enemy_y_pos, self.surf.get_width(), self.surf.get_height())
        elif self.game_level == 3:
            self.surf = pygame.image.load('enlv3.PNG').convert()
            self.rect = pygame.Rect(enemy_x_pos, enemy_y_pos, self.surf.get_width(), self.surf.get_height())
            self.direction = '' #for level 3
            if self.up_down == 0:
                self.direction = 'up'
            elif self.up_down == 1:
                self.direction = 'mid'
            elif self.up_down == 2:
                self.direction = 'down'
    def update(self):
        if self.game_level == 1:
            self.rect.move_ip(-2, 0)
            if self.rect.x < 0:
                self.kill()
        #end of level 1
        elif self.game_level == 2:
            self.rect.move_ip(-2, 0)
            if self.rect.x < 0:
                self.kill()
            if self.up_down == 0: #up
                self.rect.move_ip(0, -2)
                if self.rect.y < 0:
                    self.rect.y = 0
            elif self.up_down == 1: #mid
                pass # normal enemy
            elif self.up_down == 2: #down
                self.rect.move_ip(0, 2)
                if self.rect.y > self.HEIGHT-15:
                    self.rect.y = self.HEIGHT-15
        #end of level 2
        elif self.game_level == 3:
            self.rect.move_ip(-2, 0)
            if self.up_down == 0: #up
                if self.rect.y < 0:
                    self.direction = 'down'
                elif self.rect.y > self.HEIGHT-15:
                    self.direction = 'up'
                
                if self.direction == 'down':
                    self.rect.move_ip(0, 2)
                if self.direction == 'up':
                    self.rect.move_ip(0, -2)
            elif self.up_down == 1: #mid
                self.rect.move_ip(-2, 0)
            elif self.up_down == 2: #down
                if self.rect.y < 0:
                    self.direction = 'down'
                elif self.rect.y > self.HEIGHT-15:
                    self.direction = 'up'
                
                if self.direction == 'down':
                    self.rect.move_ip(0, 2)
                if self.direction == 'up':
                    self.rect.move_ip(0, -2)
        #end of level 3    