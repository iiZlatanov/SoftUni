data = input().split()

total = 0
longer_word = data[0]
shorter_word = data[1]

if len(shorter_word) > len(longer_word):
    longer_word = data[1]
    shorter_word = data[0]

index = 0
for shorter_words_characters in shorter_word:
    longer_words_characters = longer_word[index]
    total += ord(shorter_words_characters) * ord(longer_words_characters)
    index += 1

for extra_characters_in_longer_word in range(len(shorter_word), len(longer_word)):
    longer_words_extra_characters = longer_word[index]
    total += ord(longer_words_extra_characters)
    index += 1

print(total)
