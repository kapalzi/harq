import pygame, sys, os
from pygame.locals import *

class Packet:
    def __init__(self, _surface, _color, _x):
        self.surface = _surface
        self.color = _color
        self.rect = pygame.Rect(20*_x, 10, 15, 30)
        self.direction = 1

    def setColor(self, _color):
        self.color = _color

    def setDirection(self, _direction):
        self.direction = _direction

    def setRect(self, _rect):
        self.rect = _rect

    def setSurface(self, _surface):
        self.surface = _surface

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        self.rect = self.rect.move(0, self.direction)