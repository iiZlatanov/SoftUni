number_of_electrons = int(input())
shells_list = []
shell_number = 1

while number_of_electrons != 0:
    variable = 2 * shell_number ** 2
    if number_of_electrons < variable:
        shells_list.append(number_of_electrons)
        break
    shells_list.append(variable)
    number_of_electrons -= variable
    shell_number += 1

print(shells_list)
