import pygame

class EnemyBulletLevel4(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT, enemy_level_4):
        #enemy_level_4 for bullet positioning
        super(EnemyBulletLevel4, self).__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.enemy_level_4 = enemy_level_4
        bullet_x = self.enemy_level_4.rect.x-10
        bullet_y = self.enemy_level_4.rect.y
        self.surface = pygame.image.load('eb2.PNG').convert()
        self.rect = pygame.Rect(bullet_x, bullet_y, self.surface.get_width(), self.surface.get_height())
    
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.x < 0:
            self.kill()