from circleshape import *
from constants import ASTEROID_MIN_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(-random_angle)
            new_velocity_2 = self.velocity.rotate(random_angle)
            