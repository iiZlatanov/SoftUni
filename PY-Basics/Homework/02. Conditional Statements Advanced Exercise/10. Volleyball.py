import math

year = input()
p = int(input())
h = int(input())

forty_eight_weekends = 48
play_while_in_sofia = (48 - h) * (3 / 4)
play_while_in_hometown = h
holidays_play = p * (2 / 3)

total_play_before_leap_or_normal = play_while_in_sofia + play_while_in_hometown + holidays_play

if year == 'normal':
    print(math.floor(total_play_before_leap_or_normal))
elif year == 'leap':
    total_play_before_leap_or_normal += total_play_before_leap_or_normal * 0.15
    print(math.floor(total_play_before_leap_or_normal))