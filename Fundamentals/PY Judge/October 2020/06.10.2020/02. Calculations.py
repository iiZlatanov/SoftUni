operator = input()
number_1 = int(input())
number_2 = int(input())


def calculations(first_number, second_number):
    if operator == "multiply":
        return first_number * second_number
    elif operator == "divide":
        return int(first_number / second_number)
    elif operator == "add":
        return first_number + second_number
    elif operator == "subtract":
        return first_number - second_number


print(calculations(number_1, number_2))