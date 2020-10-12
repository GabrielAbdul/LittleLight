#!/usr/bin/env python3
'''module that defines save class'''


class Attack():
    '''class to define a save'''
    def __init__(self, damage, range=None, requirements={}, animation=''):
        '''method to be called upon object instantiation'''
        if range is not None:
            self.range = range
        self.requirements = requirements
        self.damage = damage
        self.animation = animation
