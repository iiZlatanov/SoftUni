capacity = int(input())
users_dict = {}

while True:
    data = input()
    if data == "Statistics":
        print(f"Users count: {len(users_dict)}")
        for key, value in users_dict.items():
            print(f"{key} - {value}")
        break

    data = data.split("=")
    command = data[0]
    if command == "Add":
        if data[1] not in users_dict:
            users_dict[data[1]] = int(data[2]) + int(data[3])

    elif command == "Message":
        if data[1] in users_dict and data[2] in users_dict:
            users_dict[data[1]] += 1
            users_dict[data[2]] += 1

            if users_dict[data[1]] == capacity:
                print(f"{data[1]} reached the capacity!")
                del users_dict[data[1]]
            if users_dict[data[2]] == capacity:
                print(f"{data[2]} reached the capacity!")
                del users_dict[data[2]]

    elif command == "Empty":
        if data[1] == "All":
            users_dict = {}
        else:
            if data[1] in users_dict:
                del users_dict[data[1]]
