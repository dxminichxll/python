import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import tkinter as tk
# Connect to database and create table if needed
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("""CREATE TABLE  IF NOT EXISTS users (username TEXT,
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
        searchUser: Searches for a user in the users database,
                    basically a login method
        registerUser: Adds new user to the database, basically a sign up method
    """

    def __init__(self, username, password):
        self.username = username
        self._password = password


    def search(self):
        print(self.username, self._password)
        print('='*30)
        if self.username in [username[0] for username in db.execute("SELECT username FROM users")]:
            print("username exists")

        else:
            print("username does not exist, Let's get you signed up")
            self.register()

        for password in db.execute("SELECT password FROM users WHERE (username=?)", (self.username,)):
            password = password[0]
            # print(password)
            if self._password == password:
                print("Login successful as {}".format(self.username))
                return True
            else:
                print("Incorrect password")


    def register(self):
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        passwordConfirm = input("Confirm password")
        if password == passwordConfirm:
            db.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            self.username = username
            self._password = password
        self.search()


def stats():
    df = pd.read_sql_query("SELECT * FROM users", db)

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2,
                                              ncols=2,
                                              figsize=(10,10))
    # Add data to ax0
    bar1 = ax0.bar(x=df["username"],
                   height=df["wins"])
    ax0.set(title="Wins",
            xlabel="User",
            ylabel="Number of wins")

    ax0.axhline(y=df["wins"].mean(), linestyle="--", color='black')
# ============================================================
    bar2 = ax1.bar(x=df["username"],
                   height=df["losses"],
                   color='red')
    ax1.set(title="Losses",
            xlabel="User",
            ylabel="Number of losses")

    ax1.axhline(y=df["losses"].mean(), linestyle="--", color='black')
# ============================================================
    bar3 = ax2.bar(x=df["username"],
                   height=df["wins"] / (df["wins"] + df["losses"]),
                   color='green')
    ax2.set(title="Win rate",
            xlabel="User",
            ylabel="Win rate (%)")

    ax2.axhline(y=(df["wins"] / (df["wins"] + df["losses"])).mean(), linestyle="--", color='black')
# ============================================================

    plt.show()


class GUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master
        self.master.title("Dice game")
        self.master.geometry('640x480-8-200')
        self.frame = tk.Frame(self.master)


class UserAuthentification(GUI):
    def __init__(self, master):
        GUI.__init__(self, master)
        playerText = tk.Variable(self.frame)
        playerText.set("Sign in as player 1")
        self.playerLabel = tk.Label(self.frame, textvariable=playerText)
        self.playerLabel.config(font=("Courier", 30))
        self.usernameLabel = tk.Label(self.frame, text='Username:')
        self.usernameEntry1 = tk.Entry(self.frame, width=30)
        self.passwordLabel = tk.Label(self.frame, text='Password:')
        self.passwordEntry1 = tk.Entry(self.frame, width=30)
        self.button1 = tk.Button(self.frame, text='Sign in',
                                             width=25,
                                             command=self.sign_in)


        self.playerLabel.pack()
        self.usernameLabel.pack()
        self.usernameEntry1.pack()
        self.passwordLabel.pack()
        self.passwordEntry1.pack()
        self.button1.pack(pady=8)
        self.frame.pack()
    def sign_in(self):
        username = self.usernameEntry1.get()
        password = self.passwordEntry1.get()
        print(username, password)
        player1 = Player(username, password)
        if player1.search() == True:
            self.newWindow = tk.Toplevel(self.master)
            self.app = MainApplication(self.newWindow)



class MainApplication(GUI):
    def __init__(self, master):
        GUI.__init__(self, master)
        self.button1 = tk.Button(self.frame, text = 'Statistics', width = 25, command = self.show_statistics)
        self.button1.pack()
        self.frame.pack()
    def show_statistics(self):
        stats()




if __name__ == '__main__':
    # username = input("Enter username: ")
    # password = input("Enter password: ")
    # username = 'dom'
    # password = 'password'
    # player1 = Player(username, password)
    # # user.search()
    # username = 'mac'
    # password = 'ok'
    # player2 = Player(username, password)
    # stats()

    # print(player1.username)
    # print(player1._password)
    #
    # print(player2.username)
    # print(player2._password)

    root = tk.Tk()
    # print(root)
    # app = GUI(root)
    # root.mainloop()

    # root2 = tk.Tk()
    app = UserAuthentification(root)
    root.mainloop()

db.commit()
db.close()
