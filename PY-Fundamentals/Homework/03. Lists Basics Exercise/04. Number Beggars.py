list_of_numbers = input().split(", ")
number_of_beggars = int(input())

if number_of_beggars == len(list_of_numbers):
    list_duplicate = []
    for k in list_of_numbers:
        list_duplicate.append(int(k))
    print(list_duplicate)
elif number_of_beggars > len(list_of_numbers):
    new_list = []
    calculations = number_of_beggars - len(list_of_numbers)
    for element in list_of_numbers:
        new_list.append(int(element))
    for i in range(calculations):
        new_list.append(0)
    print(new_list)
else:
    count = 0
    beggar_list = []
    for number in range(number_of_beggars):
        beggar_list.append(0)
    for elements in list_of_numbers:
        elements = int(elements)
        beggar_list[count] += elements
        count += 1
        if count == number_of_beggars:
            count = 0
    print(beggar_list)