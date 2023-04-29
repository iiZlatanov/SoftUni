import sys
variable = sys.maxsize

while True:
    string_or_int = input()
    if string_or_int == 'Stop':
        break
    number = int(string_or_int)
    if number < variable:
        variable = number

print(variable)