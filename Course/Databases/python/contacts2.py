import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
# update_cursor.execute(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
# ^^ the executescript() function is designed to execute more than one sql statement in one call
# You can do this by separating the statements with semi-colons and python will execute them one after the other
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

# for row in db.execute("SELECT * FROM contacts"):
#     print(row)

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-'*20)

db.close()
