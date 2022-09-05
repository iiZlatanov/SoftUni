def check_if_numbers(list_data: list):
    for number in list_data:
        if isinstance(number, int) is False and isinstance(number, float) is False:
            return False
    return True


def numbers_rounding(list_of_numbers: list):
    result = [round(float(number)) for number in list_of_numbers]
    return result
    # if check_if_numbers(list_of_numbers) is True:
    #     result = [round(float(number)) for number in list_of_numbers]
    #     return result


data = input().split(" ")
print(numbers_rounding(data))
