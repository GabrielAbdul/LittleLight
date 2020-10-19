#!/usr/bin/env python3
'''module that defines save class'''
from models import storage


class Save():
    '''class to define a save'''

    objects = {
            'auto': {},
            'save_1': {},
            'save_2': {},
            'save_3': {},
            }

    def __init__(self):
        '''method to be called upon object instantiation'''
        self.__achievements = []

    def save(self, save_name):
        '''method that will save a game'''
        try:
            storage.save(self.objects, save_name)
        except Exception as e:
            print("Couldn't save:", e)

    def load(self):
        '''method that will load a game'''
        try:
            return storage.load_save()
        except Exception as e:
            print("Couldn't load save:", e)

    def delete(self):
        '''methoid that will delete a game'''
        storage.delete_save(save)
