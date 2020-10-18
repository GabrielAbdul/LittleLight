#!/usr/bin/env python3
'''module that defines player class'''
import pygame


class Player(pygame.sprite.Sprite):
    '''class to define a player'''
    steps = 2 # Number of pixels per step. Repeated in startGame if needs changing
    jump_count = 0 # counter for jump time
    hang_count = 0 # counter for hang time after jumping

    def __init__(self):
        '''method to be called upon object instantiation'''
        super().__init__()
        img = pygame.image.load('images/sprites/Sprite1standright.png').convert_alpha()
        img1 = pygame.image.load('images/sprites/Sprite1stepright.png').convert_alpha()
        img1.convert_alpha()
        self.images = []
        self.images.append(img)
        self.images.append(img1)
        for i in range(2, 9):
            img = pygame.image.load('images/sprites/Sprite1stepright' + str(i) + '.png').convert_alpha()
            self.images.append(img)
        self.__ani = 8
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0 # x-axis movement: positive=right, negative=left
        self.movey = 0 # y-axis movement: positive=down, negative=up
        self.frame = 0 # sprite frame
        self.health = 0
        self.curr_health = 0
        self.strength = 1
        self.agility = 1
        self.glow = 1
        self.prevx = self.movex # logging previous x
        self.prevx2 = 0 # logging idle direction
        self.falling = True # Is the player falling
        self.jumping = False # Is the player jumping
        self.hang = False # Is the player hangin in the air
        self.i_frame = 0
        self.lives = 3

    def getStats(self):
        '''returns a dictionary of player stats'''
        tmp = self.__dict__.copy()
        res = {'health': tmp.get('health'),
               'curr_health': tmp.get('curr_health'),
                'agility': tmp.get('agility'),
                'strength': tmp.get('strength'),
                'glow': tmp.get('glow')}
        return res

    def updateStats(self, dict):
        '''method that updates stats'''
        for key, val in eval(dict).items():
            setattr(self, key, val)

    def control(self, x, y):
        '''Allows the player to control the character'''
        if (self.prevx < 0 and self.movex > 0 and x == 0) or (self.prevx > 0 and self.movex < 0 and x == 0):
            self.movex = self.prevx # Smoothing out movement when multiple keys pressed
            return
        if self.prevx != 0:
            self.prevx2 = self.prevx # Logging last direction faced
        self.prevx = self.movex
        self.movex = x
        self.movey = y

    def update(self, enemy_list):
        '''Update sprite position'''
        if self.movex > 0: # moving right
            self.frame += 1
            if self.frame > 3 * self.__ani: # pausing on each frame for 3 ticks due to gamespeed
                self.frame = 1
            self.image = self.images[self.frame // 3] # '//' to ensure int and not float
        if self.movex == 0:
            self.frame = 0
            if self.prevx2 >= 0:
                self.image = self.images[0] # If facing right, use right idle frame
            else:
                self.image = pygame.transform.flip(self.images[0], True, False)
        if self.movex < 0: # moving left
            self.frame += 1
            if self.frame > 3 * self.__ani: # pausing on each frame for 3 ticks due to gamespeed
                self.frame = 1
            self.image = pygame.transform.flip(self.images[self.frame // 3], True, False) # '//' to ensure int and not float, transform flips right sprite to left
        if self.i_frame > 0 and not self.jumping:
            self.image = pygame.image.load('images/sprites/Sprite1hitright.png').convert_alpha()
            if self.i_frame > 10 and self.i_frame < 30:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)
        if self.jumping and self.falling is False: # If the user is jumping. Falling check is redundant
            self.jump_count += 1
            if self.jump_count >= 15: # Timer for upward movement
                self.jumping = False
                self.jump_count = 0
                self.hang = True
                self.hang_count = 1
        elif self.hang is True and self.hang_count <= 6: # Hang time after jumping before falling: user makes a sharp parabola instead of triangle
            self.hang_count += 1
        else: # Make user start falling
            self.falling = True
            self.hang = False
            self.hang_count = 0
        if self.rect.bottom >= 640: # Temporary magic number, pending map and ground
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
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            if self.falling:
                if (enemy.rect.right >= self.rect.left + 40 and enemy.rect.left <= self.rect.right - 40) and self.rect.bottom >= enemy.rect.bottom + (enemy.rect.top - enemy.rect.bottom) // 2:
                    self.falling = False
                    self.jump()
                    enemy.die(enemy_list)
                    self.i_frame = 10
                    continue
            if self.i_frame == 0 and (not self.falling and not self.hang):
                if enemy.rect.right >= self.rect.left + 40 and enemy.rect.left <= self.rect.right - 40 and self.rect.bottom >= enemy.rect.top + 10:
                    self.curr_health -= enemy.damage
                    self.i_frame = 60
                    print("Health: {}/{}".format(self.curr_health, self.health))
                    break
        if self.i_frame > 0:
            self.i_frame -= 1
        if self.curr_health <= 0:
            self.lives -= 1
            self.curr_health = self.health
            return True

    def gravity(self):
        if self.falling:
            self.movey += 5 # Fall faster than jump, looks better imo
        if self.jumping:
            self.movey -= 4

    def jump(self):
        if self.falling is False and self.jumping is False and self.hang is False: # Don't want user infini-jumping from midair. Could implement double jump later
            self.jumping = True
            self.falling = False
            self.rect.y -= 10
