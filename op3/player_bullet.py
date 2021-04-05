import pygame

class PlayerBullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, WIDTH, HEIGHT, player):
        super(PlayerBullet, self).__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player = player
        self.surface = pygame.image.load('pb2.PNG').convert()
        self.rect = pygame.Rect(self.player.rect.x+10, self.player.rect.y+3, self.surface.get_width(), self.surface.get_height())
        
    def update(self):
        self.rect.move_ip(3, 0)
        if self.rect.x > self.WIDTH:
            self.kill()