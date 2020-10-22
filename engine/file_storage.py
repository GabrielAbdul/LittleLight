#!/usr/bin/env python3
'''Module that is used for file storage'''
import os
import json


class FileStorage():
    '''class FileStorage'''

    # path to save game file
    __file_path = 'save_game.json'

    @staticmethod
    def save(save_game, save_name):
        '''FileStorage module to create a saved game'''
#        save_game.__achievements.append(achievement.check_achievements())
        js = object
        with open('save_game.json', 'r') as file:
            js = json.load(file)
        print(js)
        js.pop(save_name)
        js.update({save_name: save_game.get(save_name)})
        print(js)
        with open('save_game.json', 'w') as file:
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
