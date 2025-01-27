import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Shot.container = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    field = AsteroidField()
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()

        # limit to 60 FPS
        dt = clock.tick(60) / 1000


#    print("Starting asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()