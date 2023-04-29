guests_list = []
attendive_list = []
non_attendive_list = []

for _ in range(int(input())):
    reservation_number = input()
    guests_list.append(reservation_number)

command = input()
while command != "END":
    attendive_list.append(command)
    command = input()

for guest in guests_list:
    if guest not in attendive_list:
        non_attendive_list.append(guest)

non_attendive_list = sorted(non_attendive_list)

print(f"{len(guests_list) - len(attendive_list)}")
print("\n".join(non_attendive_list))
