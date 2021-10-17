import pygame, random
from pygame.constants import WINDOWHIDDEN

# Initialise pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision detection")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_d] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_w] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_s] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    # Check for collision between two rects
    if dragon_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.left = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.top = random.randint(0, WINDOW_HEIGHT - 32)

    # Fill display surface
    display_surface.fill((0,0,0))

    # Draw rectangles to represent the rects of each object
    pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pygame.display.update()

    # Tick the clokc
    clock.tick(FPS)

# End the game
pygame.quit()