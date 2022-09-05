guests_list = []
guests_that_attended_the_party = []
non_attending_guest = []

for _ in range(int(input())):
    reservation_number = input()
    guests_list.append(reservation_number)

while True:
    data = input()
    if data == "END":
        break
    guests_that_attended_the_party.append(data)

for guest in guests_list:
    if guest not in guests_that_attended_the_party:
        non_attending_guest.append(guest)

non_attending_guest = sorted(non_attending_guest)
print(f"{len(guests_list) - len(guests_that_attended_the_party)}")
print("\n".join(non_attending_guest))
