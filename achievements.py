import pygame, random, time
'''Defines an achievement class, and several achievements'''


class achievement():
    '''Basic info for all achievements'''
    id = 0
    complete = False
    hint = ""
    __all_achievements = []
    name = ""

    def __init__(self, **kwargs):
        '''Initializes class vars'''
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.__all_achievements.append(self)

    @classmethod
    def check_achievements(cls):
        '''Returns a list of completed achievements'''
        res = []
        for a in cls.__all_achievements:
            if a.complete:
                res.append(a)
        return res

    def __str__(self):
        '''Defines string representation of object'''
        return '{' + "{}.{}: {}".format(self.__class__.__name__, self.id, self.__dict__) + '}'

    @classmethod
    def grant_achievement(cls, id):
        '''grants achievements to user'''
        if id != 0:
            for a in cls.__all_achievements:
                if a.id == id:
                    a.complete = True
                    #display_achievement
                    return 1
        return 0

    @classmethod
    def lucky(cls):
        '''Might grant the lucky achievement'''
        random.seed(time.time())
        if random.randint(0, 1000000) == 0:
            for a in cls.__all_achievements:
                if a.id == 0:
                    a.complete = True
                    #display_achievement
                    return 1
        return 0


def create_achievements():
    '''Creates all achievements with static IDs'''
    rdm = achievement(name="lucky", id=0, hint="You've gotta be pretty lucky to get this")
    stonks = achievement(name="stonks", id=1, hint="Have an absurd amount of strength")
    ll = achievement(name="Little Light", id=0, hint="Increase your glow")
    shine = achievement(name="Shine Bright", id=0, hint="Have a lot of glow")