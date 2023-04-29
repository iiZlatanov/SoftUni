data = input()
replace_repeating_characters = ""
previous_character = ""

for character in data:
    if previous_character != character:
        replace_repeating_characters += character
    previous_character = character

print(replace_repeating_characters)
