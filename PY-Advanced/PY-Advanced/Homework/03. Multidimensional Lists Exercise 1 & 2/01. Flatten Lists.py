data = input().split("|")
result = []

for sub_string in data[::-1]:
    result.extend(sub_string.split())
print(*result)

# # With comprehension
# numbers = [string.split() for string in input().split("|")]
# print(*[" ".join(sublist) for sublist in numbers[::-1] if string])
