data = input()
materials = {}

while data != "stop":
    quantity = int(input())
    if data not in materials:
        materials[data] = quantity
    else:
        materials[data] += quantity
    data = input()

for key, value in materials.items():
    print(f"{key} -> {value}")
