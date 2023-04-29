number_of_pairs = int(input())
students_and_their_grades_dict = {}

for i in range(number_of_pairs):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_and_their_grades_dict:
        students_and_their_grades_dict[student_name] = student_grade
    else:
        students_and_their_grades_dict[student_name] += student_grade
        students_and_their_grades_dict[student_name] /= 2

for n in range(len(students_and_their_grades_dict)):
    for key, value in students_and_their_grades_dict.items():
        if value < 4.50:
            students_and_their_grades_dict.pop(key)
            break

sorted_dict = dict(sorted(students_and_their_grades_dict.items(), key=lambda x: x[1], reverse=True))

for name,grade in sorted_dict.items():
    print(f"{name} -> {grade:.2f}")
