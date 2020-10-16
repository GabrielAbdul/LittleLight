#!/usr/bin/env python3
'''module that defines player class'''
from models.base_model import Base
import pygame
import os


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
    steps = 2 # Number of pixels per step. Repeated in startGame if needs changing

    def __init__(self):
        '''method to be called upon object instantiation'''
        super().__init__()
        img = pygame.image.load('images/sprites/Sprite1standright.png').convert_alpha()
        img1 = pygame.image.load('images/sprites/Sprite1stepright.png').convert_alpha()
        img1.convert_alpha()
        self.images = []
        self.images.append(img)
        self.images.append(img1)
        for i in range(2, 9):
            img = pygame.image.load('images/sprites/Sprite1stepright' + str(i) + '.png').convert_alpha()
            self.images.append(img)
        self.__ani = 8
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 0
        self.strength = 1
        self.agility = 1
        self.glow = 1
        self.prevx = self.movex
        self.prevx2 = 0

    def getStats(self):
        '''returns a dictionary of player stats'''
        res = self.__dict__.copy()
        del res['images']
        del res['image']
        del res['rect']
        return res

    def control(self, x, y):
        '''Allows the player to control the character'''
        if (self.prevx < 0 and self.movex > 0 and x == 0) or (self.prevx > 0 and self.movex < 0 and x == 0):
            self.movex = self.prevx
            return
        if self.prevx != 0:
            self.prevx2 = self.prevx
        self.prevx = self.movex
        self.movex = x
        self.movey = y

    def update(self):
        '''Update sprite position'''
        self.rect.x += self.movex
        self.rect.y += self.movey
        if self.movex > 0: # moving right
            self.frame += 1
            if self.frame > 3 * self.__ani:
                self.frame = 1
            self.image = self.images[self.frame // 3]
        if self.movex == 0:
            self.frame = 0
            if self.prevx2 >= 0:
                self.image = self.images[0]
            else:
                self.image = pygame.transform.flip(self.images[0], True, False)
        if self.movex < 0: # moving left
            self.frame += 1
            if self.frame > 3 * self.__ani:
                self.frame = 1
            self.image = pygame.transform.flip(self.images[self.frame // 3], True, False)
