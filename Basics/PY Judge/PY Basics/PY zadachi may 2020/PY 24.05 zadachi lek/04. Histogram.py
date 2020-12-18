n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range (1, n+1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    elif 800 <= number:
        p5 += 1

percent_one = p1 / n * 100
percent_two = p2 / n * 100
percent_three = p3 / n * 100
percent_four = p4 / n * 100
percent_five = p5 / n * 100

print(f'{percent_one:.2f}%')
print(f'{percent_two:.2f}%')
print(f'{percent_three:.2f}%')
print(f'{percent_four:.2f}%')
print(f'{percent_five:.2f}%')
