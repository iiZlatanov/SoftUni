# data = input().split()
# unique_numbers = []
#
# for el in data:
#     if el not in unique_numbers:
#         unique_numbers.append(el)
#
# for number in unique_numbers:
#     print(f"{float(number)} - {data.count(number)} times")

values = tuple(map(float, input().split()))
counter = {value: values.count(value) for value in values}

for k, v in counter.items():
    print(f"{k} - {v} times")
