# initiate variables
totalSticks = 15  # sets the starting amount of sticks
player = "Player 1" # states current player

def new_player(player):  # alternates between players
    if player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"


def sticks_remaining(totalSticks, player):  # determines if a player has won
    if totalSticks > 0:
        print("Sticks remaining: {}\n".format(totalSticks))
    else:
        print('='*40)
        print("The winner is {}".format(new_player(player)))
        # winner is determined calculating the opposite player
        quit()


while True:
    sticks = int(input(player + " Pick up 1,2 or 3 sticks: "))
    if 0 < sticks < 4 and sticks <= totalSticks:
        totalSticks -= sticks
        sticks_remaining(totalSticks, player)
    else:
        print("Please pick a valid number of sticks \n")

    player = new_player(player)
