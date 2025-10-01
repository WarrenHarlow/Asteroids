import pygame
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # remove this asteroid
        self.kill()

        from constants import ASTEROID_MIN_RADIUS

        # don't spawn smaller asteroids if we're already at the minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # base direction vector (fallback if current velocity is zero)
        base_vec = self.velocity if self.velocity.length() != 0 else pygame.Vector2(0, 1)

        # random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # create two new direction vectors rotated in opposite directions
        vec1 = base_vec.rotate(random_angle)
        vec2 = base_vec.rotate(-random_angle)

        # compute new radius per assignment
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # spawn two smaller asteroids at this position with scaled up velocities
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vec1 * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vec2 * 1.2