number_of_names = int(input())
odd_numbers = []
even_numbers = []

for i in range(1, number_of_names + 1):
    current_name = input()
    ascii_value = 0
    for letter in current_name:
        ascii_value += ord(letter)
    result_number = ascii_value // i
    if result_number % 2 == 0:
        even_numbers.append(result_number)
    else:
        odd_numbers.append(result_number)

odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)

if odd_sum == even_sum:
    union_values = []
    for el in even_numbers:
        union_values.append(el)
    for el in odd_numbers:
        if el not in union_values:
            union_values.append(el)
    print(", ".join((map(str, union_values))))

elif odd_sum > even_sum:
    print(", ".join(map(str, odd_numbers)))

elif odd_sum < even_sum:
    symmetric_difference_values = []
    for el in even_numbers:
        if el not in odd_numbers:
            symmetric_difference_values.append(el)
    for el in odd_numbers:
        if el not in even_numbers and el not in symmetric_difference_values:
            symmetric_difference_values.append(el)
    print(", ".join(map(str, symmetric_difference_values)))
