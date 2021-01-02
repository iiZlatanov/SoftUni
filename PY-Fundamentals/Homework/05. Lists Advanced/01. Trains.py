number_of_wagons = int(input())
command = input()

wagons_list = [0 for _ in range(number_of_wagons)]

while command != 'End':
    data = command.split()

    if data[0] == 'add':
        number_of_people = int(data[1])
        wagons_list[-1] += number_of_people
    elif data[0] == 'insert':
        number_of_people = int(data[2])
        wagon_number = int(data[1])
        wagons_list[wagon_number] += number_of_people
    elif data[0] == 'leave':
        number_of_people = int(data[2])
        wagon_number = int(data[1])
        wagons_list[wagon_number] -= number_of_people

    command = input()

print(wagons_list)
