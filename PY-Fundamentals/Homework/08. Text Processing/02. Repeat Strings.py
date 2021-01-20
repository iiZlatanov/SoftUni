data = input().split()
concatenated_string = ""

for element in data:
    for length in range(len(element)):
        concatenated_string += element

print(concatenated_string)
