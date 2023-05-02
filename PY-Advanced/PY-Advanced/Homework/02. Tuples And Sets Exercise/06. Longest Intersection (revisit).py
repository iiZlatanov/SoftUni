number_of_intersections = int(input())
all_result_sets = []
longest_intersection = []

for _ in range(number_of_intersections):
    first_set = set()
    second_set = set()
    data = input().split("-")
    first_intersection, second_intersection = data[0].split(","), data[1].split(",")

    for number in range(int(first_intersection[0]), int(first_intersection[1]) + 1):
        first_set.add(number)
    for number in range(int(second_intersection[0]), int(second_intersection[1]) + 1):
        second_set.add(number)
    result_set = set(first_set.intersection(second_set))
    all_result_sets.append(result_set)

longest_intersection.append(all_result_sets[1])#appending the first set here so that the initial IF below can work
for set_number in all_result_sets:
    if len(longest_intersection[0]) < len(set_number):
        longest_intersection.pop()
        longest_intersection.append(list(set_number))

print(f"Longest intersection is "
      f"{', '.join(str(x) for x in list(longest_intersection))} "
      f"with length {len(longest_intersection[0])}")
