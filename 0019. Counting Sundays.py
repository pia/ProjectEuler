import datetime

start_time = datetime.datetime(1901, 1, 1)
end_time = datetime.datetime(2000, 12, 31)
interval = datetime.timedelta(days=1)
count = 0
while start_time < end_time:
    if start_time.day == 1 and start_time.isoweekday() == 7:
        count += 1
    start_time += interval

print(count)
