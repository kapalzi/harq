import pygame, sys, os
from pygame.locals import *

simulationSpeed = 1 #1 - realtime
endToEndDelay = 5000 #5000ms
frameSize = 8
transmissionSpeed = 60

class SRController(object):
    def __init__(self):
        return

    def animation(self):
        clock = pygame.time.Clock()
        pygame.init()
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((1000, 500),0,32)
        running = True
        window.fill((255,255,255))

        moving_rect = Rect(10,10,15,30)
        bottom_rect = Rect(10, 460, 15, 30)
        top_rect = Rect(10, 10, 15, 30)
        direction = 10  # 1 w dol
        while running:
            window.fill((255, 255, 255))

            moving_rect = moving_rect.move(0,direction)

            if(moving_rect.contains(bottom_rect)):
                direction = -10

            if (moving_rect.contains(top_rect)):
                direction = 0

            pygame.draw.rect(window,(255,0,0),moving_rect)
            pygame.draw.rect(window, (0, 0, 255), top_rect)
            pygame.draw.rect(window, (0, 0, 255), bottom_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    running = False

            pygame.display.update()
            clock.tick(60)


