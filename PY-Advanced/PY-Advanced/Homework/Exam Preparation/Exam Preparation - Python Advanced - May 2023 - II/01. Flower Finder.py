from collections import deque

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

searched_flowers = {
    "rose": 0,
    "tulip": 0,
    "lotus": 0,
    "daffodil": 0,
}
already_searched_letters = []
flag = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    if vowel not in already_searched_letters:
        for flower in searched_flowers.keys():
            for ch in flower:
                if ch == vowel:
                    searched_flowers[flower] += 1
        already_searched_letters.append(vowel)

    if consonant not in already_searched_letters:
        for flower in searched_flowers.keys():
            for ch in flower:
                if ch == consonant:
                    searched_flowers[flower] += 1
        already_searched_letters.append(consonant)

    for key, value in searched_flowers.items():
        if len(key) == value:
            print(f"Word found: {key}")
            flag = True
            break

    if flag:
        break

if not flag:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(F"Consonants left: {' '.join(consonants)}")
