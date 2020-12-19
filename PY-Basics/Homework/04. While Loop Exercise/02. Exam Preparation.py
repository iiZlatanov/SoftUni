number_of_bad_grades_required_to_bust = int(input())
bad_grades = 0
average_grade = 0
grade_number = 0
name_of_last_exercise = 0

while True:
    name_of_exercise = input()
    if name_of_exercise == 'Enough':
        print(f'Average score: {(average_grade / grade_number):.2f}')
        print(f'Number of problems: {grade_number}')
        print(f'Last problem: {name_of_last_exercise}')
        break
    grade = int(input())
    average_grade += grade
    grade_number += 1
    if grade <= 4:
        bad_grades += 1
    if bad_grades >= number_of_bad_grades_required_to_bust:
        print(f'You need a break, {bad_grades} poor grades.')
        break
    name_of_last_exercise = name_of_exercise