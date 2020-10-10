#!/usr/bin/env python3
'''module that defines base class'''


class Base():
    '''class Base that is inherited from all other classes'''

    __num = 0

    def __init__(self):
        '''method to be called upon object instantiation'''
        self.id = Base.__num + 1
        Base.__num = self.id
