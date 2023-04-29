number_of_iterations = int(input())
students = {}

for _ in range(number_of_iterations):
    data = tuple(input().split())
    student_name = data[0]
    student_grade = float(data[1])
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student, grade in students.items():
    grades_string = ' '.join(map(lambda grads: f"{grads:.2f}", grade))
    average_grade = sum(grade) / len(grade)
    print(f"{student} -> {grades_string} (avg: {average_grade:.2f})")
