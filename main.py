import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfelid import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")

    # create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # set containers so instances auto-add to these groups
    AsteroidField.containers = updatables
    Asteroid.containers = updatables, drawables, asteroids
    Shot.containers = updatables, drawables, shots
    Player.containers = updatables, drawables

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update all updatable sprites (passes dt to each sprite.update)
        updatables.update(dt)

        # check collisions between player and asteroids
        for asteroid in list(asteroids):
            if asteroid.collide(player):
                print("Game over!")
                pygame.quit()
                sys.exit(0)

        # check collisions between shots and asteroids
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collide(shot):
                    asteroid.split()  # spawn smaller asteroids (or kill if too small)
                    shot.kill()

        screen.fill((0, 0, 0))
        # draw each drawable sprite by calling its draw method
        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
