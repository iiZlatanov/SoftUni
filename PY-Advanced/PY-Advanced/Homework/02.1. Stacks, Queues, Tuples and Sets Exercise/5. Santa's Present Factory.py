from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
crafted_presents = []
result_presents = {}
flag = False

present_prices = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

while materials and magic_levels:
    box = materials[-1]
    while box == 0:
        materials.pop()
        box = materials[-1]
    magic = magic_levels[0]
    while magic == 0:
        magic_levels.popleft()
        if magic_levels:
            magic = magic_levels[0]
        else:
            flag = True
            break
    if flag is True:
        break
    result = box * magic

    if result in present_prices:
        materials.pop()
        magic_levels.popleft()
        crafted_presents.append(result)
    elif result < 0:
        result = box + magic
        materials.pop()
        magic_levels.popleft()
        materials.append(result)
    else:
        magic_levels.popleft()
        materials[-1] += 15

print("The presents are crafted! Merry Christmas!") \
    if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) else print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for el in crafted_presents:
    if el not in result_presents:
        result_presents[el] = 1
    else:
        result_presents[el] += 1
for toy, number in result_presents.items():
    print(f"{toy}: {number}")
