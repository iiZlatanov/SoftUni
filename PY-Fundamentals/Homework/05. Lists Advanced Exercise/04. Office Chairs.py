number_of_rooms = int(input())
flag = True
number_of_free_chairs = 0

for room in range(1, number_of_rooms + 1):
    info = input().split()
    number_of_people = int(info[1])
    if len(info[0]) < number_of_people:
        print(f"{number_of_people - len(info[0])} more chairs needed in room {room}")
        flag = False
    elif len(info[0]) > number_of_people:
        number_of_free_chairs += len(info[0]) - number_of_people

if flag is True:
    print(f"Game On, {number_of_free_chairs} free chairs left")
