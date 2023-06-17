def gather_credits(credits_needed, *args):
    my_credits = 0
    enrolled_already = []

    for pair in args:
        course_name = pair[0]
        course_credits = pair[1]
        if my_credits >= credits_needed:
            break
        if course_name in enrolled_already:
            continue
        else:
            enrolled_already.append(course_name)
            my_credits += course_credits

    if my_credits >= credits_needed:
        result = f"Enrollment finished! Maximum credits: {my_credits}.\nCourses: {', '.join(sorted(enrolled_already))}"
        return result

    result = f"You need to enroll in more courses! You have to gather {credits_needed - my_credits} credits more."
    return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print("---------------")
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print("---------------")
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
