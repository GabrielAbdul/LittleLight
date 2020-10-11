import random, pygame, sys, time
from models.button import button
'''Starts the game Little Light'''


def main():
    '''Basic game loop'''
    global toolsCanvas, gameDisplay
    toolsCanvas = pygame.Surface((700, 120))
    pygame.init()

    done = False
    pygame.display.set_caption('Little Light')

    mainMenu = pygame.image.load('images/menu1.jpg')
    contMenu = pygame.image.load('images/menu2.jpg')
    newMenu = pygame.image.load('images/menu3.jpg')
    size = (width, height) = mainMenu.get_size()
    pygame.transform.scale(contMenu, (width, height))
    pygame.transform.scale(newMenu, (width, height))

    gameDisplay = pygame.display.set_mode(size)
    gameDisplay.fill((0, 0, 0))
    clock = pygame.time.Clock()
    menu = 'main'

    # buttons
    newGame = button([width / 3, height / 2 + 50, width / 3, 40], gameDisplay)
    cont = button([width / 3, height / 2 + 100, width / 3, 40], gameDisplay)
    ext = button([width / 3, (height / 2) + 150, width / 3, 40], gameDisplay)

    print("w/h: {}/{}".format(width, height))

    def displayMenu(name):
        '''Displays a menu'''
        menus = {'main': mainMenu, 'continue': contMenu, 'newgame': newMenu, 'pause': 'placeholder'}
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
        return 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    if menu == 'main':
                        done = True
                    elif menu == 'continue' or menu == 'newgame':
                        menu = 'main'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if menu == 'main':
                    if ext.rect.collidepoint(pos):
                        done = True
                    elif cont.rect.collidepoint(pos):
                        menu = 'continue'
                    elif newGame.rect.collidepoint(pos):
                        menu = 'newgame'
        ch = displayMenu(menu)
        if ch == 1:
            break
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    main()
