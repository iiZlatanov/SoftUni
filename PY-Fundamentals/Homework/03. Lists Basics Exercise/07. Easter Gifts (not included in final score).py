gifts_list = input().split()

while True:
    to_do = input()
    list_variant_of_to_do = to_do.split()
    if to_do == "No Money":
        break

    if len(list_variant_of_to_do) == 2:
        command, gift = to_do.split()
        if command == "OutOfStock":
            for element in gifts_list:
                if element == gift:
                    gifts_list.remove(element)
        elif command == "JustInCase":
            gifts_list[-1] = gift
    elif len(list_variant_of_to_do) == 3:
        command, gift, index = to_do.split()
        index = int(index)
        gifts_list[index] = gift

print(gifts_list)