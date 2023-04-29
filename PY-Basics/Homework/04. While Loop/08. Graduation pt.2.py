# name_of_student = input()
# grade_count = 0
# grade_sum = 0
# grade_average = 0
#
# while True:
#     grade = float(input())
#     grade_count += 1
#     if grade < 4:
#         grade_count -= 1
#         while True:
#             second_chance = float(input())
#             grade_count += 1
#             if second_chance < 4:
#                 print(f'{name_of_student} has been excluded at {grade_count} grade')
#                 break
#             grade_sum += grade
#             grade_average = grade_sum / grade_count
#             if grade_count >= 12:
#                 print(f'{name_of_student} graduated. Average grade: {grade_average:.2f}')
#                 break
#     grade_sum += grade
#     grade_average = grade_sum / grade_count
#     if grade_count >= 12:
#         print(f'{name_of_student} graduated. Average grade: {grade_average:.2f}')
#         break

name_of_student = input()
bad_grades = 0
grade_count = 0
grade_total = 0

for i in range(12):
    grade = float(input())
    if grade < 4:
        bad_grades += 1
    if bad_grades > 1:
        print(f'{name_of_student} has been excluded at {grade_count} grade')
        break
    grade_count += 1
    grade_total += grade
    if grade_count == 12:
        grade_average = grade_total / grade_count
        print(f'{name_of_student} graduated. Average grade: {grade_average:.2f}')
