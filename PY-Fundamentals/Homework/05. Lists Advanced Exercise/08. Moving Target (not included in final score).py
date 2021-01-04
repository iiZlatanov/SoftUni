numbers = input().split()
targets_values = [int(x) for x in numbers]
command_and_values = input().split()
values_list = [int(x) for x in command_and_values if len(x) <= 2]
command = command_and_values[0]

while command != "End":
    if command == "Shoot":
        index = values_list[0]
        power = values_list[1]
        if index <= (len(targets_values) - 1):
            targets_values[index] -= power
            if targets_values[index] <= 0:
                targets_values.pop(index)
    elif command == "Add":
        index = values_list[0]
        value = values_list[1]
        if index <= (len(targets_values) - 1):
            targets_values.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        index = values_list[0]
        radius = values_list[1]
        if (index + radius - 1) <= len(targets_values) and index >= radius:
            targets_values.pop(index)
            while radius != 0:
                targets_values.pop(index)
                targets_values.pop(index - 1)
                index -= 1
                radius -= 1
        else:
            print("Strike missed!")

    command_and_values = input().split()
    values_list = [int(x) for x in command_and_values if len(x) <= 2]
    command = command_and_values[0]

print("|".join(map(str, targets_values)))
