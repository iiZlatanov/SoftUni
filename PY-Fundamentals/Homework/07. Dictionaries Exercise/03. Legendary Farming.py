key_materials = {"shards": [0, "Shadowmourne"], "fragments": [0, "Valanyr"], "motes": [0, "Dragonwrath"]}
junks = {}
REQUIRED_MATS_TO_CRAFT = 250
flag = True

while flag is True:
    data = input().split()
    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item in key_materials:
            key_materials[item][0] += quantity
        else:
            if item in junks:
                junks[item] += quantity
            else:
                junks[item] = quantity

        for key in key_materials:
            if key_materials[key][0] >= REQUIRED_MATS_TO_CRAFT:
                key_materials[key][0] -= REQUIRED_MATS_TO_CRAFT
                print(f"{key_materials[key][1]} obtained!")
                for element, number in key_materials.items():
                    key_materials[element] = number[0]

                sorted_dict = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
                for keys, values in sorted_dict.items():
                    print(f"{keys}: {values}")

                sorted_junk = sorted(junks.items(), key=lambda x: x[0])
                for junk_keys, junk_values in sorted_junk:
                    print(f"{junk_keys}: {junk_values}")

                flag = False
                break
        if flag is False:
            break
