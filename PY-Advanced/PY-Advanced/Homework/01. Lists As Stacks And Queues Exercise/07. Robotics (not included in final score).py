from datetime import datetime, timedelta
from collections import deque

robots = {data.split("-")[0]: [int(data.split("-")[1]), 0] for data in input().split(";")}
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    data = input()
    if data == "End":
        break
    else:
        products.append(data)

while products:
    factory_time += timedelta(0, 1)#the 0 is for days, the 1 is for seconds
