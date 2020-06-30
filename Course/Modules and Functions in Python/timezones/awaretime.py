import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))
# "naive" means it doesn't account for daylight saving time(DST)

aware_local_time = pytz.utc.localize(utc_time).astimezone()
# The astimezone() function will find the timezone of the local computer
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time: {}, Time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())
# timestamp() prints the seconds since the epoch

s = 1445733000
t = s + (60 * 60)
# Sets the time stamp to one hour later
gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
