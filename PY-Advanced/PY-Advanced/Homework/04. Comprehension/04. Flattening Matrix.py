number = int(input())
result = []

for i in range(number):
    current_list_of_numbers = input().split(", ")
    [result.append(int(number)) for number in current_list_of_numbers]

print(result)
