command = input()
participants = {}
courses_lengths = {}

while command != "end":
    data = command.split(" : ")
    course = data[0]
    student = data[1]
    if course not in courses_lengths:
        courses_lengths[course] = 1
    else:
        courses_lengths[course] += 1

    if course not in participants:
        participants[course] = [student]
    else:
        participants[course].append(student)

    command = input()

ordered_courses_lengths = dict(sorted(courses_lengths.items(), key=lambda x: -x[1]))
ordered_participants = {x: sorted(participants[x]) for x in participants.keys()}

for key, value in ordered_courses_lengths.items():
    print(f"{key}: {value}")
    for keys, values in ordered_participants.items():
        if keys == key:
            x = "\n-- ".join(values)
            print(f"-- {x}")
