import math
number_of_days = int(input())
food_in_kgs_she_is_gonna_leave = int(input())
food_the_dog_needs_per_day_in_kgs = float(input())
food_the_cat_needs_per_day_in_kgs = float(input())
food_the_turtle_needs_per_day_in_gs = float(input())

food_the_turtle_needs_per_day_in_kgs = food_the_turtle_needs_per_day_in_gs / 1000

dog_enough = number_of_days * food_the_dog_needs_per_day_in_kgs
cat_enough = number_of_days * food_the_cat_needs_per_day_in_kgs
turtle_enough = number_of_days * food_the_turtle_needs_per_day_in_kgs

total = dog_enough + cat_enough + turtle_enough

if total <= food_in_kgs_she_is_gonna_leave:
    print(f'{math.floor(food_in_kgs_she_is_gonna_leave - total)} kilos of food left.')
elif total > food_in_kgs_she_is_gonna_leave:
    print(f'{math.ceil(total - food_in_kgs_she_is_gonna_leave)} more kilos of food are needed.')

