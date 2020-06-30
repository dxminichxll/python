import sqlite3

db = sqlite3.connect("contacts.sqlite")


usr_name = input("Enter a name to search:")


for name, phone, email in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (usr_name,)):
    print(name)
    print(phone)
    print(email)
    print('-'*20)

db.close()
