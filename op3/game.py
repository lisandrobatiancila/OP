import pygame
import sys
import random
from player import Player
from player_bullet import PlayerBullet
from enemy import Enemy
from enemy_bullet import EnemyBullet
from response import Response
from level_4 import Level_4
from nmy_level_4 import EnemyLevel4
from nmy_bullet_level_4 import EnemyBulletLevel4
from back_ground import BackGround
from boss import Boss

class Game:
    def __init__(self, screen, WIDTH, HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
    def main_game(self):
        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
        back_ground_group = pygame.sprite.Group()
        ADD_BACK_GROUND = pygame.USEREVENT+5
        pygame.time.set_timer(ADD_BACK_GROUND, 1000)
        
        player = Player(self.WIDTH, self.HEIGHT)
        player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
        player_bullet_group = pygame.sprite.Group()
        #enemy
        enemy = Enemy(self.WIDTH, self.HEIGHT, 1)
        enemy_group = pygame.sprite.Group()
        enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, enemy.rect.x, enemy.rect.y)
        enemy_bullet_group = pygame.sprite.Group()
                
        ENEMY_ADD = pygame.USEREVENT+1
        ENEMY_BULLET = pygame.USEREVENT+2
        pygame.time.set_timer(ENEMY_ADD, 1500)#enemy ship
        pygame.time.set_timer(ENEMY_BULLET, 2500)#enemy bullet
        
        level_4 = Level_4(self.screen, self.WIDTH, self.HEIGHT)
        ADD_SNAKE = pygame.USEREVENT+3
        pygame.time.set_timer(ADD_SNAKE, 2000)
        level_4_group = pygame.sprite.Group()
        food_location = None
        is_first_run = True
        food_is_eaten = True #true by default so that it can be blitted
        food_life_span = 3
        snake_coord = []
        player_last_pos = {'x': 0, 'y': 0}
        hit_counter = 0
        enemy_level_4 = EnemyLevel4(self.screen, self.WIDTH, self.HEIGHT)
        eb_lvl_4 = EnemyBulletLevel4(self.screen, self.WIDTH, self.HEIGHT, enemy_level_4)
        ENEMY_LEVEL_4 = pygame.USEREVENT+1
        EB_LVL_4 = pygame.USEREVENT+2
        pygame.time.set_timer(ENEMY_LEVEL_4, 1500)
        pygame.time.set_timer(EB_LVL_4, 2500)
        enemy_level_4_group = pygame.sprite.Group()
        eb_lvl_4_group = pygame.sprite.Group()
        
        key_pressed = None #player actions
        is_running = True
        frame_tick = pygame.time.Clock()
        created_enemies = []
        response = Response(self.screen, self.WIDTH, self.HEIGHT)
        response.game_title()
        boss = Boss(self.screen, self.WIDTH, self.HEIGHT, 5)
        boss_bullet_group = pygame.sprite.Group()
        boss_move = 'plain_attack'
        is_player_hit = True
        BOSS_FIRE_EVENT = pygame.USEREVENT+1
        pygame.time.set_timer(BOSS_FIRE_EVENT, 1000)#boss will fire
        BOSS_ADD_ENEMY = pygame.USEREVENT+2
        pygame.time.set_timer(BOSS_ADD_ENEMY, 3000)#boss add enemy
        BOSS_ATTACK = pygame.USEREVENT+3
        pygame.time.set_timer(BOSS_ATTACK, 5000)#boss move forward
        
        game_current_level = 1 #set to 1
        game_current_score = 0 #set to 0
        check_score = True #check user score for leveling purposes.
        is_game_over = False
        while is_running:
            self.screen.fill((000, 000, 000))
            if check_score:
                if game_current_level == 1: # for level 1
                    game_current_score = 0
                    created_enemies = []
                    player_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                elif game_current_level == 2: # for level 2
                    game_current_score = 0
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    player_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                elif game_current_level == 3: # for level 3
                    game_current_score = 0
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    player_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                elif game_current_level == 4: # for level 4
                    game_current_score = 0
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    player_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                elif game_current_level == 5: # for level 5
                    game_current_score = 0
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    for ebg in enemy_bullet_group:
                        ebg.kill()
                    is_player_hit = True
                    created_enemies = []
                    player_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    level_4_group.remove()
                    food_location = {}
            #end of checking user score
            if game_current_level == 1:
                if response.is_active:
                    response.levels(game_current_level)
                    response.is_active = False
                    check_score = False #check user score for leveling purposes.
                    
                #self.game_grid()
                response.scores(game_current_score) #player scores
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                    if event.type == ADD_BACK_GROUND:
                        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
                        back_ground_group.add(back_ground)
                    if event.type == pygame.KEYDOWN:
                        key_pressed = event.key
                        if key_pressed == pygame.K_f:
                            player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
                            player_bullet_group.add(player_bullet)
                    #add enemy for 250 s
                    if event.type == ENEMY_ADD:
                        enemy = Enemy(self.WIDTH, self.HEIGHT, 1)
                        enemy_group.add(enemy)
                        created_enemies.append(enemy)
                        is_game_over = False
                    if event.type == ENEMY_BULLET:
                        for ce in created_enemies:
                            if ce != None:
                                if ce.rect.x < 0:
                                    ce.kill()
                                else:
                                    enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, ce.rect.x, ce.rect.y)
                                    enemy_bullet_group.add(enemy_bullet)
                for bgg in back_ground_group:
                    self.screen.blit(bgg.surface, bgg.rect)
                self.screen.blit(player.surf, player.rect) #player ship
                player.update(key_pressed) # player-movement
                for pbg in player_bullet_group:
                    self.screen.blit(pbg.surface, pbg.rect)
                #enemy
                for eg in enemy_group:
                    self.screen.blit(eg.surf, eg.rect)
                for ebg in enemy_bullet_group:
                    self.screen.blit(ebg.surface, ebg.rect)
                if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
                    pass #bullet hit other bullets
                if pygame.sprite.groupcollide(player_bullet_group, enemy_group, False, False):
                    game_current_score = game_current_score+1
                    if game_current_score == 20:
                        response.is_active = True
                        check_score = True
                        game_current_level = 2
                    #player bullet hit enemy
                    hit = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False)
                    index = 0
                    if len(created_enemies) > 0:
                        is_found = False
                        for h in hit:
                            if h in created_enemies:
                                index = created_enemies.index(h)
                                is_found = True
                                break
                        if is_found:
                            created_enemies[index].rect.x = -10
                            created_enemies[index].kill()
                            created_enemies[index] = None
                if pygame.sprite.spritecollideany(player, enemy_bullet_group):
                    #player was hit by enemy bullets
                    game_current_score = 0
                    game_current_level = 1
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()#player was hit by an enemy
                    response.levels(game_current_level)
                if pygame.sprite.spritecollideany(player, enemy_group):
                    #player hit group of enemies
                    game_current_score = 0
                    game_current_level = 1
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()#print('object hit object')
                    response.levels(game_current_level)
                back_ground_group.update()
                player_bullet_group.update()
                enemy_group.update()
                enemy_bullet_group.update(is_game_over)
            #end of level 1
            elif game_current_level == 2:
                if response.is_active:
                    response.levels(game_current_level)
                    response.is_active = False
                    check_score = False #check user score for leveling purposes.
                    
                #self.game_grid()
                response.scores(game_current_score)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                    if event.type == ADD_BACK_GROUND:
                        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
                        back_ground_group.add(back_ground)
                    if event.type == pygame.KEYDOWN:
                        key_pressed = event.key
                        if event.key == pygame.K_f:
                            player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
                            player_bullet_group.add(player_bullet)
                    if event.type == ENEMY_ADD:
                        enemy = Enemy(self.WIDTH, self.HEIGHT, 2)
                        enemy_group.add(enemy)
                        created_enemies.append(enemy)
                        is_game_over = False
                    if event.type == ENEMY_BULLET:
                        for ce in created_enemies:
                            if ce != None:
                                if ce.rect.x < 0:
                                    ce.kill()
                                else:
                                    enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, ce.rect.x, ce.rect.y)
                                    enemy_bullet_group.add(enemy_bullet)
                for bgg in back_ground_group:
                    self.screen.blit(bgg.surface, bgg.rect)
                self.screen.blit(player.surf, player.rect)
                player.update(key_pressed)
                for pbg in player_bullet_group:
                    self.screen.blit(pbg.surface, pbg.rect)
                for eg in enemy_group:
                    self.screen.blit(eg.surf, eg.rect)
                for ebg in enemy_bullet_group:
                    self.screen.blit(ebg.surface, ebg.rect)
                if pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False):
                    #player hit enemy
                    game_current_score = game_current_score+1
                    if game_current_score == 20:
                        response.is_active = True
                        check_score = True
                        game_current_level = 3
                    hit = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False)
                    index = 0
                    for h in hit:
                        index = created_enemies.index(h)
                        break
                    created_enemies[index].rect.x = -10
                    created_enemies[index].kill()
                    created_enemies[index] = None
                if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
                    #player bullet hit enemy bullet
                    pass
                if pygame.sprite.spritecollideany(player, enemy_bullet_group):
                    #player was hit by enemy
                    game_current_score = 0
                    game_current_level = 2
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                if pygame.sprite.spritecollideany(player, enemy_group):
                    #object hit object
                    game_current_score = 0
                    game_current_level = 2
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                back_ground_group.update()
                player_bullet_group.update()
                enemy_bullet_group.update(is_game_over)
                enemy_group.update()
            #end of level 2
            elif game_current_level == 3:
                if response.is_active:
                    response.levels(game_current_level)
                    response.is_active = False
                    check_score = False #check user score for leveling purposes.
                    
                #self.game_grid()
                response.scores(game_current_score)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                    if event.type == ADD_BACK_GROUND:
                        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
                        back_ground_group.add(back_ground)
                    if event.type == pygame.KEYDOWN:
                        key_pressed = event.key
                        if event.key == pygame.K_f:
                            player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
                            player_bullet_group.add(player_bullet)
                    if event.type == ENEMY_ADD:
                        enemy = Enemy(self.WIDTH, self.HEIGHT, 3)
                        enemy_group.add(enemy)
                        created_enemies.append(enemy)
                        is_game_over = False
                    if event.type == ENEMY_BULLET:
                        for ce in created_enemies:
                            if ce != None:
                                if ce.rect.x < 0:
                                    ce.kill()
                                else:
                                    enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, ce.rect.x, ce.rect.y)
                                    enemy_bullet_group.add(enemy_bullet)
                for bgg in back_ground_group:
                    self.screen.blit(bgg.surface, bgg.rect)
                self.screen.blit(player.surf, player.rect)
                player.update(key_pressed)
                for pbg in player_bullet_group:
                    self.screen.blit(pbg.surface, pbg.rect)
                for eg in enemy_group:
                    self.screen.blit(eg.surf, eg.rect)
                for ebg in enemy_bullet_group:
                    self.screen.blit(ebg.surface, ebg.rect)
                
                if pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False):
                    #player bullet hit enemy
                    game_current_score = game_current_score+1
                    if game_current_score == 20:
                        response.is_active = True
                        check_score = True
                        game_current_level = 4
                    hit = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False)
                    index = 0
                    for h in hit:
                        index = created_enemies.index(h)
                        break
                    created_enemies[index].rect.x = -10
                    created_enemies[index].kill()
                    created_enemies[index] = None
                if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
                    #player bullet hit enemy bullet
                    pass
                if pygame.sprite.spritecollideany(player, enemy_group):
                    #object hit object
                    game_current_score = 0
                    game_current_level = 3
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                if pygame.sprite.spritecollideany(player, enemy_bullet_group):
                    #player was hit by enemy
                    game_current_score = 0
                    game_current_level = 3
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    created_enemies = []
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    player_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                back_ground_group.update()
                enemy_group.update()
                enemy_bullet_group.update(is_game_over)
                player_bullet_group.update()
            #end of level 3
            elif game_current_level == 4:
                if response.is_active:
                    response.levels(game_current_level)
                    response.is_active = False
                    check_score = False #check user score for leveling purposes.
                    food_location = level_4.food_location()
                    
                #self.game_grid()
                response.scores(game_current_score) #player scores
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                    if event.type == ADD_BACK_GROUND:
                        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
                        back_ground_group.add(back_ground)
                    if event.type == pygame.KEYDOWN:
                        key_pressed = event.key
                        if event.key == pygame.K_f:
                            player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
                            player_bullet_group.add(player_bullet)
                    if event.type == ENEMY_LEVEL_4:
                        enemy_level_4 = EnemyLevel4(self.screen, self.WIDTH, self.HEIGHT)
                        enemy_level_4_group.add(enemy_level_4)
                        created_enemies.append(enemy_level_4)
                    if event.type == EB_LVL_4:
                        for ce in created_enemies:
                            if ce != None:
                                if ce.rect.x < 0:
                                    ce.kill()
                                else:
                                    eb_lvl_4 = EnemyBulletLevel4(self.screen, self.WIDTH, self.HEIGHT, ce)
                                    eb_lvl_4_group.add(eb_lvl_4)
                    if event.type == ADD_SNAKE:
                        if len(snake_coord) == 0 and food_is_eaten:
                            level_4 = Level_4(self.screen, self.WIDTH, self.HEIGHT)
                            level_4_group.add(level_4)
                            food_location = level_4.food_location()
                            food_life_span = 3
                            food_is_eaten = False
                            hit_counter = 0
                        else:
                            if len(level_4.snake_coord) > 0 and level_4.snake_coord[0]['x'] < 0 and food_is_eaten:
                                level_4 = Level_4(self.screen, self.WIDTH, self.HEIGHT)
                                level_4_group.add(level_4)
                                food_location = level_4.food_location()
                                food_life_span = 3
                                food_is_eaten = False
                                hit_counter = 0
                        
                        if is_first_run and food_is_eaten:
                            level_4 = Level_4(self.screen, self.WIDTH, self.HEIGHT)
                            level_4_group.add(level_4)
                            food_life_span = 3
                            food_is_eaten = False
                            is_first_run = False
                            hit_counter = 0
                for bgg in back_ground_group:
                    self.screen.blit(bgg.surface, bgg.rect)
                self.screen.blit(player.surf, player.rect)
                player.update(key_pressed)
                for pbg in player_bullet_group:
                    self.screen.blit(pbg.surface, pbg.rect)
                self.screen.blit(level_4.food_surf, (food_location['x'], food_location['y'], level_4.food_surf.get_width(), level_4.food_surf.get_height()))
                for l4g in level_4_group:
                    snake_coord = l4g.snake_coord
                    for sc in snake_coord:
                        self.screen.blit(l4g.snake_surf, (sc['x'], sc['y'], l4g.snake_surf.get_width(), l4g.snake_surf.get_height()))
                for el4g in enemy_level_4_group:
                    self.screen.blit(el4g.surface, el4g.rect)
                for ebl4g in eb_lvl_4_group:
                    self.screen.blit(ebl4g.surface, ebl4g.rect)
                    
                food_is_eaten = level_4.food_is_eaten()
                if food_is_eaten:
                    player_last_pos = {'x': player.rect.x, 'y': player.rect.y}
                    
                level_4_group.update(food_location['y'], food_location['x'], player_last_pos)
                player_bullet_group.update()
                for pbg in player_bullet_group:
                    diff_x = food_location['x']-pbg.rect.x
                    diff_y = 0
                    if food_location['y'] > pbg.rect.y:
                        diff_y = food_location['y']-pbg.rect.y
                    elif food_location['y'] < pbg.rect.y:
                        diff_y = pbg.rect.y-food_location['y']
                    if diff_x < 5 and diff_y < 7:
                        food_life_span = food_life_span - 1
                        pbg.kill()
                #player destroyed snake food
                if food_life_span == 0:
                    hit_counter = hit_counter+1
                    if hit_counter > 0 and hit_counter < 2:
                        game_current_score = game_current_score+1
                        food_location = {'x': -100, 'y': 0}
                        new_head = {'x': -20, 'y': -5}
                        level_4.snake_coord.insert(0, new_head)
                        snake_coord = []
                        food_is_eaten = True
                        level_4_group.remove()
                #check if player was eaten/destroyed by snake
                if len(snake_coord) > 0:
                    if level_4.is_player_hit:
                        hit_counter = hit_counter+1
                        if hit_counter > 0 and hit_counter < 2:
                            #print('player was eaten')
                            game_current_score = 0
                            game_current_level = 4
                            is_game_over = True
                            player.rect.x = 0
                            player.rect.y = 0
                            player.direction = 'down'
                            for ce in created_enemies:
                                if ce != None:
                                    ce.rect.x = -10
                                    ce.kill()
                            for pbg in player_bullet_group:
                                pbg.kill()
                            for ebl4 in eb_lvl_4_group:
                                ebl4.kill()
                            food_is_eaten = True
                            level_4.snake_coord = []
                            snake_coord = []
                            created_enemies = []
                            level_4_group.remove()
                            eb_lvl_4_group.remove()
                            player_bullet_group.remove()
                            response.game_over()
                            response.levels(game_current_level)
                #check if player bullet hit enemy bullet
                if pygame.sprite.groupcollide(player_bullet_group, eb_lvl_4_group, True, True):
                    pass
                #check if player bullet hit an enemy
                if pygame.sprite.groupcollide(enemy_level_4_group, player_bullet_group, False, False):
                    game_current_score = game_current_score+1
                    hit = pygame.sprite.groupcollide(enemy_level_4_group, player_bullet_group, False, False)
                    index = 0
                    for h in hit:
                        index = created_enemies.index(h)
                        break
                    created_enemies[index].rect.x = -10
                    created_enemies[index].kill()
                    created_enemies[index] = None
                #check if player object hit enemy object
                if pygame.sprite.spritecollideany(player, enemy_level_4_group):
                    game_current_score = 0
                    game_current_level = 4
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    for ebl4 in eb_lvl_4_group:
                        ebl4.kill()
                    food_is_eaten = True
                    level_4.snake_coord = []
                    snake_coord = []
                    created_enemies = []
                    level_4_group.remove()
                    eb_lvl_4_group.remove()
                    player_bullet_group.remove()
                    response.game_over()#print('object hit object')
                    response.levels(game_current_level)
                #check if player hit by enemy bullet
                if pygame.sprite.spritecollideany(player, eb_lvl_4_group):
                    game_current_score = 0
                    game_current_level = 4
                    is_game_over = True
                    player.rect.x = 0
                    player.rect.y = 0
                    player.direction = 'down'
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    for pbg in player_bullet_group:
                        pbg.kill()
                    for ebl4 in eb_lvl_4_group:
                        ebl4.kill()
                    food_is_eaten = True
                    level_4.snake_coord = []
                    snake_coord = []
                    created_enemies = []
                    level_4_group.remove()
                    eb_lvl_4_group.remove()
                    player_bullet_group.remove()
                    response.game_over()#print('object hit object')
                    response.levels(game_current_level)
                if game_current_score == 20:
                    response.is_active = True
                    check_score = True
                    game_current_level = 5
                back_ground_group.update()
                enemy_level_4_group.update()
                eb_lvl_4_group.update()
            #end level 4                
            elif game_current_level == 5:
                if response.is_active:
                    response.levels(game_current_level)
                    response.is_active = False
                    check_score = False #check user score for leveling purposes.
                    
                #self.game_grid()
                for bgg in back_ground_group:
                    self.screen.blit(bgg.surface, bgg.rect)
                response.scores(game_current_score) #player scores
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_running = False
                    if event.type == ADD_BACK_GROUND:
                        back_ground = BackGround(self.screen, self.WIDTH, self.HEIGHT)
                        back_ground_group.add(back_ground)
                    if event.type == BOSS_FIRE_EVENT:
                        enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, boss.rect.x, boss.rect.y)
                        boss_bullet_group.add(enemy_bullet)
                    if event.type == BOSS_ADD_ENEMY:
                        type_of_enemy = random.randint(1, 3)#[1 for level 1, 2 for level 2, 3 for level 3]
                        enemy = Enemy(self.WIDTH, self.HEIGHT, type_of_enemy)
                        enemy_group.add(enemy)
                        created_enemies.append(enemy)
                    if event.type == ENEMY_BULLET:
                        for ce in created_enemies:
                            if ce != None:
                                if ce.rect.x < 0:
                                    ce.kill()
                                else:
                                    enemy_bullet = EnemyBullet(self.screen, self.WIDTH, self.HEIGHT, ce.rect.x, ce.rect.y)
                                    enemy_bullet_group.add(enemy_bullet)
                            
                    if event.type == BOSS_ATTACK:
                        if boss.boss_prev_direction == '':
                            boss_move = 'forward'
                        elif boss.boss_prev_direction == 'forward':
                            boss_move = 'backward'
                        elif boss.boss_prev_direction == 'backward':
                            boss_move = 'plain_attack'
                    if event.type == pygame.KEYDOWN:
                        key_pressed = event.key
                        if event.key == pygame.K_f:
                            player_bullet = PlayerBullet(self.screen, self.WIDTH, self.HEIGHT, player)
                            player_bullet_group.add(player_bullet)
                self.screen.blit(boss.life_bar_surf_w, boss.life_bar_rect_w)#boss
                self.screen.blit(boss.life_bar_surf_r, boss.life_bar_rect_r)#boss
                self.screen.blit(boss.life_no, boss.life_no_rect)#boss
                self.screen.blit(boss.surface, boss.rect)#boss
                self.screen.blit(player.surf, player.rect)#player
                
                for bbg in boss_bullet_group:
                    self.screen.blit(bbg.surface, bbg.rect)
                for eg in enemy_group:
                    self.screen.blit(eg.surf, eg.rect)
                for ebg in enemy_bullet_group:
                    self.screen.blit(ebg.surface, ebg.rect)
                for pbg in player_bullet_group:
                    self.screen.blit(pbg.surface, pbg.rect)
                if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
                    pass #check if player bullet hit enemy bullet
                if pygame.sprite.groupcollide(player_bullet_group, boss_bullet_group, True, True):
                    pass #check if player bullet hit boss bullet
                if pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False):
                    game_current_score = game_current_score+1
                    hit = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, False)
                    index = 0
                    for h in hit:
                        index = created_enemies.index(h)
                        break
                    created_enemies[index].rect.x = -10
                    created_enemies[index].kill()
                    created_enemies[index] = None
                if boss.collission_bullet({'key': 'bullet', 'value': player_bullet_group}):
                    game_current_score = game_current_score+1
                    boss.boss_life = boss.boss_life-1
                    if boss.boss_life == 0:
                        boss.boss_life = 0
                        if response.level_cleared():
                            is_running = False
                if boss.collission_ship({'key': 'ship', 'value': player}):
                    if is_player_hit: #player collide boss
                        is_player_hit = False
                        boss.rect.x = boss.WIDTH-55
                        boss.life_bar_rect_w.x = boss.rect.x+10
                        boss.life_bar_rect_r.x = boss.life_bar_rect_w.x+2
                        boss.life_no_rect = boss.life_bar_rect_r.x+10
                        boss.boss_life = 50
                        game_current_score = 0
                        game_current_level = 5
                        for ce in created_enemies:
                            if ce != None:
                                ce.rect.x = -10
                                ce.kill()
                        created_enemies = []
                        for pbg in player_bullet_group:
                            pbg.kill()
                        player_bullet_group.remove()
                        for bbg in boss_bullet_group:
                            bbg.kill()
                        boss_bullet_group.remove()
                        enemy_group.remove()
                        enemy_bullet_group.remove()
                        response.game_over()
                        response.levels(game_current_level)
                        is_player_hit = True
                if pygame.sprite.spritecollide(player, enemy_group, True):
                    #if enemy_group collide to player
                    boss.rect.x = boss.WIDTH-55
                    boss.life_bar_rect_w.x = boss.rect.x+10
                    boss.life_bar_rect_r.x = boss.life_bar_rect_w.x+2
                    boss.life_no_rect = boss.life_bar_rect_r.x+10
                    boss.boss_life = 50
                    game_current_score = 0
                    game_current_level = 5
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    created_enemies = []
                    for pbg in player_bullet_group:
                        pbg.kill()
                    player_bullet_group.remove()
                    for bbg in boss_bullet_group:
                        bbg.kill()
                    boss_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                    is_player_hit = True
                if pygame.sprite.spritecollide(player, enemy_bullet_group, True):
                    #if enemy bullet hit player
                    boss.rect.x = boss.WIDTH-55
                    boss.life_bar_rect_w.x = boss.rect.x+10
                    boss.life_bar_rect_r.x = boss.life_bar_rect_w.x+2
                    boss.life_no_rect = boss.life_bar_rect_r.x+10
                    boss.boss_life = 50
                    game_current_score = 0
                    game_current_level = 5
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    created_enemies = []
                    for pbg in player_bullet_group:
                        pbg.kill()
                    player_bullet_group.remove()
                    for bbg in boss_bullet_group:
                        bbg.kill()
                    boss_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    response.game_over()
                    response.levels(game_current_level)
                    is_player_hit = True
                if pygame.sprite.spritecollide(player, boss_bullet_group, True):
                    #if boss bullet hit player
                    boss.rect.x = boss.WIDTH-55
                    boss.life_bar_rect_w.x = boss.rect.x+10
                    boss.life_bar_rect_r.x = boss.life_bar_rect_w.x+2
                    boss.life_no_rect = boss.life_bar_rect_r.x+10
                    boss.boss_life = 50
                    game_current_score = 0
                    game_current_level = 5
                    for ce in created_enemies:
                        if ce != None:
                            ce.rect.x = -10
                            ce.kill()
                    created_enemies = []
                    for pbg in player_bullet_group:
                        pbg.kill()
                    player_bullet_group.remove()
                    for bbg in boss_bullet_group:
                        bbg.kill()
                    boss_bullet_group.remove()
                    enemy_group.remove()
                    enemy_bullet_group.remove()
                    response.game_over()#print('object hit object')
                    response.levels(game_current_level)
                    is_player_hit = True
                enemy_group.update()
                boss_bullet_group.update(False)
                enemy_bullet_group.update(False)
                boss.update(50, boss_move)
                back_ground_group.update()
                player.update(key_pressed)
                player_bullet_group.update()
            #end level 5
            frame_tick.tick(30)
            pygame.display.flip()
        if not is_running:
            pygame.quit()
            sys.exit()
            
    def game_grid(self):
        grid_color = (170, 170, 000)
        for x in range(0, self.WIDTH-5, 15):
            pygame.draw.line(self.screen, grid_color, (0, x), (self.WIDTH, x))
        
        for y in range(0, self.WIDTH-5, 15):
            pygame.draw.line(self.screen, grid_color, (y, 0), (y, self.HEIGHT))