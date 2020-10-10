#!/usr/bin/env python3
'''module that defines base class'''


class Base(id=None):
    '''class Base that is inherited from all other classes'''

    if id is not None:
        self.id = id
    self.id = self.id + 1
