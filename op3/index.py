import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    WIDTH = 480
    HEIGHT = 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('OP3')
    game = Game(screen, WIDTH, HEIGHT)

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        game.main_game()
        pygame.display.flip()
    pygame.quit()
