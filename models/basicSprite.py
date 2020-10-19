#!/usr/bin/python3
'''Defines the base enemy class'''
import pygame
import random


class basicSprite(pygame.sprite.Sprite):
    '''Base sprite class to be inherited from for various sprites'''
    def __init__(self, x, y, img):
        '''Instantiates base instance variables'''
        #x and y are starting pos, img is default image. Extra images should be loaded in inherited class
        super().__init__()
        self.images = []
        self.image = pygame.image.load('images/sprites/' + img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
