import time

# print(time.gmtime(0))

# print(time.localtime())
# # This prints a named tuple which can be used to easily access each data value
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day", time_here[2], time_here.tm_mday)

import time
from time import time as my_timer
# # Time deals with real times rather than measuring durations
# from time import perf_counter as my_timer
# # This records actually elapsed time
# from time import monotonic as my_timer
# from time import process_time as my_timer
# # Process_time records the time where the CPU is used
import random

input("press enter to start")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))
# strft stands for string from time and this translates the time into a more readable form
# the '%X' argument means to only show the appropriate time, not the date

print("your reaction time was {} seconds".format(end_time - start_time))