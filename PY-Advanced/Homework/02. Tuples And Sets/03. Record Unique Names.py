number_of_names = int(input())
unique_names_list = []

for _ in range(number_of_names):
    name = input()
    unique_names_list.append(name)

print('\n' .join(set(unique_names_list)))
