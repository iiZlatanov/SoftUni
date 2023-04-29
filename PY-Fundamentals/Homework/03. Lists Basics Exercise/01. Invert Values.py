single_string_in_numbers = str(input()).split()
opposites_list = []

for element in single_string_in_numbers:
    element = int(element)
    opposites_list.append(element * -1)

print(opposites_list)