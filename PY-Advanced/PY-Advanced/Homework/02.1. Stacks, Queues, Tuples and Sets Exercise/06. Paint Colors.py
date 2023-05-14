# from collections import deque
# from math import floor
# data = deque(input().split())
#
# main_colors = ["red", "yellow", "blue"]
# secondary_colors = ["orange", "purple", "green"]
# result = []
# waiting_for_second_check = []
# required_colors = {
#     "orange": {"red", "yellow"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"}
# }
#
# while data:
#     first_word = data.popleft()
#     second_word = data.pop() if data else ""
#     if first_word + second_word in main_colors:
#         result.append(first_word + second_word)
#     elif second_word + first_word in main_colors:
#         result.append(second_word + first_word)
#     elif ((first_word + second_word in secondary_colors) or (second_word + first_word in secondary_colors)) and ((required_colors[first_word + second_word] in result) or (required_colors[second_word + first_word] in result):
#         result.append(first_word + second_word)
#     elif (first_word + second_word or second_word + first_word) in secondary_colors:
#         waiting_for_second_check.append(first_word + second_word)
#     else:
#         first_word = first_word[:-1]
#         second_word = second_word[:-1]
#         data.insert(floor(len(data) / 2), first_word)
#         data.insert(floor(len(data) / 2), second_word)
#     for el in waiting_for_second_check:
#         if required_colors[el] in result:
#             result.append(el)
#
# print(result)
