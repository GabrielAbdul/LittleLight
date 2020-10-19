import pygame
'''Defines the button class for use primarily in menus'''


class button(pygame.Rect):
    '''Creates a rectangular button'''
    __gameDisplay = None

    def __init__(self, args, gameDisplay=None, color=(255, 0, 0),
                 rectColor=(255, 150, 0)):
        '''initializes a rectangle with values'''
        if self.__gameDisplay is None and gameDisplay is None:
            exit(2)
        self.left, self.top, self.width, self.height = args[0], args[1],\
        args[2], args[3]
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        if gameDisplay is not None:
            button.__gameDisplay = self.gameDisplay = gameDisplay
        else:
            self.gameDisplay = button.__gameDisplay
        self.color = color
        self.rectColor = rectColor

    def draw(self, color=None):
        '''draws the rectangle'''
        if color is None:
            tmp = self.rectColor
        else:
            tmp = color
        pygame.draw.rect(self.gameDisplay, tmp, self.rect, 0)

    def addText(self, text, offset=0):
        '''adds text to the button'''
        self.font = pygame.font.SysFont('Arial', 25)
        self.gameDisplay.blit(self.font.render(text, True, self.color),
                              ((self.left + self.width / 3) - offset,
                               self.top))
