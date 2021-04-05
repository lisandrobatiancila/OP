import pygame
from pygame.locals import(
    K_RIGHT,
    K_UP,
    K_LEFT,
    K_DOWN,
    K_d,
    K_w,
    K_a,
    K_s
    )

class Player(pygame.sprite.Sprite):
    
    def __init__(self, WIDTH, HEIGHT):
        super(Player, self).__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.surf = pygame.image.load('circ_protagonist.PNG').convert()
        self.rect = pygame.Rect(0, 0, self.surf.get_width(), self.surf.get_height())
        self.right = 'right'
        self.top = 'top'
        self.left = 'left'
        self.down = 'down'
        self.direction = self.down
        
    def update(self, key_pressed):
        if key_pressed == K_RIGHT or key_pressed == K_d:
            self.direction = self.right
        elif key_pressed == K_UP or key_pressed == K_w:
            self.direction = self.top
        elif key_pressed == K_LEFT or key_pressed == K_a:
            self.direction = self.left
        elif key_pressed == K_DOWN or key_pressed == K_s:
            self.direction = self.down
        
        if self.direction == self.right:
            if self.direction == self.right and key_pressed == pygame.K_f:
                self.rect.move_ip(2, 0)
            else:
                self.rect.move_ip(3, 0)
        if self.direction == self.top:
            self.rect.move_ip(0, -3)
        if self.direction == self.left:
            self.rect.move_ip(-3, 0)
        if self.direction == self.down:
            self.rect.move_ip(0, 3)
        
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > self.WIDTH-15:
            self.rect.x = self.WIDTH-15
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > self.HEIGHT-15:
            self.rect.y = self.HEIGHT-15