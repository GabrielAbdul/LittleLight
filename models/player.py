#!/usr/bin/env python3
'''module that defines player class'''
from base_model import Base


class Player(Base):
    '''class to define a player'''
    __init__(self):
        '''method to be called upon object instantiation'''
        self.health = 100
        self.strength = 0
        self.agility = 0
        self.glow = 0
