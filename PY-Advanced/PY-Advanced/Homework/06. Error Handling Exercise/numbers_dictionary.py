numbers_dictionary = {}

line = input()
while line != "Search":
    while line.isdigit():  # This while will ensure we do not get things like 2: 1 or 4: 5 or 5: 5 in the dict
        print("Please pass the number as a word instead of a digit.")
        line = input()
    number_as_string = line

    try:
        number_as_int = int(input())
        numbers_dictionary[number_as_string] = number_as_int
    except ValueError:
        print("The variable number must be an integer!")
        continue

    line = input()

line = input()
while line != "Remove":
    searched_number = line
    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary.")
    line = input()

line = input()
while line != "End":
    number_to_remove = line
    try:
        del numbers_dictionary[number_to_remove]
    except KeyError:
        print("Number cannot be deleted since it does not exist in dictionary.")
    line = input()

print(numbers_dictionary)
