import sqlite3

db = sqlite3.connect('users.sqlite')

username = input('username: ')
password = input('password: ')

db.execute("CREATE TABLE IF NOT EXISTS USERS (username TEXT, password TEXT)")

def sign_up(username, password):
    if [(username, )] == [row for row in db.execute("SELECT username FROM users WHERE username = '{}'".format(username))]:
        print('incorrect password')
    else:
        db.execute("INSERT INTO USERS(username, password) VALUES('{}', '{}')"
        .format(username, password))
        print("Signed up {} with password '{}'".format(username, password))

def sign_in(username, password):
    if [(username, )] == [row for row in db.execute("SELECT username FROM users WHERE username = '{}'".format(username))]:
        if [(password, )] == [row for row in db.execute("SELECT password FROM users WHERE username = '{}'".format(username))]:
            print('access granted')
            return True
        else:
            print('access denied')
            return False

def cipher(text):
    cipher_text = []
    cipher2 = [char for char in "abcdefghijklmnopqrstuvwxyz\n ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    cipher1 = [char for char in "yzabcdefghijklmnopqrstuvwx\n YZABCDEFGHIJKLMNOPQRSTUVWX"]
    for char in text:
        cipher_letter = cipher1[cipher2.index(char)]
        cipher_text.append(cipher_letter)
    return "".join(cipher_text)

try:
    if sign_in(username,password):
        with open('text.txt','r') as file:
            print(cipher(file.read()))

    else:
        sign_up(username, password)
except IndexError:
    sign_up(username, password)


db.commit()
db.close()
