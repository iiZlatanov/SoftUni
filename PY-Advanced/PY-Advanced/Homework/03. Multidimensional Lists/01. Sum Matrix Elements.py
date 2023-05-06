data = [int(x) for x in input().split(", ")]
result = []
sum_of_nums = 0

for x in range(data[0]):
    columns_data = [int(x) for x in input().split(", ")]
    for el in columns_data:
        sum_of_nums += el
    result.append(columns_data)

print(sum_of_nums)
print(result)
