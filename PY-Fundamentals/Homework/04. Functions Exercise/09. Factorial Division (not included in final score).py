def factorial_of_a_number(number):
    factorial_of_current_number = number
    for i in range(number , 0, -1):
        if i == 1:
            i = 2
        factorial_of_current_number = (i-1) * factorial_of_current_number
    return factorial_of_current_number


number_1 = int(input())
number_2 = int(input())
result = factorial_of_a_number(number_1) / factorial_of_a_number(number_2)
print(f"{result:.2f}")