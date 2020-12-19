import sys

smallest = sys.maxsize
biggest = -sys.maxsize

number = int(input())

for i in range(0, number):
    numbers = int(input())
    if numbers < smallest:
        smallest = numbers
    if numbers > biggest:
        biggest = numbers

print(f'Max number: {biggest}')
print(f'Min number: {smallest}')