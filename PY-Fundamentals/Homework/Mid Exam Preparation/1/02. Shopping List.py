groceries_list = input().split("!")

command = input()
index = 0

while command != "Go Shopping!":
    command_list = command.split(" ")
    if command_list[0] == "Urgent":
        if command_list[1] not in groceries_list:
            groceries_list.insert(0, command_list[1])

    elif command_list[0] == "Unnecessary":
        if command_list[1] in groceries_list:
            groceries_list.remove(command_list[1])

    elif command_list[0] == "Correct":
        for grocery in groceries_list:
            if grocery == command_list[1]:
                groceries_list.pop(index)
                groceries_list.insert(index, command_list[2])
            index += 1
        index = 0

    elif command_list[0] == "Rearrange":
        if command_list[1] in groceries_list:
            groceries_list.remove(command_list[1])
            groceries_list.append(command_list[1])

    command = input()

print(", ".join(groceries_list))
