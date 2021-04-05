import pygame
import random

class EnemyLevel4(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT):
        super(EnemyLevel4, self).__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        x_rand = self.WIDTH-10
        y_rand = random.randint(0, 15) * 15
        self.surface = pygame.image.load('enlvl4.PNG').convert()
        self.rect = pygame.Rect(x_rand, y_rand, self.surface.get_width(), self.surface.get_height())
    
    def update(self):
        self.rect.move_ip(-2, 0)
        if self.rect.x < 0:
            self.kill()