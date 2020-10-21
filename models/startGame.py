import pygame
import random
from models import enemy
from models.achievements import *


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    from models.button import button
    achievements = create_achievements()
    achieve = achievement()
    done = False
    player_list = pygame.sprite.Group()
    player_list.add(player)
    baseSteps = 2
    steps = 2  # pixels to move per step
    level = Level(gameDisplay)
    enemy_list, plat_list, rope_list, backdrop, candle = level.create(player)
    jmp = button([890, 600, 60, 25], gameDisplay, (0, 0, 0), (100, 200, 50))
    while not done:
        # checking for player stats and granting achievements based on them
        if player.strength >= 30:
            granted = achieve.grant_achievement(player, achievements[1])
            if granted == 1:
                print("Achievement {} Unlocked!".format(achievements[1]))
        if player.randomInt == 50:
            granted = achieve.grant_achievement(player, achievements[0])
            if granted == 1:
                print("Achievement {} Unlocked!".format(achievements[0]))
        if player.glow >= 10:
            granted = achieve.grant_achievement(player, achievements[3])
            if granted == 1:
                print("Achievement {} Unlocked!".format(achievements[3]))
        if player.glow < 2:
            granted = achieve.grant_achievement(player, achievements[2])
            if granted == 1:
                print("Achievement {} Unlocked!".format(achievements[2]))
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(backdrop, (0, 0))
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
            steps = baseSteps + 2
        else:
            player.climbing = False
        if keys[pygame.K_r]:
            enemy_list, plat_list, rope_list, backdrop, candle = level.create(player)
            player.kills = 0
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not player.jumping:
                player.control(0, 4)
                player.rect.y += 1
        if keys[pygame.K_l]:
            if candle.colliderect(player.rect):
                player.lighting = True
        if not candle.colliderect(player.rect):
            player.lighting = False
        if not player.jumping:
            steps = baseSteps
        enemy_list.draw(gameDisplay)
        plat_list.draw(gameDisplay)
        rope_list.draw(gameDisplay)
        for enemy in enemy_list:
            enemy.move(plat_list)
        player.gravity()  # Make sure gravity affects the player
        reset = player.update(enemy_list, plat_list, rope_list)  # Update player position
        if player.litCandle and player.rect.right >= 950 and player.rect.top >= 520:
            player.litCandle = False
            player.level += 1
            reset = True
            player.total_kills += player.kills
            player.kills = 0
        if player.lives == 0:
            return False
        elif reset is True:
            player.rect.x = 0
            player.rect.y = 500
            enemy_list, plat_list, rope_list, backdrop, candle = level.create(player)
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
    def __init__(self, gameDisplay):
        '''Initializes the level class'''
        self.gameDisplay = gameDisplay
    def create(self, player):
        '''Creates the level'''
        from models import platform
        enemy_list = pygame.sprite.Group()
        plat_list = pygame.sprite.Group()
        rope_list = pygame.sprite.Group()
        if player.level == 0:  # tutorial
            player.rect.x = 0
            player.rect.y = 500  # User spawns falling
            plt = [[115, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [0, 630, 960, 25, 'basicLongPlatformSprite(1).png'],
                   [640, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [540, 310, 50, 25, 'basicBlockPlatformSprite (1).png'],
                   [375, 460, 50, 25, 'basicBlockPlatformSprite (1).png'], [840, 340, 50, 25, 'basicBlockPlatformSprite (1).png']]
            loc =  [[250, 576], [600, 576], [120, 300]]
            rop = [[470, 25, 21, 500, 'basicRopeSprite.png']]
            for location in loc:
                e = enemy.Rat(location[0], location[1])
                enemy_list.add(e)
            for plat in plt:
                p = platform.Platform(plat[0], plat[1], plat[2], plat[3], plat[4])
                plat_list.add(p)
            for rope in rop:
                r = platform.Rope(rope[0], rope[1], rope[2], rope[3], rope[4])
                rope_list.add(r)
            candle = pygame.Rect(773, 280, 50, 50)
        elif player.level == 1:
            player.rect.x = 0
            player.rect.y = 500  # User spawns falling
            plt = [[115, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [0, 620, 960, 25, 'basicLongPlatformSprite(1).png'],
                   [640, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [840, 320, 25, 40, 'basicBlockPlatformSprite (1).png'],
                   [205, 555, 40, 20, 'basicBlockPlatformSprite (1).png'], [290, 500, 50, 25, 'basicBlockPlatformSprite (1).png'],
                   [240, 450, 20, 10, 'basicBlockPlatformSprite (1).png'], [90, 350, 25, 25, 'basicBlockPlatformSprite (1).png'],
                   [25, 280, 40, 25, 'basicBlockPlatformSprite (1).png'], [90, 225, 25, 35, 'basicBlockPlatformSprite (1).png'],
                   [320, 305, 25, 45, 'basicBlockPlatformSprite (1).png'], [430, 320, 105, 30, 'basicLongPlatformSprite(1).png']]
            for plat in plt:
                p = platform.Platform(plat[0], plat[1], plat[2], plat[3], plat[4])
                plat_list.add(p)
            rop = [[200, 0, 25, 250, 'basicRopeSprite.png'], [730, 0, 25, 350, 'basicRopeSprite.png']]
            for rope in rop:
                r = platform.Rope(rope[0], rope[1], rope[2], rope[3], rope[4])
                rope_list.add(r)
            loc =  [[250, 576], [630, 350]]
            for location in loc:
                e = enemy.Rat(location[0], location[1])
                enemy_list.add(e)
        if player.level <= 5:
            backdrop = pygame.image.load('images/maps/Guardtower.png')
            candle = pygame.Rect(773, 280, 50, 50)
        return enemy_list, plat_list, rope_list, backdrop, candle
