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
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.type = 'rope'


class Box(pygame.sprite.Sprite):
    '''Adds a class that acts as a platform that can be moved by the user'''
    def __init__(self, x, y, width, height, img):
        '''Initializes a Box'''
        super().__init__()
        self.image = pygame.image.load('images/sprites/' + img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = 'box'
        self.movex = 0
        self.prev_movex = 0

    def move(self, plat_list):
        '''Moves the box'''
        p_list = pygame.sprite.spritecollide(self, plat_list, False)
        self.rect.x += self.movex
        self.movex = 0
        for p in p_list:
            if p is not self:
                if p.rect.left - 5 <= self.rect.right and p.rect.right + 5 >= self.rect.left:
                    if self.rect.top + 50 <= p.rect.top:
                        self.rect.y -= 2
                    if self.rect.bottom <= p.rect.top:
                        self.rect.bottom = p.rect.top
        if p_list == [] or p_list == [self]:
            self.rect.bottom += 6
            self.movex = 1 if self.prev_movex > 0 else -1

