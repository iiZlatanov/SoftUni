import math
hours_needed = int(input())
days = int(input())
overtime_employees = int(input())

actual_days = days - (days * 0.1)
actual_days_turned_into_hours = actual_days * 8
overtime_employees_hours = overtime_employees * 2 * days
work_hours = math.floor(overtime_employees_hours + actual_days_turned_into_hours)

if hours_needed <= work_hours:
    print(f'Yes!{math.floor(work_hours - hours_needed)} hours left.')
elif hours_needed > work_hours:
    print(f'Not enough time!{math.floor(hours_needed - work_hours)} hours needed.')