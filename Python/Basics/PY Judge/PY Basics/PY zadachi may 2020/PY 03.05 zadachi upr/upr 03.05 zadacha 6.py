# days_the_charity_will_run = int(input())
# number_of_confectioners = int(input())
# number_of_cakes = int(input())
# number_of_waffles = int(input())
# number_of_pancakes = int(input())
#
# cakes = 45.0
# waffles = 5.80
# pancakes = 3.20
#
# number_of_cakes_per_confectioner_per_day = number_of_confectioners * number_of_cakes * cakes
# number_of_waffles_per_confectioner_per_day = number_of_confectioners * number_of_waffles * waffles
# number_of_pancakes_per_confectioner_per_day = number_of_confectioners * number_of_pancakes * pancakes
#
# cakes_multiplied_by_days = number_of_cakes_per_confectioner_per_day * days_the_charity_will_run
# waffles_multiplied_by_days = number_of_waffles_per_confectioner_per_day * days_the_charity_will_run
# pancakes_multiplied_by_days = number_of_pancakes_per_confectioner_per_day * days_the_charity_will_run
#
# total = cakes_multiplied_by_days + waffles_multiplied_by_days + pancakes_multiplied_by_days - ((cakes_multiplied_by_days + waffles_multiplied_by_days + pancakes_multiplied_by_days) / 8)
# print(total)

days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_price = 45
waffles_price = 5.80
pancakes_price = 3.20

money_per_day = ((cakes_count * cakes_price) + (waffles_price * waffles_count) + (pancakes_count * pancakes_price)) * bakers_count

income = money_per_day * days_count
profit = income - (income / 8)
print(profit)
