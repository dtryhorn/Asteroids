import sys

import pygame

from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()

    # Engine variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0

    # Groups
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    # Add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    # Game objects
    player: Player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    field: AsteroidField = AsteroidField()

    # Initial message
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)


        for asteroid in asteroids:
            # Check for asteroid collision with player
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            # Check for collision with shot
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()



        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
