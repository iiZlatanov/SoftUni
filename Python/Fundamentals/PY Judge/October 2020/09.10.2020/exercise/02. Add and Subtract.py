def add_and_subtract(x, y, z):
    def sum_numbers(k, j):
        result_of_addition = k + j
        return result_of_addition

    result = sum_numbers(x, y)

    def subtract(g):
        result_of_subtraction = result - g
        return result_of_subtraction

    end_result = subtract(z)
    return end_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(first_number + second_number - third_number)