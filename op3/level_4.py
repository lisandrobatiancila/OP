import pygame
import random

class Level_4(pygame.sprite.Sprite):
    def __init__(self, screen, WIDTH, HEIGHT):
        super(Level_4, self).__init__()
        self.screne = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.food_surf = pygame.Surface((15, 15))
        self.food_surf.fill((255, 000, 000))
        snake_x = 20 * 15
        snake_y = random.randint(0, 15)
        snake_y = snake_y * 15
        self.snake_surf = pygame.Surface((15, 15))
        self.snake_surf.fill((000, 255, 000))
        self.snake_coord = [{'x': snake_x, 'y': snake_y}, {'x': snake_x-1, 'y': snake_y}, {'x': snake_x-2, 'y': snake_y}]
        self.is_food_eaten = False
        self.snake_direction = '' # used for removing the snake
        self.is_straight_direction = ''
        self.is_player_hit = False
        
    def food_location(self):
        food_x = random.randint(5, 15) * 15
        food_y = random.randint(0, 15) * 15
        
        return {'x': food_x, 'y': food_y}
    def food_is_eaten(self):
        return self.is_food_eaten
    def update(self, food_y, food_x, player_last_pos): #get player current position as the food is eaten
        if not self.is_food_eaten:
            if len(self.snake_coord) > 0:
                if food_y > self.snake_coord[0]['y'] and food_y != self.snake_coord[0]['y']: # the y coordinates
                    new_head = {'x': self.snake_coord[0]['x'], 'y': self.snake_coord[0]['y']+1}
                    self.snake_coord.insert(0, new_head)
                    del self.snake_coord[-1]
                elif food_y < self.snake_coord[0]['y'] and food_y != self.snake_coord[0]['y']: # the x coordinates
                    new_head = {'x': self.snake_coord[0]['x'], 'y': self.snake_coord[0]['y']-1}
                    self.snake_coord.insert(0, new_head)
                    del self.snake_coord[-1]
                if food_y == self.snake_coord[0]['y']:
                    new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                    self.snake_coord.insert(0, new_head)
                    del self.snake_coord[-1]
                    
                if food_x == self.snake_coord[0]['x'] and food_y == self.snake_coord[0]['y']:
                    self.is_food_eaten = True
           
        if self.is_food_eaten:
            if len(self.snake_coord) > 0:
                if self.snake_coord[0]['y'] > player_last_pos['y'] and self.snake_direction != 'right' and self.is_straight_direction != 'straight':
                    self.snake_direction = 'up'
                if self.snake_coord[0]['y'] < player_last_pos['y'] and self.snake_direction != 'right' and self.is_straight_direction != 'straight':
                    self.snake_direction = 'down'
                
                if self.is_straight_direction == 'straight':
                    new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                    self.snake_coord.insert(0, new_head)
                    del self.snake_coord[-1]
                    diff_of_x = self.snake_coord[0]['x']- player_last_pos['x']
                    diff_of_y = self.snake_coord[0]['y']-player_last_pos['y']
                    if abs(diff_of_x) < 15 and abs(diff_of_y) < 5:
                        diff = self.snake_coord[0]['x']-player_last_pos['x']
                        if abs(diff) < 16:
                            self.is_player_hit = True
                            
                elif self.snake_direction == 'up':
                    if self.snake_coord[0]['y'] == player_last_pos['y']:
                        diff_of_x = self.snake_coord[0]['x']- player_last_pos['x']
                        if abs(diff_of_x) < 15:
                            diff = self.snake_coord[0]['x']-player_last_pos['x']
                            if abs(diff) < 16:
                                self.is_player_hit = True
                        new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                        self.snake_coord.insert(0, new_head)
                        del self.snake_coord[-1]
                        self.is_straight_direction = 'straight'
                        
                    else:
                        diff = self.snake_coord[0]['y'] - player_last_pos['y']
                        if diff < 5:
                            diff_of_x = self.snake_coord[0]['x']- player_last_pos['x']
                            if abs(diff_of_x) < 15:
                                diff = self.snake_coord[0]['x']-player_last_pos['x']
                                if abs(diff) < 16:
                                    self.is_player_hit = True
                            new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                            self.snake_coord.insert(0, new_head)
                            del self.snake_coord[-1]
                            self.is_straight_direction = 'straight'
                            
                        else:
                            new_head = {'x': self.snake_coord[0]['x'], 'y': self.snake_coord[0]['y']-5}
                            self.snake_coord.insert(0, new_head)
                            del self.snake_coord[-1]
                
                elif self.snake_direction == 'down':
                    if self.snake_coord[0]['y'] == player_last_pos['y']:
                        diff_of_x = self.snake_coord[0]['x']- player_last_pos['x']
                        if abs(diff_of_x) < 15:
                            diff = self.snake_coord[0]['x']-player_last_pos['x']
                            if abs(diff) < 16:
                                self.is_player_hit = True
                                new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                                self.snake_coord.insert(0, new_head)
                                del self.snake_coord[-1]
                                self.is_straight_direction = 'straight'
                        else:
                            new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                            self.snake_coord.insert(0, new_head)
                            del self.snake_coord[-1]
                            self.is_straight_direction = 'straight'
                        
                    else:
                        diff =  player_last_pos['y'] - self.snake_coord[0]['y']
                        if diff < 5:
                            diff_of_x = self.snake_coord[0]['x']- player_last_pos['x']
                            if abs(diff_of_x) < 15:
                                diff = self.snake_coord[0]['x']-player_last_pos['x']
                                if abs(diff) < 16:
                                    self.is_player_hit = True
                                    new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                                    self.snake_coord.insert(0, new_head)
                                    del self.snake_coord[-1]
                                    self.is_straight_direction = 'straight'
                            else:
                                new_head = {'x': self.snake_coord[0]['x']-5, 'y': self.snake_coord[0]['y']}
                                self.snake_coord.insert(0, new_head)
                                del self.snake_coord[-1]
                                self.is_straight_direction = 'straight'
                            
                        else:
                            new_head = {'x': self.snake_coord[0]['x'], 'y': self.snake_coord[0]['y']+5}
                            self.snake_coord.insert(0, new_head)
                            del self.snake_coord[-1]