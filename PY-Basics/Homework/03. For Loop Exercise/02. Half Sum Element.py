import sys

n = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    number = int(input())
    total_sum += number
    if number > max_number:
        max_number = number

other_sum = total_sum - max_number
if max_number == other_sum:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - other_sum)}')
