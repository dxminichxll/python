# Import all libraries
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import tkinter as tk
from PIL import ImageTk, Image
import time
import random
# Connect to database and create table if needed
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("""CREATE TABLE IF NOT EXISTS users (username TEXT,
                                                 password TEXT,
                                                 wins INTEGER,
                                                 losses INTEGER,
                                                 best_score INTEGER)""")

# db.execute("INSERT INTO users(username, password, wins, losses, best_score) VALUES('domhill', '12345', 16, 10, 100)")
# db.execute("INSERT INTO users(username, password, wins, losses, best_score) VALUES('dom', 'password', 100, 17, 178)")
# db.execute("INSERT INTO users(username, password, wins, losses, best_score) VALUES('mac', 'ok', 1, 15, 20)")


class Player():

    """Class to represent a player

    Attributes:
        username (str): username of user
        _password (str): password of user

    Methods:
        search(): Searches for a user in the users database,
                    basically a login method
    """

    def __init__(self, username, password):
        self.username = username
        self._password = password


    def search(self):
        print(self.username, self._password)
        print('='*30)
        # Check if username is in database
        if self.username in [username[0] for username in db.execute("SELECT username FROM users")]:
            print("username exists")

        else:
            print("username does not exist")
            app.errorText.set("Username does not exist, try signing up")
            app.passwordEntry1.delete(0, 'end')

        for password in db.execute("SELECT password FROM users WHERE (username=?)", (self.username,)):
            password = password[0] # select password for username from database
            if self._password == password:
                print("Login successful as {}".format(self.username))
                return True # login is successful
            else:
                print("Incorrect password")
                app.errorText.set("Incorrect password, please try again")
                app.passwordEntry1.delete(0, 'end')


def register(username, password):
    allUsernames=[]
    for row in db.execute("SELECT username FROM users"): # check database for usernames
        allUsernames.append(row[0])
    if username not in allUsernames: # if username not already in database:
        # Add user to sqlite database
        db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (username, password, 0, 0, 0))
        app.signUpApp.errorText.set("Account created, exit this tab and log in")
    else:
        app.signUpApp.errorText.set("Username already in use")

    # TODO: add password strength test


def stats(): # Creates and presents statistics for each user

    # Create a pandas DataFrame from sqlite database
    df = pd.read_sql_query("SELECT * FROM users", db)

    # Create subplots for graphs
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2,
                                              ncols=2,
                                              figsize=(10, 10))
    # Add data to ax0 (first graph)
    bar1 = ax0.bar(x=df["username"],
                   height=df["wins"])
    ax0.set(title="Wins",
            xlabel="User",
            ylabel="Number of wins") # customisation

    ax0.axhline(y=df["wins"].mean(), linestyle="--", color='black') # mean line
# ============================================================
    # Add data to ax1 (second graph)
    bar2 = ax1.bar(x=df["username"],
                   height=df["losses"],
                   color='red')
    ax1.set(title="Losses",
            xlabel="User",
            ylabel="Number of losses") # customisation

    ax1.axhline(y=df["losses"].mean(),
                linestyle="--",
                color='black') # mean line
# ============================================================
    # Add data to ax2 (first graph)
    bar3 = ax2.bar(x=df["username"],
                   height=df["wins"] / (df["wins"] + df["losses"]),
                   color='green')
    ax2.set(title="Win rate",
            xlabel="User",
            ylabel="Win rate (%)") # customisation

    ax2.axhline(y=(df["wins"] / (df["wins"] + df["losses"])).mean(),
                linestyle="--",
                color='black') # mean line
# ============================================================

    plt.show() # Presents graphs


class GUI(tk.Frame):
    """
        Parent class for all GUI-based subclasses
    """
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master
        self.master.geometry('640x480-8-200')
        self.frame = tk.Frame(self.master)


class UserAuthentification(GUI):
    """
        Class for user login
        Subclass of 'GUI' class

        Creates all tkinter widgets for login

        Methods:
        sign_in(): passes information to the Player class and calls its
                   'search()' method to search for user. Will then log in
                   user if the password is right
        sign_up(): Creates a new window for a user to sign up

    """
    def __init__(self, master):
        GUI.__init__(self, master)
        self.master.title("Login")
        self.currentPlayer = 'player 1'
        self.playerText = tk.Variable(self.frame)
        self.errorText = tk.Variable(self.frame)
        self.playerText.set("Sign in as player 1")
        self.playerLabel = tk.Label(self.frame, textvariable=self.playerText)
        self.playerLabel.config(font=("Courier", 30))
        self.usernameLabel = tk.Label(self.frame, text='Username:')
        self.usernameEntry1 = tk.Entry(self.frame, width=30)
        self.passwordLabel = tk.Label(self.frame, text='Password:')
        self.passwordEntry1 = tk.Entry(self.frame, show='*', width=30)
        self.signInButton = tk.Button(self.frame, text='Sign in',
                                             width=25,
                                             command=self.sign_in)
        self.signUpButton = tk.Button(self.frame, text='Sign up',
                                             width=25,
                                             command=self.sign_up)
        self.errorLabel = tk.Label(self.frame, textvariable=self.errorText)


        self.playerLabel.pack()
        self.usernameLabel.pack()
        self.usernameEntry1.pack()
        self.passwordLabel.pack()
        self.passwordEntry1.pack()
        self.signInButton.pack(pady=8)
        self.signUpButton.pack()
        self.errorLabel.pack()
        self.frame.pack()
    def sign_in(self):
        username = self.usernameEntry1.get()
        password = self.passwordEntry1.get()
        # Checks if player 1 or player 2 is signing in
        if self.currentPlayer == 'player 1':
            global player1
            player1 = Player(username, password)
            if player1.search() == True: # if username and password is correct:
                # Set up GUI to sign in player 2
                self.errorText.set(' ')
                self.usernameEntry1.delete(0, 'end')
                self.passwordEntry1.delete(0, 'end')
                self.playerText.set('Sign in as player 2')
                self.currentPlayer = 'player 2'
        else: # sign in player 2
            global player2
            player2 = Player(username, password)
            if player2.search() == True: # if username and password is correct:
                self.master.destroy() # destroy current window
                root = tk.Tk()
                app = MainApplication(root)
                root.mainloop() # create new window (main game)

    def sign_up(self):
        root2 = tk.Tk()
        self.signUpApp = SignUp(root2)
        root2.mainloop() # create pop-up for sign up

class SignUp(UserAuthentification):

    """
        Class for creating new user

        Subclass of 'UserAuthentification' class (inherits all properties)

        Methods:
        sign_up(): passes information to the 'register()' function to
                   add new user to database
    """
    def __init__(self, master):
        UserAuthentification.__init__(self, master)
        self.master.title("Sign up")
        self.playerText.set("Sign up")
        self.signInButton.destroy()

    def sign_up(self):
        username = self.usernameEntry1.get()
        password = self.passwordEntry1.get()
        register(username, password)



class MainApplication(GUI):

    """
        Class handling the main game

        Subclass of 'GUI' parent class

        Not yet finished, just checking statistics and accounts are working

    """
    def __init__(self, master):
        GUI.__init__(self, master)
        self.master.title("Dice Game")
        self.master['pady'] = 10
        self.master['padx'] = 10
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)

        self.playerTextRaw = "Player 1: {} \nPlayer 2: {}".format(player1.username, player2.username)
        self.playerText = tk.Variable()
        self.playerText.set(self.playerTextRaw)
        self.button1 = tk.Button(self.master, text = 'Statistics', width = 10, command = self.show_statistics)
        self.playerLabel = tk.Label(self.master, textvariable=self.playerText)
        self.rollButton = tk.Button(self.master, text='Roll dice', width=40, command=self.roll)

        self.button1.grid(row=0, column=0, sticky='nw')
        self.playerLabel.grid(row=0, column=4, sticky='ne')
        self.rollButton.grid(row=2, column=1, columnspan=2)

        self.image = Image.open("images/dice1.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice1Image = ImageTk.PhotoImage(self.image)

        self.image = Image.open("images/dice2.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice2Image = ImageTk.PhotoImage(self.image)

        self.image = Image.open("images/dice3.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice3Image = ImageTk.PhotoImage(self.image)

        self.image = Image.open("images/dice4.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice4Image = ImageTk.PhotoImage(self.image)

        self.image = Image.open("images/dice5.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice5Image = ImageTk.PhotoImage(self.image)

        self.image = Image.open("images/dice6.jpg")
        self.image = self.image.resize((80,80), Image.ANTIALIAS)
        self.dice6Image = ImageTk.PhotoImage(self.image)


        self.dice1ImageLabel = tk.Label(self.master, image=self.dice1Image)
        self.dice1ImageLabel.grid(row=1, column=1)
        self.dice2ImageLabel = tk.Label(self.master, image=self.dice2Image)
        self.dice2ImageLabel.grid(row=1, column=2)


        # =============================== dice rolling
    def roll(self):
        self.count = 0.01
        self.dice = [self.dice1Image, self.dice2Image, self.dice3Image, self.dice4Image, self.dice5Image, self.dice6Image]
        for i in range(1, 100):
            self.master.update()
            randompic1 = random.choice(self.dice)
            randompic2 = random.choice(self.dice)
            self.dice1ImageLabel.configure(image=randompic1)
            time.sleep(self.count)
            self.dice2ImageLabel.configure(image=randompic2)
            time.sleep(self.count)
            self.count = self.count * 1.5

            print(self.count)

            if self.count > 0.5:
                self.dice1 = randompic1
                self.dice2 = randompic2
                break
        print('dice stopped')
        self.dice1 = int(str(self.dice1)[-1])
        self.dice2 = int(str(self.dice2)[-1])
        print(self.dice1)
        print(self.dice2)

        self.add_dice(self.dice1, self.dice2)

    def add_dice(self, dice1, dice2):
        print(dice1 + dice2)










    def show_statistics(self):
        stats()




if __name__ == '__main__': # main program
    root = tk.Tk()
    # app = UserAuthentification(root)

    # player1 = Player('dom', 'password')
    # player2 = Player('mac', 'ok')
    app = UserAuthentification(root)

    root.mainloop() # creates login window

# Commit and database changes and close it
db.commit()
db.close()
