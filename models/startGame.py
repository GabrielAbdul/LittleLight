import pygame


def startGame(gameDisplay, save, player, clock):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 576
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10 # pixels to move per step
    while not done:
        gameDisplay.fill((0, 0, 0))
        player_list.draw(gameDisplay)
        player.update()
        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pause_game = __import__('littlelight').pause_game
                    done = pause_game(gameDisplay)
                if keys[pygame.K_LEFT] or event.key == ord('a'):
                    player.control(-steps, 0)
                if keys[pygame.K_RIGHT] or event.key == ord('d'):
                    player.control(steps, 0)
                if keys[pygame.K_UP] or event.key == ord('w'):
                    print('jump')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0)
    return done