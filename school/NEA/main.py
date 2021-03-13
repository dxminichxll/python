import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
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
        username (str): username of user.
        _password (str): password of user

    Methods:
        searchUser: Searches for a user in the users database,
                    basically a login method
        registerUser: Adds new user to the database, basically a sign up method
    """

    def __init__(self, username, password):
        self.username = username
        self._password = password


    def searchUser(self):
        print(self.username, self._password)
        print('='*30)
        if self.username in [username[0] for username in db.execute("SELECT username FROM users")]:
            print("username exists")

        else:
            print("username does not exist, Let's get you signed up")
            self.registerUser()

        for password in db.execute("SELECT password FROM users WHERE (username=?)", (self.username,)):
            password = password[0]
            # print(password)
            if self._password == password:
                print("Login successful as {}".format(self.username))
            else:
                print("Incorrect password")


    def registerUser(self):
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        passwordConfirm = input("Confirm password")
        if password == passwordConfirm:
            db.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            self.username = username
            self._password = password
        self.searchUser()


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


# username = input("Enter username: ")
# password = input("Enter password: ")
username = 'dom'
password = 'password'
player1 = Player(username, password)
# user.searchUser()
username = 'mac'
password = 'ok'
player2 = Player(username, password)
stats()

# print(player1.__doc__)

print(player1.username)
print(player1._password)

print(player2.username)
print(player2._password)


db.commit()
db.close()
