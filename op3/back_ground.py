import pygame
import random

class BackGround(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT):
        super(BackGround, self).__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        astrd_x = 30 * 15
        astrd_y = random.randint(0, 15) * 15
        asteroids = ['background/atrd0.PNG', 'background/atrd1.PNG', 'background/atrd2.PNG']
        asteroids_rand = random.randint(0, len(asteroids)-1)
        
        self.surface = pygame.image.load(asteroids[asteroids_rand]).convert()
        self.rect = pygame.Rect(astrd_x, astrd_y, self.surface.get_width(), self.surface.get_height())
        
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.x < 0:
            self.kill()