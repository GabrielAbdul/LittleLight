#!/usr/bin/env python3
'''module that defines player class'''
from models.base_model import Base


class Player(Base):
    '''class to define a player'''
    def __init__(self):
        '''method to be called upon object instantiation'''
        self.health = 0
        self.strength = 1
        self.agility = 1
        self.glow = 1

    def getStats(self):
        '''returns a dictionary of player stats'''
        return self.__dict__.copy()