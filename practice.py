import datetime
from datetime import time

h = datetime.datetime.now()
hour = h.time()
print(hour.hour)
print(hour)

today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=31)
print(lastMonth.strftime("%Y-%m-%d"))