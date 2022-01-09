import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random


# Initialise pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Battle boats!")
blockSize = WINDOW_HEIGHT//9

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set colour variables
WHITE = (255, 255, 255)

letters =  ["A", "B", "C", "D", "E", "F", "G", "H"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
letterDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# Set font
font = pygame.font.SysFont('calibri', int(blockSize/1.5))

# Define classes
class Game():
    """A class to control gameplay"""
    def __init__(self, blockSize):
        # self.grid = [[0 for x in range (1, 9)] for y in range (1, 9)]
        self.blockSize = blockSize

    def draw(self):
        # Draw grid first
        for x in range(0, 9 * self.blockSize, self.blockSize):
            for y in range(0, 9 * self.blockSize, self.blockSize):
                if y == 0 and x != 0:
                    # print(int(x/blockSize))
                    text = font.render(letters[int(x/self.blockSize)- 1], True, WHITE)
                    text_rect = text.get_rect()
                    text_rect.left = x + self.blockSize / 4
                    text_rect.top = y + self.blockSize / 4
                    display_surface.blit(text, text_rect)

                if x == 0 and y != 0:
                    # print(int(x/blockSize))
                    text = font.render(numbers[int(y/self.blockSize)- 1], True, WHITE)
                    text_rect = text.get_rect()
                    text_rect.left = x + self.blockSize / 4
                    text_rect.top = y + self.blockSize / 4
                    display_surface.blit(text, text_rect)

                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                pygame.draw.rect(display_surface, WHITE, rect, 1)

    def alert(self, text):
        alertText = font.render(text, True, WHITE)
        alertRect = alertText.get_rect()
        alertRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        subText = font.render("Press enter to continue", True, WHITE)
        subRect = subText.get_rect()
        subRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)
        display_surface.blit(alertText, alertRect)
        display_surface.blit(subText,subRect)
        pygame.display.update()

        is_paused = True
        while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            is_paused = False
                    if event.type == pygame.QUIT:
                        is_paused = False
                        running = False


class Player():
    """A class that can manage a player"""
    def __init__(self):
        self.grid = [[0 for x in range (1, 9)] for y in range (1, 9)]

    def createGrid(self, computer=False): # Puts ships on the grid
        global letterDict
        if computer: # Create random ship placement for computer player
            for i in range(5):
                repeated = True
                while repeated == True:
                    num1, num2 = self.randomCoords()
                    if self.grid[num1][num2] == 0:
                        self.grid[num1][num2] = 1
                        repeated = False
                    elif self.grid[num1][num2] == 0:
                        repeated = True
        else: # Allow the user to choose their own coordinates for their ships
            print("""You will now be asked for the coordinates where you want to place your boat
            Please answer in the format like 'G6' or 'C4'""")
            for i in range(5):
                valid = False
                while valid == False:
                    try:
                        coordinate = input("Please enter coordinate {}: ".format(i + 1))
                        coordX, coordY = [char for char in coordinate]
                        coordX = coordX.upper()
                        # print(letterDict)
                        # print(letterDict[coordX])
                        coordX = letterDict[coordX] + 1
                        # print(coordX, coordY)
                        coordX = int(coordX) - 1
                        coordY = int(coordY) - 1
                        
                        if self.grid[coordX][coordY] == 1:
                            # print("Here")
                            raise ValueError('Repeated coordinate')
                        # print("Over here")
                        if self.grid[coordX][coordY] == 0:
                            # print("There")
                            self.grid[coordX][coordY] = 1
                    
                        valid = True
                    except:
                        print("Invalid input, please try again")
                        valid = False
                
            
    def randomCoords(self): # Creates 2 random numbers for coordinates
        num1 = random.randint(0, 7)
        num2 = random.randint(0, 7)
        return num1, num2

    def shoot(self, player, computer_grid, coordX, coordY, blockSize): # Sends a shot to the other players grid
        coordX = coordX // blockSize
        coordY = coordY // blockSize
        print(coordX-1, coordY-1)

        # Check if the the other grid has a ship on it
        if player == computer:

            pass
        else:
            print("Here")
            print(computer.grid[coordY-1][coordX-1])
            if computer.grid[coordY-1][coordX-1] == 1:
                print("HIT")
                return True


# Create a game object
my_game = Game(blockSize)


player = Player()
# for row in player.grid:
#     print(row)
player.createGrid()


computer = Player()
computer.createGrid(computer=True)
for row in computer.grid:
    print(row)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player wants to warp
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordX, coordY = pygame.mouse.get_pos()
            if coordX < blockSize * 9 and coordX > blockSize and coordY < blockSize * 9 and coordY > blockSize:
                if player.shoot(player, computer.grid, coordX, coordY, blockSize):
                    my_game.alert("Hit computer")


    # Update and draw the game
    my_game.draw()

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)


# End the game
pygame.quit()