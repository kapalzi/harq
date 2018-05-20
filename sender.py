import pygame, sys, os
from pygame.locals import *

class Sender:
    def __init__(self, _surface, _color, _x, _frame = 0):
        self.surface = _surface
        self.color = _color
        self.rect = pygame.Rect(20 * _x, 10, 15, 30)
        self.frame = _frame
    def setColor(self, _color):
        self.color = _color

    def setDirection(self, _direction):
        self.direction = _direction

    def setRect(self, _rect):
        self.rect = _rect

    def setSurface(self, _surface):
        self.surface = _surface

    def setFrame(self, _frame):
        self.frame = _frame

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


