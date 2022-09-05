number_of_intersections = int(input())
longest_intersection = 0
bigger_starting_number = 0
lower_finishing_number = 0
result = []
longest_intersection_point_a, longest_intersection_point_b = 0, 0

for _ in range(number_of_intersections):
    current_intersection = input().split("-")
    first, second = current_intersection
    road_a_start, road_a_finish = map(int, first.split(","))
    road_b_start, road_b_finish = map(int, second.split(","))

    if road_a_start > road_b_start:
        bigger_starting_number = road_a_start
    else:
        bigger_starting_number = road_b_start

    if road_a_finish < road_b_finish:
        lower_finishing_number = road_a_finish
    else:
        lower_finishing_number = road_b_finish

    if lower_finishing_number - bigger_starting_number > longest_intersection:
        longest_intersection_point_a, longest_intersection_point_b = bigger_starting_number, lower_finishing_number
        longest_intersection = lower_finishing_number - bigger_starting_number

for x in range(longest_intersection_point_a, longest_intersection_point_b + 1):
    result.append(x)

print(f"Longest intersection is {result} with length {len(result)}")
