import datetime
import time

start = time.time()
following_date = datetime.datetime.today()
sunday_count = 0
start_date = datetime.datetime(1901, 1, 1)
end_date = datetime.datetime(2000, 12, 31)
diff = abs(end_date - start_date)

while start_date != end_date:
    if start_date.weekday() == 6 and start_date.day == 1:
        sunday_count += 1
        start_date = start_date + datetime.timedelta(days=7)
    else:
        start_date = start_date + datetime.timedelta(days=1)

print(sunday_count)
print("Process took", time.time() - start, "sec")