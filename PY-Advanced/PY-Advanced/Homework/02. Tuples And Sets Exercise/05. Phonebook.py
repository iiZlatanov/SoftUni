data = input()
contacts = {}

while len(data) > 3:
    split_data = data.split("-")
    name = split_data[0]
    number = split_data[1]
    if name not in contacts:
        contacts[name] = number
    else:
        contacts[name] = number
    data = input()

data = int(data)

for _ in range(data):
    searched_name = input()
    if searched_name in contacts:
        print(f"{searched_name} -> {contacts[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
