year = int(input("Year:"))
month = int(input("Month (1-12):"))

if month == 1:
    monthName = 'January'
    days = 31
if month == 2:
    monthName = 'Feburary'
    if year % 4 == 0:
        days = 29
    else:
        days = 28
if month == 3:
    monthName = 'March'
    days = 31
if month == 4:
    monthName = 'April'
    days = 30
if month == 5:
    monthName = 'May'
    days = 31
if month == 6:
    monthName = 'June'
    days = 30
if month == 7:
    monthName = 'July'
    days = 31
if month == 8:
    monthName = 'August'
    days = 31
if month == 9:
    monthName = 'September'
    days = 30
if month == 10:
    monthName = 'October'
    days = 31
if month == 11:
    monthName = 'November'
    days = 30
if month == 12:
    monthName = 'December'
    days = 31


print('Year:', year)
print('Month:', monthName)
print(days, 'days in that month')