#for problem 7 Robotics

from collections import deque
from datetime import datetime, timedelta

robots_and_their_processing_time = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
time = time + timedelta(seconds=3)
product = input()
products_list = deque()

while not product == "End":
    products_list.append(product)
    product = input()

while len(products_list) > 0:
    pass