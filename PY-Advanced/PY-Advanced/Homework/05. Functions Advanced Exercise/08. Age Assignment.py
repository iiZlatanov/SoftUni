def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        result[name] = kwargs[name[0]]

    result = sorted(result.items(), key=lambda x: x[0])
    return "\n".join(f"{name} is {age} years old." for name, age in result)

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
