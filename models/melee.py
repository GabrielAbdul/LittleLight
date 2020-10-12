#!/usr/bin/env python3
'''module that defines save class'''
from attack import Attack


class Melee(Attack):
    '''class to define a save'''
    def __init__(self, damage, range=None, requirements={}, animation=''):
        '''method to be called upon object instantiation'''
        super().__init__(damage, range, requirements, animation)
