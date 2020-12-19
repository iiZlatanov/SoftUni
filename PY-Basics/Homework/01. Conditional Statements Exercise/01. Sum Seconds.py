import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

combined_time = time_first + time_second + time_third

whole_number_division = combined_time // 60
module_division = combined_time % 60

if module_division < 10:
    print(f'{whole_number_division}:0{module_division}')
else:
    print(f'{whole_number_division}:{module_division}')