number_of_people_waiting = int(input())
lift = list(map(int, input().split()))
current_lift_index = 0

for wagon in lift:
    if number_of_people_waiting == 0:
        break
    while wagon < 4:
        if number_of_people_waiting == 0:
            break
        lift[current_lift_index] += 1
        wagon += 1
        number_of_people_waiting -= 1
        if wagon == 4:
            current_lift_index += 1


all_seats = len(lift) * 4
taken_seats = sum(lift)

if number_of_people_waiting == 0 and taken_seats < all_seats:
    print("The lift has empty spots!")
elif number_of_people_waiting > 0 and taken_seats == all_seats:
    print(f"There isn't enough space! {number_of_people_waiting} people in a queue!")

print(' '.join(list(map(str, lift))))