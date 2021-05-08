def sum_of_all_even_and_odd_digits(given_number: str):
    odd_and_even_numbers = [
        [],
        []
    ]
    for element in given_number:
        if int(element) % 2 != 0:
            odd_and_even_numbers[0].append(int(element))
        else:
            odd_and_even_numbers[1].append(int(element))
    odd_sum = sum(odd_and_even_numbers[0])
    even_sum = sum(odd_and_even_numbers[1])
    return odd_sum, even_sum


a, b = sum_of_all_even_and_odd_digits(str(input()))
print(f"Odd sum = {a}, Even sum = {b}")

#Without function exercise
#
# odd_and_even_numbers = [
#     [],
#     []
# ]
# for element in str(input()):
#     if int(element) % 2 != 0:
#         odd_and_even_numbers[0].append(int(element))
#     else:
#         odd_and_even_numbers[1].append(int(element))
# odd_sum = sum(odd_and_even_numbers[0])
# even_sum = sum(odd_and_even_numbers[1])
#
# print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")