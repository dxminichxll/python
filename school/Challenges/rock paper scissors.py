import random
name = input("what is your name?")
print("hello", name)
again = "y"
while again == "y":
    p_score = 0
    c_score = 0

    while p_score < 3 and c_score < 3:

        player = input("rock (r) paper (p) or scissors (s)")

        if player == 'r' or player == 'p' or player == 's':

            chosen = random.randint(1,3)
            if chosen == 1:
                computer = "r"
            elif chosen == 2:
                computer = "p"
            elif chosen == 3:
                computer = "s"

            print(player + " vs " + computer)
            if player == computer:
               print("DRAW")
               win = ""
            elif player == "r" and computer == "s":
                win = True
                print("YOU WIN!")
            elif player == "p" and computer == "r":
                win = True
                print("YOU WIN!")
            elif player == "s" and computer =="p":
                win = True
                print("YOU WIN!")
            elif computer == "r" and player == "s":
                win = False
                print("YOU LOSE")
            elif computer == "p" and player == "r":
                win = False
                print("YOU LOSE")
            elif computer == "s" and player == "p":
                win = False
                print("YOU LOSE")

            if win == True:
                p_score = p_score + 1
                print(p_score,"-",c_score)
                win = ''

            elif not win:
                c_score = c_score + 1
                print(p_score, "-", c_score)
                win = ''
        else:
            print('please enter a valid input')
    if p_score > c_score:
        print("YOU HAVE WON THE GAME")
    elif c_score > p_score:
        print("YOU HAVE LOST THE GAME")
    again = "n"
    again = input("would you like to play again "+name+"?(y/n)\n")
