# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Init pygame
    pygame.init()

    # Console Printout
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    # Screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group() 

    # Static container
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, drawable, updatable)

    # Game Time
    game_time = pygame.time.Clock()
    dt = 0

    # Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    # Gameloop
    while (True):
        # Detect exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # Updatable Group Updating
        dt = game_time.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            # Bullet Vs. Asteroid Collision
            for bullet in bullets:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()
            # Player Vs. Asteroid Collision
            if (asteroid.collision(player)):
                print("Game over!")
                return

        # Drawable
        for item in drawable:
            item.draw(screen)


        # Screen update
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
