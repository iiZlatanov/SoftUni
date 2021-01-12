data = input()
sides_and_names = {}
flag = True
list_with_names = []
while data != "Lumpawaroo":
    data = data.split()
    if data[1] == "|":
        force_side = data[0]
        force_user = data[2]
        if force_side not in sides_and_names and force_user not in list_with_names:
            sides_and_names[force_side] = [force_user]
        elif force_side not in sides_and_names:
            sides_and_names[force_side] = []
        list_with_names.append(data[2])
    else:
        pass
    data = input()

print(sides_and_names)

# Light | Gosho
# Light | Pesho
# whatever | Pesho
# Dark | Pesho
# Light | Pesho
# Light | Gosho
# Dark | Pesho
# Light | Pesho
# Lumpawaroo
