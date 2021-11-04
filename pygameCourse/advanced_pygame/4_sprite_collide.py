import pygame, random

# Initialise pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite groups")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define classes

class Player(pygame.sprite.Sprite):
    """A simple class to represent a player"""
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5

        self.monster_group = monster_group
    
    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()

    def move(self):
        """Move the player continuously"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
    
    def check_collisions(self):
        """Check for collsions between player(self) and monster group"""
        if pygame.sprite.spritecollide(self, monster_group, True):
            print(len(monster_group))



class Monster(pygame.sprite.Sprite):
    """A simple class to represent a monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = random.randint(1, 10)
    
    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity



# Create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

# Create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player)


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display
    display_surface.fill((0,0,0))

    # Updata and draw assets
    player_group.update()
    player_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()