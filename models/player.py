#!/usr/bin/env python3
'''module that defines player class'''
import pygame


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
    steps = 2  # Number of pixels per step. Repeated in startGame
    jump_count = 0  # counter for jump time
    hang_count = 0  # counter for hang time after jumping

    def __init__(self):
        '''method to be called upon object instantiation'''
        super().__init__()
        img = pygame.image.load('images/sprites/Sprite1standright.png').\
        convert_alpha()
        img1 = pygame.image.load('images/sprites/Sprite1stepright.png').\
        convert_alpha()
        img1.convert_alpha()
        self.images = []
        self.images.append(img)
        self.images.append(img1)
        for i in range(2, 9):
            img = pygame.image.load('images/sprites/Sprite1stepright' +
                                    str(i) + '.png').convert_alpha()
            self.images.append(img)
        self.__ani = 8
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0  # x-axis movement: positive=right, negative=left
        self.movey = 0  # y-axis movement: positive=down, negative=up
        self.frame = 0  # sprite frame
        self.health = 0
        self.curr_health = 0
        self.strength = 1
        self.agility = 1
        self.glow = 1
        self.prevx = self.movex  # logging previous x
        self.prevx2 = 0  # logging idle direction
        self.falling = True  # Is the player falling
        self.jumping = False  # Is the player jumping
        self.jump_cd = 0
        self.hang = False  # Is the player hangin in the air
        self.i_frame = 0
        self.lives = 3
        self.total_kills = 0
        self.kills = 0
        self.level = 0
        self.climbing = False
        self.slowfall = False

    def getStats(self):
        '''returns a dictionary of player stats'''
        tmp = self.__dict__.copy()
        res = {'health': tmp.get('health'),
               'curr_health': tmp.get('curr_health'),
               'agility': tmp.get('agility'),
               'strength': tmp.get('strength'),
               'glow': tmp.get('glow'),
               'kills': tmp.get('kills'),
               'lives': tmp.get('lives'),
               'level': tmp.get('level')
               }
        return res

    def updateStats(self, dict):
        '''method that updates stats'''
        for key, val in eval(dict).items():
            setattr(self, key, val)

    def control(self, x, y):
        '''Allows the player to control the character'''
        if (self.prevx < 0 and self.movex > 0 and x == 0) or\
        (self.prevx > 0 and self.movex < 0 and x == 0):
            self.movex = self.prevx  # Smooth movement when multiple keys down
            return
        if self.prevx != 0:
            self.prevx2 = self.prevx  # Logging last direction faced
        self.prevx = self.movex
        self.movex = x
        self.movey = y

    def update(self, enemy_list, plat_list, rope_list):
        '''Update sprite position'''
        if self.climbing:
            self.jumping = False
        if self.movex > 0:  # moving right
            self.frame += 1
            if self.frame > 3 * self.__ani:  # pausing on each frame for 3 tick
                self.frame = 1
            self.image = self.images[self.frame // 3]  # '//' to ensure int res
        if self.movex == 0:
            self.frame = 0
            if self.prevx2 >= 0:
                self.image = self.images[0]  # If right use right idle frame
            else:
                self.image = pygame.transform.flip(self.images[0], True, False)
        if self.movex < 0:  # moving left
            self.frame += 1
            if self.frame > 3 * self.__ani:  # pausing on each frame for 3 tick
                self.frame = 1
            self.image = pygame.transform.flip(self.images[self.frame // 3],
                                               True, False)
            # '//' to ensure int and not float, transform flips right sprite
        if self.i_frame > 0 and not self.jumping:
            self.image = pygame.image.load(
                'images/sprites/Sprite1hitright.png').convert_alpha()
        if self.jumping and self.falling is False:  # If the user is jumping.
            self.jump_count += 1
            if self.jump_count >= 15:  # Timer for upward movement
                self.jumping = False
                self.jump_count = 0
                self.hang = True
                self.hang_count = 1
                self.jump_cd = 50 - (5 * self.agility)
        elif self.hang is True and self.hang_count <= 6:
            # Hang time after jumping before falling
            self.hang_count += 1
        else:  # Make user start falling
            self.falling = True
            self.hang = False
            self.hang_count = 0
        if self.jump_cd > 0:
            self.jump_cd -= 1
        if self.rect.bottom >= 640:  # Temporary magic number, pending map
            self.rect.bottom = 640
            self.movey = 0
            self.jumping = False
            self.falling = False
        if self.rect.right >= 960:
            self.rect.right = 960
        if self.rect.left <= 0:
            self.rect.left = 0
        self.rect.x += self.movex
        self.rect.y += self.movey
        self.climbing = False
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        land_list = pygame.sprite.spritecollide(self, plat_list, False)
        r_list = pygame.sprite.spritecollide(self, rope_list, False)
        self.collisionCheck(enemy_list, hit_list, land_list, r_list)
        if self.i_frame > 0:
            self.i_frame -= 1
        if self.curr_health <= 0:
            self.lives -= 1
            self.curr_health = self.health
            return True


    def gravity(self):
        if self.falling:
            self.movey += 5  # Fall faster than jump, looks better imo
            if self.slowfall:
                self.movey -= 3
        if self.jumping:
            self.movey -= 4
        if self.climbing:
            self.movey -= 8

    def jump(self, ovr=0):
        if ovr == 2:
            self.climbing = True
        elif self.falling is False and\
        self.jumping is False and\
        self.hang is False and\
        (self.jump_cd == 0 or ovr == 1):  # Don't want user infini-jumping from midair.
            self.jumping = True
            self.falling = False
            self.rect.y -= 5

    def collisionCheck(self, enemy_list, hit_list, land_list, r_list):
        '''Checks for collision with player'''
        for enemy in hit_list:
            if (enemy.rect.right >= self.rect.left + 40 and
                enemy.rect.left <= self.rect.right - 40) and\
            self.rect.bottom <= enemy.rect.bottom +\
            (enemy.rect.top - enemy.rect.bottom) // 2:
                self.falling = False
                self.jump(1)
                enemy.die(enemy_list)
                self.i_frame = 10
                if enemy not in enemy_list:
                    self.kills += 1
                continue
            elif self.i_frame == 0 and self.rect.bottom >= enemy.rect.bottom - (enemy.image.get_size()[1] // 2):
                if enemy.rect.right >= self.rect.left + 40 and\
                enemy.rect.left <= self.rect.right - 40 and\
                self.rect.bottom >= enemy.rect.top + 10:
                    self.curr_health -= enemy.damage
                    self.i_frame = 60
                    print("Health: {}/{}".format(self.curr_health,
                                                 self.health))
                    break
        for p in land_list:
            tmp_x = (self.rect.left + (self.image.get_size()[0] // 2))
            if p.rect.left - 5 <= tmp_x and p.rect.right + 5 >= tmp_x:
                if self.rect.top + 50 <= p.rect.top:
                    self.falling = False
                    self.hang = False
                    self.movey = 0
                    self.jump_count = 0
                if self.rect.bottom <= p.rect.top + 5:
                    self.rect.bottom = p.rect.top + 5
                    self.jumping = False
        for r in r_list:
            tmp_x = (self.rect.left + (self.image.get_size()[0] // 2))
            if r.rect.top + 6 < self.rect.top and r.rect.bottom >= self.rect.top:
                if r.rect.left <= tmp_x and r.rect.right >= tmp_x:
                    self.climbing = True
                    self.jumping = False
                    self.hang = False
            elif r.rect.top <= self.rect.top:
                if r.rect.left - 5 <= tmp_x and r.rect.right + 5 >= tmp_x:
                    self.rect.top = r.rect.top
                    if self.movey < 0:
                        self.movey = 0
            else:
                if not self.climbing:
                    if r.rect.left - 5 <= tmp_x and r.rect.right + 5 >= tmp_x:
                        self.slowfall = True
        if len(r_list) == 0:
            self.climbing = False
            self.slowfall = False
