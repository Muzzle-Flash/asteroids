import pygame
from circleshape import *
from constants import *
from shot import *

class Player (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.fireDelay = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation).normalize()
        self.velocity = forward * PLAYER_SPEED
        self.position += self.velocity * dt

    def update(self, dt):
        self.fireDelay -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt*-1)
            self.move(0)
        if keys[pygame.K_d]:
            self.rotate(dt)
            self.move(0)
        if keys[pygame.K_w]:
            self.move(dt)
            self.rotate(0)
        if keys[pygame.K_s]:
            self.move(dt*-1)
            self.rotate(0)
        if keys[pygame.K_SPACE]:
            self.move(0)
            self.rotate(0)
            self.shoot()
    
    def shoot(self):
        if self.fireDelay <= 0:
            forward = pygame.Vector2(0,1).rotate(self.rotation).normalize()
            firingPosition = pygame.Vector2(self.position.x, self.position.y) + forward * PLAYER_RADIUS
            shot = Shot(firingPosition.x, firingPosition.y, SHOT_RADIUS) 
            shot.velocity = (forward * (SHOT_SPEED)) + self.velocity
            print(f"shot velocity: {shot.velocity}")
            print(f"shot position: {shot.position}")
            self.fireDelay = (60/PLAYER_RPM)