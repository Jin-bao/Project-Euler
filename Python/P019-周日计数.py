import datetime

theWeek = [1, 2, 3, 4, 5, 6, 7]
SunTotal = 0
for year in range(1901, 2001):
  for month in range(1, 13):
    if theWeek[datetime.date(year,month,1).weekday()] == 7:
      SunTotal += 1
print(SunTotal)