data = input().split()
my_dict = {}

for key in data:
    key = key.lower()
    if key not in my_dict:
        my_dict[key] = 1
    else:
        my_dict[key] += 1

for keys, values in my_dict.items():
    if not values % 2 == 0:
        print(keys, end=" ")
