#•	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
#•	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
#•	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
#•	4ти ред: брой работници – цяло число в интервала [1 … 20]

import math
x = int(input())
y = float(input())
z = int(input())
number_of_workers = int(input())

kgs_of_grapes = x * y
kgs_used_for_wine = kgs_of_grapes * 0.4
one_liter_of_wine = kgs_used_for_wine / 2.5

if one_liter_of_wine < z:
    more_liters_required_to_meet_the_needs = z - one_liter_of_wine
    print(f'It will be a tough winter! More {math.floor(more_liters_required_to_meet_the_needs)} liters wine needed.')
elif one_liter_of_wine > z:
    print(f'Good harvest this year! Total wine: {math.floor(one_liter_of_wine)} liters.')
    wine_left_after_requirement_is_met = one_liter_of_wine - z
    wine_per_person = wine_left_after_requirement_is_met / number_of_workers
    print(f'{math.ceil(wine_left_after_requirement_is_met)} liters left -> {math.ceil(wine_per_person)} liters per person.')