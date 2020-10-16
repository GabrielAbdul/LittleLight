#!/usr/bin/env python3
'''Module that is used for file storage'''
import os
import json


class FileStorage():
    '''class FileStorage'''

    # path to save game file
    __file_path = 'save_game.py'

    @staticmethod
    def save(save_game):
        '''FileStorage module to create a saved game'''
#        save_game.__achievements.append(achievement.check_achievements())
        with open('save_game.py', 'w') as file:
            json.dump(save_game, file)

    @staticmethod
    def load_save():
        '''FileStorage method to load a saved game'''
        with open('save_game.py', 'rb') as file:
            return json.load(file)

    @staticmethod
    def delete_save(save_game):
        '''FileStorage method to delete previous saved game'''
        if os.path.exists('save_game.py'):
            os.remove('save_game.py')
        else:
            print('No save data found')
