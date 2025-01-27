import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__

    def draw(self, x, y, radius):
        pygame.draw.circle(x, y, radius, 2)

    def update(self):
        self.position += (self.velocity * dt)

