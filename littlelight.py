import random, pygame, sys, time
from models.button import button
'''Starts the game Little Light'''


def main():
    '''Basic game loop'''
    global toolsCanvas, gameDisplay, paused = True
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

    # buttons
    newGame = button([width / 3, height / 2 + 50, width / 3, 40], gameDisplay)
    ext = button([width / 3, (height / 2) + 100, width / 3, 40], gameDisplay)

    print("w/h: {}/{}".format(width, height))

    def displayMenu(name):
        '''Displays a menu'''
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

    def pause_game():
        '''function to pause the game, should be within main game loop'''
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            resume = button([width / 3, (height / 2) + 100, width / 3, 40])
            quit = button([width / 3, (height / 2) + 100, width / 3, 40])
            quit.addText('Quit')
            resume.addText('Resume')

            pygame.display.update()

    def unpause_game():
        '''function to unpause the game'''
        pause = False


if __name__ == '__main__':
    main()
