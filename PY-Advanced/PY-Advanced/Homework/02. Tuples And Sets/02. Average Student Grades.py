number_of_inputs = int(input())
students_records = {}

for _ in range(number_of_inputs):
    name_and_mark = input().split()
    student_name = name_and_mark[0]
    student_mark = float(name_and_mark[1])
    if student_name not in students_records:
        students_records[student_name] = []
    students_records[student_name].append(student_mark)

for name, grades in students_records.items():
    grades_list = grades
    print(f"{name} -> ", end="")
    for el in grades_list:
        element = float(el)
        print(f"{element:.2f} ", end="")
    print(f"(avg: {sum(grades_list) / len(grades_list):.2f})")
