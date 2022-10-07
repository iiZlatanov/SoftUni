def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())
names = input_to_list(n)


# names = [
#     "Lee",
#     "Joey",
#     "Lee",
#     "Joe",
#     "Alan",
#     "Alan",
#     "Peter",
#     "Joey",
# ]

unique_names = set(names)
for name in unique_names:
    print(name)
