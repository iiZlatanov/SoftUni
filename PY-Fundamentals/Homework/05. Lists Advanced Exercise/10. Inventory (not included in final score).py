inventory = input().split(", ")
commands_and_values = input().split(" - ")
command = commands_and_values[0]

while command != "Craft!":

    if command == "Collect":
        if commands_and_values[1] not in inventory:
            inventory.append(commands_and_values[1])

    elif command == "Drop":
        for el in inventory:
            if el == commands_and_values[1]:
                inventory.remove(el)

    elif command == "Combine Items":
        items_list = commands_and_values[1].split(":")
        old_item = items_list[0]
        new_item = items_list[1]
        index = -1
        for el in inventory:
            index += 1
            if old_item == el:
                inventory.insert(index + 1, new_item)

    elif command == "Renew":
        for el in inventory:
            if el == commands_and_values[1]:
                inventory.remove(el)
                inventory.append(el)
    commands_and_values = input().split(" - ")
    command = commands_and_values[0]

print(", ".join(inventory))
