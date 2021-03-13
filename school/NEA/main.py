import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import tkinter as tk
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
        register(): Adds new user to the database, basically a sign up method
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
            print("username does not exist")
            userAuthApp.errorText.set("Username does not exist, try signing up")
            self.register()

        for password in db.execute("SELECT password FROM users WHERE (username=?)", (self.username,)):
            password = password[0]
            # print(password)
            if self._password == password:
                print("Login successful as {}".format(self.username))
                return True
            else:
                print("Incorrect password")
                userAuthApp.errorText.set("Incorrect password, please try again")


def register(username, password):
    allUsernames=[]
    for row in db.execute("SELECT username FROM users"):
        allUsernames.append(row[0])
    if username not in allUsernames:
        db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (username, password, 0, 0, 0))
        userAuthApp.signUpApp.errorText.set("Account created, exit this tab and log in")
    else:
        userAuthApp.signUpApp.errorText.set("Username already in use")
        # self.username = username
        # self._password = password
    # self.search()

    # # TODO: add password strength test


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
        # self.master.title("Dice game")
        self.master.geometry('640x480-8-200')
        self.frame = tk.Frame(self.master)


class UserAuthentification(GUI):
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
        self.passwordEntry1 = tk.Entry(self.frame, width=30)
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
        print(username, password)
        if self.currentPlayer == 'player 1':
            player1 = Player(username, password)
            if player1.search() == True:
                self.errorText.set(' ')
                self.playerText.set('Sign in as player 2')
                self.currentPlayer = 'player 2'
        else:
            print("Test1")
            player2 = Player(username, password)
            print("Test2")
            print(player2.search())
            if player2.search() == True:
                self.master.destroy()
                root = tk.Tk()
                app = MainApplication(root)
                root.mainloop()
                # self.newWindow = tk.Toplevel(self.master)
                # self.app = MainApplication(self.newWindow)

    def sign_up(self):
        root2 = tk.Tk()
        self.signUpApp = SignUp(root2)
        root2.mainloop()

class SignUp(UserAuthentification):
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
    def __init__(self, master):
        GUI.__init__(self, master)
        self.button1 = tk.Button(self.frame, text = 'Statistics', width = 25, command = self.show_statistics)
        self.button1.pack()
        self.frame.pack()
    def show_statistics(self):
        stats()




if __name__ == '__main__':


    root = tk.Tk()
    userAuthApp = UserAuthentification(root)
    root.mainloop()

db.commit()
db.close()
