list_of_words = input().split()
searched_palindrome = input()
palindrome_list = [el for el in list_of_words if el == el[::-1]]
searched_palindrome_count = palindrome_list.count(searched_palindrome)

print(palindrome_list)
print(f"Found palindrome {searched_palindrome_count} times")

# Solution without list comprehension
#
# list_of_words = input().split()
# searched_palindrome = input()
# palindromes_list = []
# searched_palindrome_count = 0
#
# for el in list_of_words:
#     palindrome_check = el[::-1]
#     if palindrome_check == el:
#         palindromes_list.append(palindrome_check)
#     if palindrome_check == searched_palindrome:
#         searched_palindrome_count += 1
#
# print(palindromes_list)
# print(f"Found palindrome {searched_palindrome_count} times")
