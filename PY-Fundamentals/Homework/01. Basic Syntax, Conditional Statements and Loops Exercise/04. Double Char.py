given_string = input()
length_of_given_string = len(given_string)
result_string = ""

for i in range(length_of_given_string):
    result_string += given_string[i] * 2

print(result_string)