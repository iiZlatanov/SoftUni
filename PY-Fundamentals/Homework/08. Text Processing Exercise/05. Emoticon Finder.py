data = input()
index = 0
list_of_emoticons = []

for character in data:
    index += 1
    if character == ":":
        combination = character + data[index]
        list_of_emoticons.append(combination)

print("\n".join(list_of_emoticons))
