#!/usr/bin/env python3
'''module that defines save class'''
from base_model import Base



class Map(Base):
    '''class to define a map'''

    def __init__(self):
        '''method to be called upon object instantiation'''
        self.save_point = 0
        self.flags_tripped = 0
