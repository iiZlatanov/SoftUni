data = input()
vowels_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
print(''.join([element for element in data if element not in vowels_list]))
