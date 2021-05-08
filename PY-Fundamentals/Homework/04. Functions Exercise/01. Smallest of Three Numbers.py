first_integer, second_integer, third_integer = int(input()), int(input()), int(input())


def smallest_given_number(first_number: int or float, second_number: int or float, third_number: int or float):
    list_with_the_numbers = [first_number, second_number, third_number]
    result = min(list_with_the_numbers)
    return result


print(smallest_given_number(first_integer, second_integer, third_integer))
