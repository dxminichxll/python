import tkinter
import time

# initiate variables
totalSticks = int(input("Pick a number of sticks for the game:"))
 # sets the starting amount of sticks
player = "Player 1" # states current player
text = 0

def new_player(player):  # alternates between players
    if player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"


def sticks_remaining(totalSticks, player):  # determines if a player has won
    if totalSticks > 0:
        sticksText.set("Sticks remaining: {}\n".format(totalSticks))
        playerText.set("{}, please pick 1, 2 or 3 sticks".format(player))
    else:
        print('='*40)
        playerText.set("")
        inputBox.destroy()
        header.destroy()
        sticksText.set("The winner is {}!".format(player))
        bg = sticksLabel.cget("background")
        fg = sticksLabel.cget("foreground")
        sticksLabel.configure(background=fg, foreground=bg)



mainWindow = tkinter.Tk()


def enterPressed(event):
    global totalSticks
    global player
    try:
        text = int(inputBox.get())
    except ValueError:
        inputBox.delete(0, 'end')
    inputBox.delete(0, 'end')
    print(text)
    # sticksText.set(player + " Pick up 1,2 or 3 sticks: ")
    if 0 < text < 4 and text <= totalSticks:
        totalSticks -= text
        sticks_remaining(totalSticks, player)
    else:
        playerText.set("{}, Please pick a valid number of sticks(1, 2 or 3)"
        .format(player))

    player = new_player(player)


mainWindow.bind('<Return>', enterPressed)

mainWindow.title("Pick up sticks!")
mainWindow.geometry('640x480+8+400')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)

mainWindow.rowconfigure(0, weight=2)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=1)

header = tkinter.Label(mainWindow, text='Pick up sticks!')
header.config(font=("Courier", 40))
header.grid(row=0, column=1, sticky='nsew')

sticksText = tkinter.Variable(mainWindow)
sticksText.set("Sticks remaining: {}\n".format(totalSticks))
sticksLabel = tkinter.Label(mainWindow, textvariable=sticksText)
sticksLabel.config(font=("Courier", 30))
sticksLabel.grid(row=1, column=1, sticky='nsew')

playerText = tkinter.Variable(mainWindow)
playerText.set("{}, please pick 1, 2 or 3 sticks".format(player))
playerLabel = tkinter.Label(mainWindow, textvariable=playerText)
playerLabel.config(font=("Courier", 15))
playerLabel.grid(row=2, column=1, sticky='n')

inputBox = tkinter.Entry(mainWindow, justify='center')
inputBox.config(font=("Courier", 20))
inputBox.grid(row=2, column=1)

mainWindow.mainloop()
