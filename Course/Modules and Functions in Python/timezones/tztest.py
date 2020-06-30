import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# ========================================================

# for x in pytz.all_timezones:
#     print(x)
# # Prints all supported timezones

# ========================================================

# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
# # prints all timezones in order
#
# ========================================================
#
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}". format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
# # prints all countries and their different timezones
# .get() function fetches a value from a list but doesn't give an error if the value doesn't exist

# ========================================================

for x in sorted(pytz.country_names):
    print("{}: {}". format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

# Prints all countries and timezones within the country
# Specifies if there is no time zone
# It also shows the time in the timezone

