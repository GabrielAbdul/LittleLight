#!/usr/bin/env python3
'''Module that is used for file storage'''
import os
import pickle
from models.save import Save


class FileStorage():
    '''class FileStorage'''

    # path to save game file
    __file_path = 'save_game.py'

    def save(save_game):
        '''FileStorage module to create a saved game'''
        with open('save_game.py', 'w') as file:
            pickle.dump(save_game, file)
        return

    def load_save():
        '''FileStorage method to load a saved game'''
        with open('save_game.py', 'rb') as file:
            return pickle.load(file)

    def delete_save():
        '''FileStorage method to delete previous saved game'''
        if os.path.exists('save_game.py'):
            os.remove('save_game.py')
        else:
            print('No save data found')
