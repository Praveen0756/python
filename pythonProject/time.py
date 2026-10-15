# Date & Time

import datetime

date = datetime.date(2026, 1, 10)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%D %Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 10, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("target date has not passed")