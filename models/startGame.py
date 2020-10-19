import pygame
import random
from models import enemy


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 500  # User spawns falling
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 2  # pixels to move per step
    level = Level()
    enemy_list = level.create(player.level)
    while not done:
        gameDisplay.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_game = __import__('littlelight').pause_game
            done = pause_game(gameDisplay)
            continue
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.control(-steps, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.control(steps, 0)
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not\
        (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            player.control(0, 0)  # Wipe movement if no keys are held down
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.jump()
        if keys[pygame.K_r]:
            enemy_list = level.create(player.level)
            player.kills = 0
        enemy_list.draw(gameDisplay)
        for enemy in enemy_list:
            enemy.move()
        player.gravity()  # Make sure gravity affects the player
        reset = player.update(enemy_list)  # Update player position
        if player.lives == 0:
            return False
        elif reset is True:
            player.rect.x = 0
            player.rect.y = 500
            enemy_list = level.create(player.level)
        player_list.draw(gameDisplay)  # Redraw player
        pygame.display.flip()  # Redraw screen with all objects in new position
        clock.tick(60)  # 60 fps speed
    print(player.kills)
    return done


class Level():
    '''Constructs a level around the player'''
    def create(self, level):
        '''Creates the level'''
        enemy_list = pygame.sprite.Group()
        if level == 0:  # tutorial
            loc =  [[200, 576], [400, 576]]
            for location in loc:
                e = enemy.Rat(location[0], location[1])
                enemy_list.add(e)
        return enemy_list
