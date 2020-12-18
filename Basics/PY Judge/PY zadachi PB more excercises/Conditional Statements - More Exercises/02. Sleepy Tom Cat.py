rest_days = int(input())

work_days = 365 - rest_days

work_days_play = work_days * 63
rest_days_play = rest_days * 127

total_play_in_minutes = work_days_play + rest_days_play

if total_play_in_minutes > 30000:
    print('Tom will run away')
    overplay = total_play_in_minutes - 30000
    print(f'{overplay // 60} hours and {overplay % 60} minutes more for play')
elif total_play_in_minutes < 30000:
    print('Tom sleeps well')
    underplay = 30000 - total_play_in_minutes
    print(f'{underplay // 60} hours and {underplay % 60} minutes less for play')