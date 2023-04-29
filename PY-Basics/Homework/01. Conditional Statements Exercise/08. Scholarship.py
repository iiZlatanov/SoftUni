import math
income = float(input())
success_rate = float(input())
minimal_salary = float(input())

social_scholarship = 0
scholarship_for_excellent_result = 0

if success_rate >= 5.5:
    scholarship_for_excellent_result = success_rate * 25

if success_rate > 4.5 and income < minimal_salary:
    social_scholarship += minimal_salary * 0.35

if social_scholarship > scholarship_for_excellent_result:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif scholarship_for_excellent_result >= social_scholarship:
    if scholarship_for_excellent_result != 0:
        print(f'You get a scholarship for excellent results {math.floor(scholarship_for_excellent_result)} BGN')
    else:
        print('You cannot get a scholarship!')
