__author__ = "israel ashush"

import pygame
import random

DEFAULT_PLAYER = "default_player.png"
PINK = (255,174,201)

class plane(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, img = DEFAULT_PLAYER):
        """

        :param x: rect.x
        :param y: rect.y
        :param img: icone_player
        """
        super(plane,self).__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = random.randint(-1,1)
        self.move_y = random.randint(-1,1)

    def update_move(self, x, y):
        self.move_x = x
        self.move_y = y

    def update_pos(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_move(self):
        return self.move_x, self.move_y

    def get_pos(self):
        return self.rect.x, self.rect.y


