data = input().split("|")
result = []

for sub_string in data[::-1]:
    result.extend(sub_string.split())
print(*result, end=" ")
