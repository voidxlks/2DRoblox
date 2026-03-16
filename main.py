import pygame
from player import Player
from world import World

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Python Roblox")

# Clock for FPS
clock = pygame.time.Clock()

# Create game objects
player = Player(400, 300)
world = World()

running = True

while running:
    clock.tick(60)  # 60 FPS

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Draw background
    screen.fill((135, 206, 235))

    # Draw world and player
    world.draw(screen)
    player.draw(screen)

    pygame.display.update()

pygame.quit()
