import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print('Game over!')
                exit()
            for shot in shots:
                if asteroid.isColliding(shot):
                    asteroid.split()
                    shot.kill()
        # player.update(dt)

if __name__ == "__main__":
    main()
