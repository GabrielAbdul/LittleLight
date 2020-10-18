#!/usr/bin/env python3
'''Module that is used for file storage'''
import os
import json


class FileStorage():
    '''class FileStorage'''

    # path to save game file
    __file_path = 'save_game.json'

    @staticmethod
    def save(save_game):
        '''FileStorage module to create a saved game'''
#        save_game.__achievements.append(achievement.check_achievements())
        with open('save_game.json', 'a+') as file:
            json.dump(save_game, file)

    @staticmethod
    def load_save():
        '''FileStorage method to load a saved game'''
        with open('save_game.json', 'rb') as file:
            return json.load(file)

    @staticmethod
    def delete_save(save_game):
        '''FileStorage method to delete previous saved game'''
        if os.path.exists('save_game.json'):
            os.remove('save_game.json')
        else:
            print('No save data found')
