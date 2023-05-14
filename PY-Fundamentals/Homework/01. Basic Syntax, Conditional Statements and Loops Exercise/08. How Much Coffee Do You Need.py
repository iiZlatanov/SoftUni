command = input()
number_of_coffees_needed = 0
events_for_1 = ["cat", "dog", "coding", "movie"]
events_for_2 = ["CAT", "DOG", "CODING", "MOVIE"]

while command != "END":
    if command in events_for_1:
        number_of_coffees_needed += 1
    elif command in events_for_2:
        number_of_coffees_needed += 2

    command = input()

if number_of_coffees_needed > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees_needed)
