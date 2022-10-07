def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())
commands = input_to_list(n)

# commands = [
#     "IN, CA2844AA",
#     "IN, CA1234TA",
#     "OUT, CA2844AA",
#     "IN, CA9999TT",
#     "IN, CA2866HI",
#     "OUT, CA1234TA",
#     "IN, CA2844AA",
#     "OUT, CA2866HI",
#     "IN, CA9876HH",
#     "IN, CA2822UU",
# ]

# commands = [
#     "IN, CA2844AA",
#     "IN, CA1234TA",
#     "OUT, CA2844AA",
#     "OUT, CA1234TA",
# ]
parking_lot = set()

for line in commands:
    in_or_out, car_plate = line.split(", ")
    if in_or_out == "IN":
        parking_lot.add(car_plate)
    elif in_or_out == "OUT":
        parking_lot.remove(car_plate)

if parking_lot:
    print(f"\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
