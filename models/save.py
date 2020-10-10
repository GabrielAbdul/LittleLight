#!/usr/bin/env python3
'''module that defines save class'''
from base_model import Base



class Save(Base):
    '''class to define a save'''

    __saves = 1
    __objects = []

    def __init__(self):
        '''method to be called upon object instantiation'''
        self.save_id = self.__saves
        self.__saves = save.id
