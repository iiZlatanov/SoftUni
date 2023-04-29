text = input()
input_string = []
for ch in text:
    input_string.append(ch)
result_string = []

while input_string:
    current_ch = input_string[-1]
    result_string.append(current_ch)
    input_string.pop()

print("".join(result_string))
