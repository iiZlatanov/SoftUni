from copy import copy
from collections import deque

secondary_colors_waiting_list = []
result_colors = []
main_colors = ["red", "blue", "yellow"]
secondary_colors = ["orange", "purple", "green"]
strings_data = deque(input().split())


def are_secondary_color_conditions_met(check_color):
    if check_color == "orange":
        if ("red" in result_colors) and ("yellow" in result_colors):
            result_colors.append(check_color)
            secondary_colors_waiting_list.pop(check_color)
    elif check_color == "purple":
        if ("red" in result_colors) and ("blue" in result_colors):
            result_colors.append(check_color)
            secondary_colors_waiting_list.pop(check_color)
    elif check_color == "green":
        if ("yellow" in result_colors) and ("blue" in result_colors):
            result_colors.append(check_color)
            secondary_colors_waiting_list.pop(check_color)


while True:
    if len(strings_data) == 1: # Here is when there is only 1 string left to operate with
        if strings_data[0] in main_colors:
            result_colors.append(strings_data.pop())
        elif strings_data[0] in secondary_colors:
            secondary_colors_waiting_list.append(strings_data.pop())
        else:
            trimmed_string = strings_data.pop()[:-1]
            if trimmed_string:
                strings_data.append(trimmed_string)

    elif len(strings_data) > 1:# Here is when there are at least 2 strings to operate with
        first_string = strings_data.popleft()
        last_string = strings_data.pop()
        if first_string + last_string in main_colors:
            result_colors.append(first_string + last_string)
        elif first_string + last_string in secondary_colors:
            secondary_colors_waiting_list.append(first_string + last_string)
        else:
            trimmed_first_string = first_string[:-1]
            if trimmed_first_string:
                strings_data.insert(len(strings_data) // 2, trimmed_first_string)
            trimmed_last_string = last_string[:-1]
            if trimmed_last_string:
                strings_data.insert(len(strings_data) // 2, trimmed_last_string)

    else:                       # Here we have the break condition, which is met when we have no strings left
        break

    if secondary_colors_waiting_list:
        for color in copy(secondary_colors_waiting_list):
            are_secondary_color_conditions_met(color)


print(result_colors)
