import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        # Return if small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle: float = random.uniform(20.0, 50.0) # 20-50 degrees
        first_vector: pygame.Vector2 = self.velocity.rotate(random_angle)
        second_vector: pygame.Vector2 = self.velocity.rotate(-random_angle)

        new_radius: float = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = first_vector * 1.2
        second_asteroid.velocity = second_vector * 1.2
