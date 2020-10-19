import pygame
import random
from models import enemy


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    from models.button import button
    done = False
    player.rect.x = 0
    player.rect.y = 500  # User spawns falling
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 2  # pixels to move per step
    level = Level()
    enemy_list, plat_list, rope_list = level.create(player.level)
    jmp = button([890, 600, 60, 25], gameDisplay, (0, 0, 0), (100, 200, 50))
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
        else:
            player.climbing = False
        if keys[pygame.K_r]:
            enemy_list, plat_list, rope_list = level.create(player.level)
            player.kills = 0
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not player.jumping:
                player.control(0, 4)
        enemy_list.draw(gameDisplay)
        plat_list.draw(gameDisplay)
        rope_list.draw(gameDisplay)
        for enemy in enemy_list:
            enemy.move()
        player.gravity()  # Make sure gravity affects the player
        reset = player.update(enemy_list, plat_list, rope_list)  # Update player position
        if player.lives == 0:
            return False
        elif reset is True:
            player.rect.x = 0
            player.rect.y = 500
            enemy_list, plat_list, rope_list = level.create(player.level)
        player_list.draw(gameDisplay)  # Redraw player
        if player.jump_cd > 0 or player.jumping:
            jmp.draw((255, 0, 0))
        else:
            jmp.draw()
        jmp.addText('Jump', 15)
        pygame.display.flip()  # Redraw screen with all objects in new position
        clock.tick(60)  # 60 fps speed
    print(player.kills)
    return done


class Level():
    '''Constructs a level around the player'''
    def create(self, level):
        '''Creates the level'''
        from models import platform
        enemy_list = pygame.sprite.Group()
        plat_list = pygame.sprite.Group()
        rope_list = pygame.sprite.Group()
        if level == 0:  # tutorial
            plt = [[200, 500, 128, 4, 'placeholder1.png'], [100, 600, 64, 4, 'placeholder1.png'],
                   [300, 550, 64, 4, 'placeholder1.png']]
            loc =  [[200, 576], [400, 576]]
            rop = [[150, 250, 21, 337, 'basicRopeSprite.png']]
            for location in loc:
                e = enemy.Rat(location[0], location[1])
                enemy_list.add(e)
            for plat in plt:
                p = platform.Platform(plat[0], plat[1], plat[2], plat[3], plat[4])
                plat_list.add(p)
            for rope in rop:
                r = platform.Rope(rope[0], rope[1], rope[2], rope[3], rope[4])
                rope_list.add(r)
        return enemy_list, plat_list, rope_list
