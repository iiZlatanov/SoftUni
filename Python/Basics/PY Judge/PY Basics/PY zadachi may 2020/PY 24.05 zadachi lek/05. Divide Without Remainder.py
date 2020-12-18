n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, n+1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

first_percent = p1 / n * 100
second_percent = p2 / n * 100
third_percent = p3 / n * 100

print(f'{first_percent:.2f}%')
print(f'{second_percent:.2f}%')
print(f'{third_percent:.2f}%')