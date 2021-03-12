import sqlite3
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)





# for passwordDb in db.execute("SELECT password FROM users WHERE (username=?)", (username,)):
#     print(passwordDb[0])
#     # if usernameDb == username and passwordDb == password:
#     print("Login successful as {}".format(username))
#     # else:
#     #     print(username, password)
for username in db.execute("SELECT username FROM users"):
    print(username[0])
