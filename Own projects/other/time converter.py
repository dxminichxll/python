def seconds(time, unit):
    if unit == 'weeks':
        seconds = time * 604800
    elif unit == 'days':
        seconds = time * 86400
    elif unit == 'hours':
        seconds = time * 3600
    elif unit == 'minutes':
        seconds = time * 60
    elif unit == 'seconds':
        seconds = time
    return str(seconds) + ' seconds'


print(seconds(5, 'weeks'))
print(seconds(4, 'days'))
print(seconds(3, 'hours'))
print(seconds(2, 'minutes'))
