import pygame
'''Defines the button class for use primarily in menus'''


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


# buttons
newGame = button([width / 3, height / 2 + 50, width / 3, 40])
ext = button([width / 3, (height / 2) + 100, width / 3, 40])