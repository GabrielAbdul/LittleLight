import pygame
import random
from models import enemy


def startGame(gameDisplay, player, clock, save):
    '''runs the main game'''
    from models.button import button
    done = False
    player_list = pygame.sprite.Group()
    player_list.add(player)
    baseSteps = 2
    steps = 2  # pixels to move per step
    level = Level(gameDisplay)
    enemy_list, plat_list, rope_list, backdrop, candle = level.create(player)
    jmp = button([890, 600, 60, 25], gameDisplay, (0, 0, 0), (100, 200, 50))
    while not done:
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
            save.objects.get('auto').update(player.getStats())
            save.save('auto')
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
        levels = {
            '0': {
                'plt': [[115, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [0, 630, 960, 25, 'basicLongPlatformSprite(1).png'],
                   [640, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [540, 310, 50, 25, 'basicBlockPlatformSprite (1).png'],
                   [375, 460, 50, 25, 'basicBlockPlatformSprite (1).png'], [840, 340, 50, 25, 'basicBlockPlatformSprite (1).png']],
                'rat':  [[250, 576], [600, 576], [120, 300]],
                'rop': [[470, 25, 21, 500, 'basicRopeSprite.png']],
                'candle': pygame.Rect(773, 280, 50, 50)
            },
            '1': {
                'plt': [[115, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [0, 620, 960, 25, 'basicLongPlatformSprite(1).png'],
                   [640, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [840, 320, 25, 40, 'basicBlockPlatformSprite (1).png'],
                   [205, 555, 40, 20, 'basicBlockPlatformSprite (1).png'], [290, 500, 50, 25, 'basicBlockPlatformSprite (1).png'],
                   [240, 450, 20, 10, 'basicBlockPlatformSprite (1).png'], [90, 350, 25, 25, 'basicBlockPlatformSprite (1).png'],
                   [25, 280, 40, 25, 'basicBlockPlatformSprite (1).png'], [90, 225, 25, 35, 'basicBlockPlatformSprite (1).png'],
                   [320, 305, 25, 45, 'basicBlockPlatformSprite (1).png'], [430, 320, 105, 30, 'basicLongPlatformSprite(1).png']],
                'rop': [[200, 0, 25, 250, 'basicRopeSprite.png'], [730, 0, 25, 350, 'basicRopeSprite.png']],
                'rat': [[250, 576], [630, 350]],
                'candle': pygame.Rect(773, 280, 50, 50)
            },
            '2': {
                'plt': [
                    [115, 410, 205, 25, 'basicLongPlatformSprite(1).png'], [0, 625, 960, 35, 'basicLongPlatformSprite(1).png'],
                    [640, 410, 205, 25, 'basicLongPlatformSprite(1).png'],
                    [290, 500, 55, 25, 'basicBlockPlatformSprite (1).png'], [415, 555, 120, 20, 'basicLongPlatformSprite(1).png'],
                    [375, 455, 50, 25, 'basicBlockPlatformSprite (1).png'], [375, 345, 50, 25, 'basicBlockPlatformSprite (1).png'],
                    [280, 375, 50, 25, 'basicBlockPlatformSprite (1).png'], [730, 340, 50, 25, 'basicBlockPlatformSprite (1).png'], # Remove this line once crates ready
                    [430, 100, 100, 25, 'basicLongPlatformSprite(1).png'], [475, 200, 160, 25, 'basicLongPlatformSprite(1).png'],
                    [35, 340, 60, 25, 'basicBlockPlatformSprite (1).png'], [52, 130, 65, 25, 'basicBlockPlatformSprite (1).png']
                        ],
                'rop': [[390, 0, 21, 280, 'basicRopeSprite.png'], [40, 0, 21, 280, 'basicRopeSprite.png']],
            }
        }
        level = {'rat': [], 'rop': [], 'plt': []}
        tmp = levels.get(str(player.level))
        if tmp is not None:
            level.update(tmp)
        for rat in level.get('rat'):
            e = enemy.Rat(rat[0], rat[1])
            enemy_list.add(e)
        for rope in level.get('rop'):
            r = platform.Rope(rope[0], rope[1], rope[2], rope[3], rope[4])
            rope_list.add(r)
        for plat in level.get('plt'):
                p = platform.Platform(plat[0], plat[1], plat[2], plat[3], plat[4])
                plat_list.add(p)
        if player.level <= 5:
            backdrop = pygame.image.load('images/maps/Guardtower.png')
            candle = pygame.Rect(773, 280, 50, 50)
            player.rect.x = 0
            player.rect.y = 500
        return enemy_list, plat_list, rope_list, backdrop, candle
