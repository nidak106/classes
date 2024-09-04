import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
ti=lambda x:x.time()
print(f"year is: {year(now)}")
print(f"month is: {month(now)}")
print(f"day is: {day(now)}")
print(f"time is: {ti(now)}")