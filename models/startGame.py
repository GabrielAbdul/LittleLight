import pygame
import random
from models.enemy import Enemy


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 500  # User spawns falling
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 2  # pixels to move per step
    level = Level()
    enemy_list = level.create(0, [[200, 576], [400, 576]])
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
            enemy_list = level.create(0, [[200, 576], [400, 576]])
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
            enemy_list = level.create(0, [[200, 576], [400, 576]])
        player_list.draw(gameDisplay)  # Redraw player
        pygame.display.flip()  # Redraw screen with all objects in new position
        clock.tick(60)  # 60 fps speed
    return done


class Level():
    '''Constructs a level around the player'''
    def create(self, level, loc):
        '''Creates the level'''
        enemy_list = pygame.sprite.Group()
        if level == 0:  # tutorial
            for location in loc:
                enemy = Enemy(location[0], location[1], 'Sprite1hitright.png')
                enemy_list.add(enemy)
        return enemy_list
