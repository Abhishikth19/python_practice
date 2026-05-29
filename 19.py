def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31
day = 0
for month in range(1, 13):
    day = (day + days_in_month(month, 1900)) % 7
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if day == 6: 
            count += 1
        day = (day + days_in_month(month, year)) % 7
print(count)