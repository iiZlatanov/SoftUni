word = input()
how_many_of_each_char = {}

for char in word:
    if char != " ":
        if char not in how_many_of_each_char:
            how_many_of_each_char[char] = 1
        else:
            how_many_of_each_char[char] += 1


for key, value in how_many_of_each_char.items():
    print(f"{key} -> {value}")
