text = input()

isdigit = ""
isalpha = ""
others = ""

for character in text:
    if character.isdigit() is True:
        isdigit += character
    elif character.isalpha() is True:
        isalpha += character
    else:
        others += character

print(f"{isdigit}\n{isalpha}\n{others}")
