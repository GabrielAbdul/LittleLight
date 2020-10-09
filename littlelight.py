import random, pygame, sys, time


def main():
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

    while not done:
        gameDisplay.blit(mainMenu, [0, 0])
        newGame = button([width / 3, height / 2 + 50, width / 3, 40])
        newGame.addText('New Game')
        ext = button([width / 3, (height / 2) + 100, width / 3, 40])
        ext.addText('Exit')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos= pygame.mouse.get_pos()
                if ext.collidepoint(pos):
                    done = True
        pygame.display.update()
        clock.tick(120)


class button(pygame.Rect):
    def __init__(self, args):
        self.left, self.top, self.width, self.height = args[0], args[1], args[2], args[3]
        self.rect = pygame.draw.rect(gameDisplay, (255, 150, 0), pygame.Rect(self.left, self.top, self.width, self.height), 0)

    def addText(self, text):
        self.font = pygame.font.SysFont('Arial', 25)
        gameDisplay.blit(self.font.render(text, True, (255, 0, 0)), (self.left + self.width / 3, self.top))


if __name__ == '__main__':
    main()