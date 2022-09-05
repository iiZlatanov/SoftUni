number = int(input())
unique_names = []

for _ in range(number):
    name = input()
    name_lower = name.lower()
    if name not in unique_names and name_lower not in unique_names:
        unique_names.append(name)

print("\n".join(unique_names))
# first_name, *other_names = unique_names
#
# print(first_name)
# print("\n".join(other_names))
