command = input()
students_results = {}
language_submissions = {}

while command != "exam finished":
    data = command.split("-")
    if len(data) == 3:
        student = data[0]
        language = data[1]
        points = int(data[2])
        if student not in students_results:
            students_results[student] = points
        else:
            if points > students_results[student]:
                students_results[student] = points
        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1
    else:
        students_results.pop(student)
    command = input()

ordered_participants = dict(sorted(students_results.items(), key=lambda x: (-x[1],x[0])))
print("Results:")
for key, value in ordered_participants.items():
    print(f"{key} | {value}")

ordered_language_submissions = dict(sorted(language_submissions.items(), key=lambda x: (-x[1],x[0])))
print("Submissions:")
for keys,values in ordered_language_submissions.items():
    print(f"{keys} - {values}")
