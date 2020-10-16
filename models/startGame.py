import pygame


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 500
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 2 # pixels to move per step
    while not done:
        gameDisplay.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_game = __import__('littlelight').pause_game
            done = pause_game(gameDisplay)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.control(-steps, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.control(steps, 0)
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            player.control(0, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
                    print('jump')
        player.gravity()
        player.update()
        player_list.draw(gameDisplay)
        pygame.display.flip()
        clock.tick(60)
    return done
