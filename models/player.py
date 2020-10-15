#!/usr/bin/env python3
'''module that defines player class'''
from models.base_model import Base
import pygame
import os


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
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

    def getStats(self):
        '''returns a dictionary of player stats'''
        res = self.__dict__.copy()
        del res['images']
        del res['image']
        del res['rect']
        return res

    def control(self, x, y):
        '''Allows the player to control the character'''
        self.movex += x
        self.movey += y

    def update(self):
        '''Update sprite position'''
        self.rect.x += self.movex
        self.rect.y += self.movey