exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
late_or_early_or_on_time = 0

if exam_time < arrival_time and (arrival_time - exam_time) < 60:
    late_or_early_or_on_time = 'Late'
    print(late_or_early_or_on_time)
    print(f'{arrival_time - exam_time} minutes after the start')

elif exam_time < arrival_time and (arrival_time - exam_time) >= 60:
    late_or_early_or_on_time = 'Late'
    very_late = (arrival_time - exam_time) // 60
    very_late_in_minutes = (arrival_time - exam_time) % 60
    print(late_or_early_or_on_time)
    print(f'{very_late}:{very_late_in_minutes:02d} hours after the start')

elif exam_time == arrival_time:
    late_or_early_or_on_time = 'On time'
    print(late_or_early_or_on_time)

elif exam_time > arrival_time and (exam_time - arrival_time) <= 30:
    late_or_early_or_on_time = 'On time'
    print(late_or_early_or_on_time)
    print(f'{exam_time - arrival_time} minutes before the start')

elif exam_time > arrival_time and (exam_time - arrival_time) >= 60:
    late_or_early_or_on_time = 'Early'
    very_early = (exam_time - arrival_time) // 60
    very_early_in_minutes = (exam_time - arrival_time) % 60
    print(late_or_early_or_on_time)
    print(f'{very_early}:{very_early_in_minutes:02d} hours before the start')

elif exam_time > arrival_time and 30 < (exam_time - arrival_time) < 60:
    late_or_early_or_on_time = 'Early'
    earlier = exam_time - arrival_time
    print(late_or_early_or_on_time)
    print(f'{earlier} minutes before the start')