clothes_capacity = list(map(int, input().split(" ")))
RACK_CAPACITY = int(input())
rack_counter = 1
current_rack_capacity = 0

while len(clothes_capacity) != 0:
    if current_rack_capacity + clothes_capacity[-1] <= RACK_CAPACITY:
        current_rack_capacity += clothes_capacity.pop()
    else:
        current_rack_capacity = 0
        rack_counter += 1

print(rack_counter)
