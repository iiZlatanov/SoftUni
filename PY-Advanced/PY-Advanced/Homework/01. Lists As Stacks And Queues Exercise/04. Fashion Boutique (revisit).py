CLOTHES_PRICES = input().split()
RACK_CAPACITY = int(input())
current_rack = 0
rack_counter = 0

for clothing in CLOTHES_PRICES:
    current_cloth = int(clothing)
    current_rack += current_cloth

    if current_rack == RACK_CAPACITY:
        current_rack = 0
        rack_counter += 1
    elif current_rack > RACK_CAPACITY:
        current_rack = 0
        rack_counter += 1
        current_rack += current_cloth

if current_rack != 0:
    rack_counter += 1

print(rack_counter)
