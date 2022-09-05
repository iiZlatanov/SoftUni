from collections import deque

data = []

for _ in range(int(input())):
    data += input().split()

data = [int(el) for el in data]
work_data = deque(data.copy())
current_petrol = data[0]
distance_to_next_station = data[1]
station_with_lowest_index_that_we_can_start_from = 0

while True:
    if distance_to_next_station > current_petrol:
        a = data.pop(0)
        b = data.pop(0)
        data.append(a)
        data.append(b)
        current_petrol = data[0]
        distance_to_next_station = data[1]
        work_data = deque(data.copy())
        station_with_lowest_index_that_we_can_start_from += 1
    else:
        work_data.popleft()
        work_data.popleft()
        if len(work_data) == 0:
            print(station_with_lowest_index_that_we_can_start_from)
            break
        current_petrol += work_data[0]
        current_petrol -= work_data[1]
