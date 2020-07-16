import tkinter

# initiate variables
while True:
    try:  # try-except block only allows integer input
        totalSticks = int(input("Pick a number of sticks for the game (less than 100000 and more than 10):"))  # sets the starting amount of sticks
        if 10 <= totalSticks <= 100000:  # doesn't allow input over 100000 (so the GUI doesn't break) or a number too small
            break
        else:
            print('test')
            continue

    except ValueError:
        continue

player = "Player 1"  # states current player
# num = 0


def new_player(player):  # alternates between players
    if player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"


def sticks_remaining(totalSticks, player):  # determines if a player has won
    if totalSticks > 0:  # Updates the GUI showing sticks remaining and the current player
        sticksText.set("Sticks remaining: {}\n".format(totalSticks))
        playerText.set("{}, please pick 1, 2 or 3 sticks".format(player))

    else:  # changes GUI to display the winner, and destroy other widgets
        playerText.set("")
        inputBox.destroy()
        header.destroy()
        sticksText.set("The winner is {}!".format(player))
        bg = sticksLabel.cget("background")
        fg = sticksLabel.cget("foreground")
        sticksLabel.configure(background=fg, foreground=bg)


def enter_pressed(event):  # function for when enter is pressed (user submits a number)
    global totalSticks
    global player
    try:
        num = int(inputBox.get())
        # sets the 'num' variable equal to the current integer in the input box when the enter key is pressed
    except ValueError:  # catches errors like using letters or box left blank
        num = 0  # resets 'num' variable to 0
    inputBox.delete(0, 'end')  # clears input box
    if 0 < num < 4 and num <= totalSticks:  # checks if the number is 1, 2 or 3
        totalSticks -= num  # subtracts the users number from the total amount of sticks
        player = new_player(player)  # alternates new player
        sticks_remaining(totalSticks, player)  # uses the sticks remaining function to check whether a player has won
    else:
        playerText.set("{}, Please pick a valid number of sticks(1, 2 or 3)".format(player))


# ============ Tkinter stuff ============

mainWindow = tkinter.Tk()  # creates tkinter object

mainWindow.bind('<Return>', enter_pressed)  # bind a function to the 'enter' key

mainWindow.title("Pick up sticks!")
mainWindow.geometry('640x480+8+400')

# configure grid for the widgets
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)

mainWindow.rowconfigure(0, weight=2)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=1)

# Header titled 'Pick up sticks!'
header = tkinter.Label(mainWindow, text='Pick up sticks!')
header.config(font=("Courier", 40))
header.grid(row=0, column=1, sticky='nsew')

# Text showing sticks remaining
sticksText = tkinter.Variable(mainWindow)
sticksText.set("Sticks remaining: {}\n".format(totalSticks))
sticksLabel = tkinter.Label(mainWindow, textvariable=sticksText)
sticksLabel.config(font=("Courier", 30))
sticksLabel.grid(row=1, column=1, sticky='nsew')

# Text showing which player's turn it is
playerText = tkinter.Variable(mainWindow)
playerText.set("{}, please pick 1, 2 or 3 sticks".format(player))
playerLabel = tkinter.Label(mainWindow, textvariable=playerText)
playerLabel.config(font=("Courier", 12))
playerLabel.grid(row=2, column=1, sticky='n')

# creates the input box for the player to enter numbers
inputBox = tkinter.Entry(mainWindow, justify='center')
inputBox.config(font=("Courier", 20))
inputBox.grid(row=2, column=1)

# starts the mainloop
mainWindow.mainloop()
