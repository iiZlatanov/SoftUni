def add_and_subtract(first_number: int, second_number: int, third_number: int):
    def sum_numbers(a: int, b: int):
        sum_result = a + b
        return sum_result

    def subtract(result_from_summing: int, c: int):
        result = result_from_summing - c
        return result

    return subtract(sum_numbers(first_number, second_number), third_number)


first_integer, second_integer, third_integer = int(input()), int(input()), int(input())
print(add_and_subtract(first_integer, second_integer, third_integer))
