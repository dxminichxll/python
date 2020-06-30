import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE  IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
# db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
# db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")
# db.execute("DELETE FROM contacts WHERE email = 'tim@email.com'")
# execute is used to create the database

cursor = db.cursor()
# ^^ Cursors are used to query the database
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("-"*20)
# ^^ you cant use a cursor twice because it runs out of lines to print
# This makes it efficient in querying databases
cursor.close()
db.commit()
# ^^ you have to commit any changes you have made to the database otherwise it will not be saved
db.close()


