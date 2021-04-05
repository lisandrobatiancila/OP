import pygame

class EnemyBullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT, enemy_x, enemy_y):
        super(EnemyBullet, self).__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.surface = pygame.image.load('eb2.PNG').convert()
        self.rect = pygame.Rect(self.enemy_x, self.enemy_y, self.surface.get_width(), self.surface.get_height())
    
    def update(self, is_game_over):
        if is_game_over:
            self.rect.x = -10
            self.rect.y = self.HEIGHT
            self.kill()
        
        elif not is_game_over:
            self.rect.move_ip(-5, 0)
            if self.rect.x < 0:
                self.rect.x = -10
                self.kill()
