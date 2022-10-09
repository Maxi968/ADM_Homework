import calendar

month, day, year = tuple(map(int, input().split(" ")))

print(calendar.day_name[calendar.weekday(year, month, day)].upper())
