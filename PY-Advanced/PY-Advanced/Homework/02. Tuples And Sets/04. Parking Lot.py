number_of_inputs = int(input())
cars_in_parking_lot = []

for _ in range(number_of_inputs):
    data = input().split(", ")
    in_or_out = data[0]
    car_number_plate = data[1]
    if in_or_out == "IN" and car_number_plate not in cars_in_parking_lot:
        cars_in_parking_lot.append(car_number_plate)
    elif in_or_out == "OUT":
        cars_in_parking_lot.remove(car_number_plate)

if len(cars_in_parking_lot) > 0:
    print("\n".join(cars_in_parking_lot))
else:
    print("Parking Lot is Empty")
