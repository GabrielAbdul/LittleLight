#!/usr/bin/python3
'''Defines the base enemy class'''
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    '''Base enemy class to be inherited from for various enemies'''
    def __init__(self, x, y, img):
        '''Instantiates base instance variables'''
        # x and y are starting pos, img is default image. Extra images should
        # be loaded in inherited class
        super().__init__()
        self.images = []
        self.image = pygame.image.load('images/sprites/' + img).convert_alpha()
        self.images.append(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.spd = 1
        self.dist = random.randint(60, 80)
        self.walk = True
        self.health = 3
        self.damage = 2

    def move(self):
        '''auto-moves the enemy'''
        if self.walk:
            if self.counter >= 0 and self.counter <= self.dist:
                self.rect.x += self.spd
                self.image = pygame.transform.flip(self.images[0], True, False)
            elif self.counter >= self.dist and self.counter <= self.dist * 2:
                self.rect.x -= self.spd
                self.image = self.images[0]
            else:
                self.counter = 0
            self.counter += 1
            if self.rect.bottom < 640:
                self.rect.y += 2
            elif self.rect.bottom < 640:
                self.rect.bottom = 640

    def die(self, enemy_list):
        '''
        determines whether enemy dies, and removes them from the screen if
        they do
        '''
        self.health -= 1
        if self.health <= 0:
            enemy_list.remove(self)

class Rat(Enemy):
    '''defines a grunt enemy'''
    def __init__(self, x, y):
        '''Initializes a rat'''
        super().__init__(x, y, 'enemies/rat1.png')
        self.health = 2
        l, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(l * 2), int(h * 2)))
        self.images[0] = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y