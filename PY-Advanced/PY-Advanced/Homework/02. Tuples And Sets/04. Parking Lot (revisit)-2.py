number_of_commands = int(input())
cars_in_parking = []

for _ in range(number_of_commands):
    data = input().split(", ")
    if data[0] == "IN":
        cars_in_parking.append(data[1])
    else:
        cars_in_parking.remove(data[1])

if len(cars_in_parking) == 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(set(cars_in_parking)))
