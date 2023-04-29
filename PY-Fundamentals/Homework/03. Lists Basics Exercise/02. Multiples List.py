factor = int(input())
count = int(input())

result_list = []
saved_factor = factor

for i in range(count):
    result_list.append(factor)
    factor += saved_factor

print(result_list)