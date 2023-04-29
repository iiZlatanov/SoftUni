employees = [
     int(input()),
     int(input()),
     int(input())
]

sum_of_possible_clients_per_hour = sum(employees)
people_count = int(input())
hours_needed_count = 0
counter = 0

while people_count > 0:
    people_count -= sum_of_possible_clients_per_hour
    counter += 1
    if counter == 4:
        counter = 0
        people_count += sum_of_possible_clients_per_hour
    hours_needed_count += 1

print(f"Time needed: {hours_needed_count}h.")
