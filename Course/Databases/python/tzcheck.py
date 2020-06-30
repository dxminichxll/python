import sqlite3
import pytz
import pickle


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
#     PARSE_DECLTYPES makes python automatically convert datatypes that were referred to when creating the table
#     It converts the timestamp from a string into a timestamp

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    # pickled_zone = row[3]
    # zone = pickle.loads(pickled_zone)
    zone = pytz.timezone("CET")
    local_time = pytz.utc.localize(utc_time).astimezone(zone)

    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()
