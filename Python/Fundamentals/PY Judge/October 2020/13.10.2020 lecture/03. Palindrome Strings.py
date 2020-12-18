list_of_words = input().split()
searched_palindrome = input()
palindrome_list = [el for el in list_of_words if el == el[::-1]]
searched_palindrome_count = palindrome_list.count(searched_palindrome)

print(palindrome_list)
print(f"Found palindrome {searched_palindrome_count} times")