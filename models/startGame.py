import pygame


def startGame(gameDisplay, player, clock, save=None):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 500 # User falls to floor. Not necessary, just to demonstrate gravity and ensure they don't start in floor
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
            continue
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.control(-steps, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.control(steps, 0)
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            player.control(0, 0) # Wipe movement if no keys are held down
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.jump()
        player.gravity() # Make sure gravity affects the player
        player.update() # Update player position
        player_list.draw(gameDisplay) # Redraw player
        pygame.display.flip() # Redraw screen with all objects in new position
        clock.tick(60) # 60 fps speed
    return done
