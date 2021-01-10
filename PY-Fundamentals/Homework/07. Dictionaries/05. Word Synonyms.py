number = int(input())
words_dict = {}

for _ in range(number):
    key = input()
    value = input()
    if key not in words_dict:
        words_dict[key] = []
        words_dict[key].append(value)
    else:
        words_dict[key].append(value)

for key, value in words_dict.items():
    print(f"{key} - {', '.join(value)}")

# Another way
# number = int(input())
# my_dict = {}
# my_list = []
# for _ in range(number * 2):
#     words = input()
#     my_list.append(words)
#
# while len(my_list) > 0:
#     first_word = my_list[0]
#     my_list.pop(0)
#     second_word = my_list[0]
#     my_list.pop(0)
#     if first_word not in my_dict:
#         my_dict[first_word] = second_word
#     else:
#         my_dict[first_word] += ", " + second_word
#
# for key,value in my_dict.items():
#     print(f"{key} - {value}")
