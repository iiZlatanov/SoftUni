operator, first_num, second_num = input(), int(input()), int(input())


def calculations(parameter_one: int, parameter_two: int):
    result = None
    if operator == "multiply":
        result = parameter_one * parameter_two
    elif operator == "divide":
        result = int(parameter_one / parameter_two)
    elif operator == "add":
        result = parameter_one + parameter_two
    elif operator == "subtract":
        result = parameter_one - parameter_two

    return result


print(calculations(first_num, second_num))
