def return_the_smallest_number(x, y, z):
    just_a_list = []
    just_a_list.append(x)
    just_a_list.append(y)
    just_a_list.append(z)
    return min(just_a_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(return_the_smallest_number(first_number, second_number, third_number))