def students_credits(*args):
    total_credits = 0
    won_credits_by_course = {}
    for arg in args:
        data = arg.split("-")
        course_name = data[0]
        credits_amount = int(data[1])
        max_test_points = int(data[2])
        diyans_points = int(data[3])

        diyans_credits = (diyans_points / max_test_points) * credits_amount
        total_credits += diyans_credits

        if course_name not in won_credits_by_course:
            won_credits_by_course[course_name] = diyans_credits

    result_string = ""
    if 240 <= total_credits:
        result_string += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result_string += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"
    for course, credit in sorted(won_credits_by_course.items(), key=lambda x: -x[1]):
        result_string += f"{course} - {credit:.1f}\n"

    return result_string

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
