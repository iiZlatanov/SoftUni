divisor = int(input())
bound = int(input())

# резултата 1 трябва да се дели на divisor-а 2 трябва да е по-малко или равно (<=) на bound-а 3 трябва да е по-голямо от 0

for i in range(bound, 0, -1):
    if i % divisor == 0:
        print(i)
        break
