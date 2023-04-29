starting_population = int(input())
years = int(input())

for i in range(1, years+1):
    starting_pop_divided_by_ten = starting_population // 10
    starting_pop_divided_by_ten_times_two = starting_pop_divided_by_ten * 2
    starting_population += starting_pop_divided_by_ten_times_two
    if i % 5 == 0:
        five_of_every_fifty = starting_population // 50
        further_multiplication = five_of_every_fifty * 5
        starting_population -= further_multiplication
    starting_pop_divided_by_twenty = starting_population // 20
    starting_pop_divided_by_twenty_times_two = starting_pop_divided_by_twenty * 2
    starting_population -= starting_pop_divided_by_twenty_times_two

print(f'Beehive population: {starting_population}')