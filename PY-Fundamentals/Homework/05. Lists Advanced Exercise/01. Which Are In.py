substrings = input().split(", ")
words = input().split(", ")

result_with_duplicates = [subst for subst in substrings for word in words if subst in word]
result = []
[result.append(x) for x in result_with_duplicates if x not in result]

print(result)





# substrings = input().split(", ")
# words = input().split(", ")
#
# result = []
#
# for subst in substrings:
#     for word in words:
#         if subst in word and subst not in result:
#                 result.append(subst)
#
# print(result)





# substrings = input().split(", ")
# words = input().split(", ")
#
# list_with_duplicates = []
# result = []
#
# for subst in substrings:
#     for word in words:
#         if subst in word:
#             list_with_duplicates.append(subst)
#
# [result.append(x) for x in list_with_duplicates if x not in result]
# print(result)
