# import pandas as pd
import sqlite3
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE  IF NOT EXISTS users (username TEXT, password TEXT)")

# db.execute("INSERT INTO users(username, password) VALUES('domhill', '12345')")
# db.execute("INSERT INTO users(username, password) VALUES('dom', 'password')")
# db.execute("INSERT INTO users(username, password) VALUES('mac', 'ok')")

for username, password in db.execute("SELECT * FROM users"):
    all_users.append([username, password])

print('='*30)


class Users():

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


username = input("Enter username: ")
password = input("Enter password: ")
user = Users(username, password)
user.searchUser()

print(user.username)
print(user._password)

db.commit()
db.close()
