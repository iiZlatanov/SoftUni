clothes_data = [int(x) for x in input().split()]
RACK_CAPACITY = int(input())

needed_racks = 1
current_rack = RACK_CAPACITY

while len(clothes_data) != 0:
    if clothes_data[-1] < current_rack:
        current_rack -= clothes_data[-1]
        clothes_data.pop()
    elif clothes_data[-1] == current_rack:
        current_rack = RACK_CAPACITY
        clothes_data.pop()
        needed_racks += 1
    else:
        current_rack = RACK_CAPACITY
        needed_racks += 1

print(needed_racks)
