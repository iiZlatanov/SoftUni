password = input()
flag = True
count_of_digits = 0

if not (6 <= len(password) <= 10):
    print("Password must be between 6 and 10 characters")
    flag = False

for element in password:
    if not (element.isalnum()):
        print("Password must consist only of letters and digits")
        flag = False
        break
for element in password:
    if element.isnumeric():
        count_of_digits += 1
if count_of_digits < 2:
    print("Password must have at least 2 digits")
    flag = False

if flag is True:
    print("Password is valid")