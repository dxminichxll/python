import pygame

pygame.init()

win = pygame.display.set_mode((426, 768))

pygame.display.set_caption("Flappy")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
#              pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
#              pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
#             pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
#             pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

images = pygame.image.load('bird_wing_down.png')
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (426, 768))
char = pygame.image.load('bird_wing_down.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.jumpCount = 0
        self.isJump = 5

    def draw(self, win):
        win.blit(images, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)


    pygame.display.update()


# mainloop
man = player(200, 410, 20, 20)
run = True
velocities = []
ys = []
jumpCounter = []
while run:
    clock.tick(17)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_SPACE]:
    #     neg = 1
    #     man.y += (man.jumpCount ** 2) * 0.5 * neg
    # else:
    #     neg = -1
    #     man.y -= (man.jumpCount ** 2) * 0.5 * neg
    # if man.jumpCount >= -10:
    #     neg = 1
    #     if man.jumpCount < 0:
    #         neg = -1
    #     man.y -= (man.jumpCount ** 2) * 0.5 * neg
    #     man.jumpCount -= 1
    # else:
    #     man.isJump = False
    #     man.jumpCount = 10


    if keys[pygame.K_SPACE]:
        neg = -1
        # man.vel = 0
        man.jumpCount = 50

    # elif man.jumpCount == 0:
    #     neg = 1

    if man.jumpCount > 40:
        man.vel -= 0.25
    else:
        neg = 1
        if man.vel <= 5:
            man.vel += 0.5

    man.y += (man.vel ** 2) * 0.5 * neg
    # man.vel += 0.5
    print(neg, man.vel, "\t", man.y, keys[pygame.K_SPACE])

    # if man.jumpCount < 15 and man.jumpCount > 1:
    #     man.vel -= 0.5
    if man.jumpCount > 0:
        man.jumpCount -= 1

    velocities.append(man.vel)
    ys.append(man.y)
    jumpCounter.append(man.jumpCount)



    redrawGameWindow()


pygame.quit()

import matplotlib.pyplot as plt
plt.plot(ys, scaley=True)
plt.plot(velocities, scaley=True)
plt.plot(jumpCounter, scaley=True)
plt.ylabel('some numbers')
plt.show()
