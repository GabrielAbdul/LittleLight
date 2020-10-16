#!/usr/bin/env python3
'''module that defines player class'''
from models.base_model import Base
import pygame
import os


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
    steps = 5 # Number of pixels per step. Repeated in startGame if needs changing

    def __init__(self):
        '''method to be called upon object instantiation'''
        super().__init__()
        img = pygame.image.load('images/sprites/Sprite1standright.png').convert()
        img1 = pygame.image.load('images/sprites/Sprite1stepright.png').convert()
        self.images = []
        self.images.append(img)
        self.images.append(img1)
        for i in range(2, 9):
            img = pygame.image.load('images/sprites/Sprite1stepright' + str(i) + '.png').convert()
            self.images.append(img)
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

    def getStats(self):
        '''returns a dictionary of player stats'''
        tmp = self.__dict__.copy()
        res = {'health': tmp.get('health'), 'strength': tmp.get('strength'), 'agility': tmp.get('agility'), 'glow': tmp.get('glow')}
        return res

    def updateStats(self, **dictionary):
        '''updates players stats'''
        for key, val in dictionary:
            setattr(self, key, val)

    def control(self, x, y):
        '''Allows the player to control the character'''
        if (self.prevx < 0 and self.movex > 0 and x == 0) or (self.prevx > 0 and self.movex < 0 and x == 0):
            self.movex = self.prevx
            return
        self.prevx = self.movex
        self.movex = x
        self.movey = y

    def update(self):
        '''Update sprite position'''
        self.rect.x += self.movex
        self.rect.y += self.movey
