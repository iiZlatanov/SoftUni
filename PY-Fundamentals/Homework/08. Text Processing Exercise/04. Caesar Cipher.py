data = input()
encrypted_text = ""

for character in data:
    encryption = ord(character) + 3
    encrypted_text += chr(encryption)

print(encrypted_text)
