number_of_wagons = int(input())

train = [0 for _ in range(number_of_wagons)]

command = input()

while command != 'End':
    commands_list = command.split()

    if commands_list[0] == 'add':
        number_of_people = int(commands_list[1])
        train[-1] += number_of_people
    elif commands_list[0] == 'insert':
        wagon_number = int(commands_list[1])
        number_of_people = int(commands_list[2])
        train[wagon_number] += number_of_people
    elif commands_list[0] == 'leave':
        wagon_number = int(commands_list[1])
        number_of_people = int(commands_list[2])
        train[wagon_number] -= number_of_people

    command = input()

print(train)