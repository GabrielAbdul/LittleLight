import random, pygame, sys, time
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

    # buttons
    newGame = button([width / 3, height / 2 + 50, width / 3, 40])
    ext = button([width / 3, (height / 2) + 100, width / 3, 40])

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


class button(pygame.Rect):
    '''Creates a rectangular button'''
    def __init__(self, args):
        '''initializes a rectangle with values'''
        self.left, self.top, self.width, self.height = args[0], args[1], args[2], args[3]
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        '''draws the rectangle'''
        pygame.draw.rect(gameDisplay, (255, 150, 0), self.rect, 0)

    def addText(self, text):
        '''adds text to the button'''
        self.font = pygame.font.SysFont('Arial', 25)
        gameDisplay.blit(self.font.render(text, True, (255, 0, 0)), (self.left + self.width / 3, self.top))


if __name__ == '__main__':
    main()
