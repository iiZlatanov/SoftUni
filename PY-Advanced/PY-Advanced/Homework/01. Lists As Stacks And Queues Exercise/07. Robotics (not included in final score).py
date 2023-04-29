from datetime import datetime, timedelta

ROBOTS_DATA = input().split(";")

for _ in ROBOTS_DATA:
    pass
time = datetime.strptime(input(), "%H:%M:%S")
time = time + timedelta(seconds=1)

