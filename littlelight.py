import pygame
import json
from models.button import button
'''Starts the game Little Light'''


def main():
    '''Basic game loop'''
    global toolsCanvas, gameDisplay, player, save
    toolsCanvas = pygame.Surface((700, 120))
    pygame.init()

    done = False
    pygame.display.set_caption('Little Light')

    '''Menus'''

    mainMenu = pygame.image.load('images/menu1.png')
    contMenu = pygame.image.load('images/menu2.jpg')
    # controls = pygame.image.load('images/menu3.jpg')
    mainMenu = pygame.transform.scale(mainMenu, (960, 640))
    size = (width, height) = mainMenu.get_size()
    contMenu = pygame.transform.scale(contMenu, (width, height))
    # controls = pygame.transform.scale(controls, (width, height))

    gameDisplay = pygame.display.set_mode(size)
    gameDisplay.fill((0, 0, 0))
    clock = pygame.time.Clock()
    menu = 'main'

    '''buttons'''

    auto_s = button([width / 3, height / 2 - 160, width / 3, 40], gameDisplay)
    save_01 = button([width / 3, height / 2 - 100, width / 3, 40], gameDisplay)
    save_02 = button([width / 3, height / 2 - 40, width / 3, 40], gameDisplay)
    save_03 = button([width / 3, height / 1 - 300, width / 3, 40], gameDisplay)
    newGame = button([width / 3, height / 2 + 50, width / 3, 40], gameDisplay,
                    (0, 0, 0))
    cont = button([width / 3, height / 2 + 100, width / 3, 40], gameDisplay,
                    (0, 0, 0))
    ext = button([width / 3, (height / 2) + 150, width / 3, 40], gameDisplay,
                    (0, 0, 0))
    c = button([320, 320, 100, 50])


    print("w/h: {}/{}".format(width, height))

    def displayMenu(name):
        '''Displays a menu'''
        menus = {
            'main': mainMenu, 'continue': contMenu
        }
        gameDisplay.fill((0, 0, 0))
        try:
            gameDisplay.blit(menus.get(name), (0, 0))
        except Exception:
            print('ex')
            return 1
        if name == 'main':
            newGame.draw()
            newGame.addText('New Game')
            cont.draw()
            cont.addText('Continue')
            ext.draw()
            ext.addText('Exit')
        elif name == 'continue':
            auto_s.draw()
            auto_s.addText('Autosave', -10)
            save_01.draw()
            save_01.addText('Save 1', -20)
            save_02.draw()
            save_02.addText('Save 2', -20)
            save_03.draw()
            save_03.addText('Save 3', -20)
        elif name == 'controls':
            c.draw()
            c.addText('continue')
            pass
        return 0

    def charCreate(save, player):
        '''Allows the user to create a character'''
        done = False
        sprite = pygame.image.load('images/sprites/Sprite1standright.png').\
        convert_alpha()
        print(sprite.get_size())
        sprite = pygame.transform.scale(sprite, (200, 400))
        print(sprite.get_size())
        s_points = 6
        s_points_button = button([width - 250, 10, 200, 30])
        str_d = button([width - 300, 50, 25, 25])
        strn = button([width - 250, 50, 150, 25])
        str_u = button([width - 75, 50, 25, 25])
        agi_d = button([width - 300, 85, 25, 25])
        agi = button([width - 250, 85, 150, 25])
        agi_u = button([width - 75, 85, 25, 25])
        glo_d = button([width - 300, 120, 25, 25])
        glo = button([width - 250, 120, 150, 25])
        glo_u = button([width - 75, 120, 25, 25])
        d = button([width - 200, height - 30, 175, 25])
        while not done:
            gameDisplay.fill((14, 20, 22))
            gameDisplay.blit(sprite, (50, 100))
            s_points_button.draw()
            s_points_button.addText('Skill Points: ' + str(s_points), 25)
            str_d.draw()
            str_d.addText('-')
            strn.draw()
            strn.addText('STR: ' + str(player.strength) + '/5', 20)
            str_u.draw()
            str_u.addText('+')
            agi_d.draw()
            agi_d.addText('-')
            agi.draw()
            agi.addText('AGI: ' + str(player.agility) + '/5', 20)
            agi_u.draw()
            agi_u.addText('+')
            glo_d.draw()
            glo_d.addText('-')
            glo.draw()
            glo.addText('GLOW: ' + str(player.glow) + '/5', 20)
            glo_u.draw()
            glo_u.addText('+')
            d.draw()
            d.addText('Finished', 15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and\
                event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if d.rect.collidepoint(pos):
                        if s_points == 0:
                            done = True
                        else:
                            print('Use all skill points to proceed')
                    if str_d.rect.collidepoint(pos):
                        if player.strength > 1:
                            s_points += 1
                            player.strength -= 1
                    elif str_u.rect.collidepoint(pos):
                        if s_points > 0 and player.strength < 5:
                            s_points -= 1
                            player.strength += 1
                    elif agi_d.rect.collidepoint(pos):
                        if player.agility > 0:
                            s_points += 1
                            player.agility -= 1
                    elif agi_u.rect.collidepoint(pos):
                        if s_points > 0 and player.agility < 5:
                            s_points -= 1
                            player.agility += 1
                    elif glo_d.rect.collidepoint(pos):
                        if player.glow > 1:
                            s_points += 1
                            player.glow -= 1
                    elif glo_u.rect.collidepoint(pos):
                        if s_points > 0 and player.glow < 5:
                            s_points -= 1
                            player.glow += 1
            pygame.display.flip()
        save.player = player

    while not done:  # Starting gameloop for main menu
        ch = displayMenu(menu)
        if ch == 1:  # Exit if an error is encountered while displaying menu
            break
        for event in pygame.event.get():  # Loop through event queue
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    if menu == 'main':
                        done = pause_game(gameDisplay)
                    elif menu == 'continue' or menu == 'newgame':
                        menu = 'main'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # On click
                pos = pygame.mouse.get_pos()
                if menu == 'main':
                    if ext.rect.collidepoint(pos):
                        done = True
                    elif cont.rect.collidepoint(pos):
                        menu = 'continue'

                    elif newGame.rect.collidepoint(pos):
                        from models.startGame import startGame
                        from models.save import Save
                        from models.player import Player
                        player = Player()
                        save = Save()
                        charCreate(save, player)
                        player.health = player.strength * 2 + player.glow
                        player.curr_health = player.health
                        save.objects.get('auto').update(player.getStats())
                        save.save('auto')
                        done = startGame(gameDisplay, player, clock, save)
                        print(player.getStats())
                        if done:
                            pygame.quit()
                            quit()
                if menu == 'continue':
                    from models.player import Player
                    from models.startGame import startGame
                    from models import storage
                    from models.save import Save
                    player = Player()
                    saves = storage.load_save()
                    save = Save()
                    save.objects = saves
                    # detect which save user clicks on
                    if auto_s.rect.collidepoint(pos):
                        player.updateStats(json.dumps(saves.get('auto')))
                        print(player.getStats())
                        done = startGame(gameDisplay, player, clock, save)
                    elif save_01.rect.collidepoint(pos):
                        saveName = 'save_1'
                        player.updateStats(json.dumps(saves.get(saveName)))
                        print(player.getStats())
                        done = startGame(gameDisplay, player, clock, save)
                    elif save_02.rect.collidepoint(pos):
                        saveName = 'save_2'
                        player.updateStats(json.dumps(saves.get(saveName)))
                        print(player.getStats())
                        done = startGame(gameDisplay, player, clock, save)
                    elif save_03.rect.collidepoint(pos):
                        saveName = 'save_3'
                        player.updateStats(json.dumps(saves.get(saveName)))
                        print(player.getStats())
                        done = startGame(gameDisplay, player, clock, save)
                    if done:
                        pygame.quit()
                        quit()
                        save = 'save_3'

        pygame.display.flip()
        clock.tick(20)


def pause_game(gameDisplay):
    '''function to pause the game, should be within main game loop'''
    paused = True
    width, height = 960, 640
    ps = pygame.image.load('images/pausemenu.png').convert_alpha()
    ps = pygame.transform.scale(ps, (960, 640))
    while paused:
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(ps, (0, 0))
        resume = button([width / 3 + 50, (height // 3), (width / 3) - 100, 40],
                        None, (255, 255, 255))
        quit = button([width / 3 + 50, (height // 3) + 50, (width / 3) - 100,
                       40], None, (255, 255, 255))
        quit.addText('Quit', -15)
        resume.addText('Resume')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if quit.rect.collidepoint(pos):
                    return True
                elif resume.rect.collidepoint(pos):
                    paused = False
        pygame.display.update()
    return False

if __name__ == '__main__':
    main()
