import sys
n = int(input())

max_number_for_even = -sys.maxsize
max_number_for_odd = -sys.maxsize
min_number_for_even = sys.maxsize
min_number_for_odd = sys.maxsize

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    numbers = float(input())
    if i % 2 == 0:
        even_sum += numbers
        if numbers > max_number_for_even:
            max_number_for_even = numbers
        if numbers < min_number_for_even:
            min_number_for_even = numbers

    else:
        odd_sum += numbers
        if numbers > max_number_for_odd:
            max_number_for_odd = numbers
        if numbers < min_number_for_odd:
            min_number_for_odd = numbers

if n == 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif n == 1:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_number_for_odd:.2f},')
    print(f'OddMax={max_number_for_odd:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_number_for_odd:.2f},')
    print(f'OddMax={max_number_for_odd:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={min_number_for_even:.2f},')
    print(f'EvenMax={max_number_for_even:.2f}')
