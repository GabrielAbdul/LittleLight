import random, pygame, sys, time
from models.button import newGame, ext
'''Starts the game Little Light'''


def main():
    '''Basic game loop'''
    global toolsCanvas
    global gameDisplay
    toolsCanvas = pygame.Surface((700, 120))
    pygame.init()

    done = False
    pygame.display.set_caption('Little Light')

    mainMenu = pygame.image.load('images/menu1.jpg')
    size = (width, height) = mainMenu.get_size()
    gameDisplay = pygame.display.set_mode(size)
    gameDisplay.fill((0, 0, 0))
    clock = pygame.time.Clock()
    menu = 'main'

    print("w/h: {}/{}".format(width, height))

    def displayMenu(name):
        menus = {'main': mainMenu, 'continue': 'placeholder', 'newgame': 'placeholder', 'pause': 'placeholder'}
        try:
            gameDisplay.blit(menus.get(name), [0, 0])
        except Exception:
            return 1
        if name == 'main':
            newGame.draw()
            newGame.addText('New Game')
            ext.draw()
            ext.addText('Exit')
        return 0

    while not done:
        ch = displayMenu(menu)
        if ch == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    if menu == 'main':
                        done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if ext.collidepoint(pos):
                    done = True
        pygame.display.update()
        clock.tick(20)


if __name__ == '__main__':
    main()
