import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, killer):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            newVelocity1 = self.velocity.rotate(split_angle)
            newVelocity2 = self.velocity.rotate(-split_angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            newAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid1.velocity = newVelocity1 * 1.5
            newAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid2.velocity = newVelocity2 * 1.5
