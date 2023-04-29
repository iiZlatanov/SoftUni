list_of_numbers = input().split()
remove_count = int(input())
list_in_integers = []

for elements in list_of_numbers:
    list_in_integers.append(int(elements))

for element in range(remove_count):
    list_in_integers.remove(min(list_in_integers))

print(list_in_integers)