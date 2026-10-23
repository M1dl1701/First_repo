import datetime

now = datetime.datetime.today()
date = datetime.datetime(year=2020, month=10, day=9)
diff = now - date
print(diff.days)
