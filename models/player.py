#!/usr/bin/env python3
'''module that defines player class'''
from models.base_model import Base
import pygame
import os


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
    steps = 2 # Number of pixels per step. Repeated in startGame if needs changing
    jump_count = 0
    hang_count = 0

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
        self.falling = True
        self.jumping = False
        self.hang = False

    def getStats(self):
        '''returns a dictionary of player stats'''
        tmp = self.__dict__.copy()
        res = {'health': tmp.get('health'),
                'agility': tmp.get('agility'),
                'strength': tmp.get('strength'),
                'glow': tmp.get('glow')}
        return res

    def updateStats(self, dict):
        '''method that updates stats'''
        for key, val in eval(dict).items():
            setattr(self, key, val)

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
        if self.jumping and self.falling is False:
            self.jump_count += 1
            if self.jump_count >= 15:
                self.jumping = False
                self.jump_count = 0
                self.hang = True
                self.hang_count = 1
        elif self.hang is True and self.hang_count <= 6:
            self.hang_count += 1
        else:
            self.falling = True
            self.hang = False
            self.hang_count = 0
        if self.rect.bottom >= 640:
            self.rect.bottom = 640
            self.movey = 0
            self.jumping = False
            self.falling = False
        self.rect.x += self.movex
        self.rect.y += self.movey

    def gravity(self):
        if self.falling:
            self.movey += 5
        if self.jumping:
            self.movey -= 4

    def jump(self):
        if self.falling is False and self.jumping is False and self.hang is False:
            self.jumping = True
            self.falling = False
            self.rect.y -= 10
