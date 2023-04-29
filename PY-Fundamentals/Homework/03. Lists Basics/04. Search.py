n = int(input())
word = input()
result_list = []
result_list_with_unique_word = []

for i in range(n):
    input_words = input()
    result_list.append(input_words)
    if word in input_words:
        result_list_with_unique_word.append(input_words)

print(result_list)
print(result_list_with_unique_word)