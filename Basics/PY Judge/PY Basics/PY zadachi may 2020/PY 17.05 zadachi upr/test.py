exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

very_late = (arrival_time - exam_time) // 60
very_late_in_minutes = (arrival_time - exam_time) % 60

print(very_late)
print(f'{very_late_in_minutes:.2d}')
