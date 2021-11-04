import pygame, random
from pygame.constants import QUIT

# Initialise pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brick Breaker!")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Create game class
class Game():
    """A class to coordinate the game"""
    
    def __init__(self, slider, ball):
        self.slider = slider
        self.ball = ball

    def update(self):
        self.check_collisions()
        # print(self.ball.x)
        # print(self.slider.rect.x)

    def check_collisions(self):
        # pass
        if self.slider.rect.colliderect(self.ball.rect):
            print("Hit")
            self.slider.hit_sound.play()
            self.ball.dx = -1 * self.ball.dx
        # if pygame.sprite.spritecollide(self.slider, self.ball, False):
        #     self.slider.hit_sound.play()
            

# Create brick class
class Brick(pygame.sprite.Sprite):
    
    def __init__():
        pass

# Create slider class
class Slider(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("slider.png")
        self.image = pygame.transform.scale(self.image, (200, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH - 100, WINDOW_HEIGHT//2)

        self.velocity = 10

        self.hit_sound = pygame.mixer.Sound("player_hit.wav")

    def update(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.velocity        
        if keys[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity
        

# Create ball class
class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        # self.rect = pygame.draw.circle(display_surface, (255,255,255), (self.x, self.y), (12), 0)
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1, WINDOW_WIDTH), random.randint(1, WINDOW_HEIGHT))


        # self.circle = pygame.draw.circle(display_surface, (255,255,255), (self.x, self.y), (10))
        # self.circle = self.circle.get_rect()
        self.velocity = 10

        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    
    def update(self):
        # self.rect = pygame.draw.circle(display_surface, (255,255,255), (self.x, self.y), (12), 0)

        # pygame.draw.circle(display_surface, (255,255,255), (self.x, self.y), (12), 0)
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        # Bounce the ball off the edges of the display
        # if self.x - self.radius <= 0 or self.x + self.radius >= WINDOW_WIDTH:
        #     self.dx = -1 * self.dx
        # if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT:
        #     self.dy = -1 * self.dy

        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1 * self.dx
            print("Sides")
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.dy = -1 * self.dy
            print("top")



# Create brick group
bricks = pygame.sprite.Group()

# Create slider group
slider_group = pygame.sprite.Group()
slider = Slider()
slider_group.add(slider)

# Create ball group
ball_group = pygame.sprite.Group()
# for i in range(1, 1000):
ball = Ball()
ball_group.add(ball)

my_game = Game(slider, ball)



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the display
    display_surface.fill((0, 0, 0))

    ball_group.update()
    ball_group.draw(display_surface)

    slider_group.update()
    slider_group.draw(display_surface)

    my_game.update()
    # ball.draw(display_surface)
    # for balle in ball.sprites():
    #     print(balle.circle)


    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)


# Quit the game
pygame.quit()