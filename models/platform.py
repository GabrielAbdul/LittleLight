import pygame
'''Defines all platforms'''


class Platform(pygame.sprite.Sprite):
    '''Simplifies gravity, makes gravity not apply to platforms'''
    def __init__(self, x, y, width, height, img):
        '''Initializes a platform'''
        super().__init__()
        self.image = pygame.image.load('images/sprites/platforms/' + img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.type = 'platform'


class Rope(pygame.sprite.Sprite):
    '''Adds a class that allows for climbing objects'''
    def __init__(self, x, y, width, height, img):
        '''Initializes a rope'''
        super().__init__()
        self.image = pygame.image.load('images/sprites/' + img).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.type = 'rope'