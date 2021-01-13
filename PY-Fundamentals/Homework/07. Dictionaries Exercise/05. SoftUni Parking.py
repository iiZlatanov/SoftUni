number_of_commands = int(input())
registered = {}

for i in range(number_of_commands):
    data = input().split()
    if len(data) == 3:
        name = data[1]
        license_plate = data[2]
        if data[1] not in registered:
            registered[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[name]}")
    else:
        name = data[1]
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registered.pop(name)

for key, value in registered.items():
    print(f"{key} => {value}")
