command = input()
courses_and_participants = {}
courses_lengths = {}

while command != "end":
    data = command.split(" : ")
    course = data[0]
    student = data[1]
    if course not in courses_and_participants:
        courses_lengths[course] = 1
        courses_and_participants[course] = [student]
    else:
        courses_lengths[course] += 1
        courses_and_participants[course].append(student)
    command = input()

ordered_courses_and_participants = dict(sorted(courses_and_participants.values(), key=lambda x: x(len)))
print(ordered_courses_and_participants)
