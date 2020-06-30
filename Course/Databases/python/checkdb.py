import sqlite3


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
#     PARSE_DECLTYPES makes python automatically convert datatypes that were referred to when creating the table
#     It converts the timestamp from a string into a timestamp

for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()