def palindrome_or_not(x):
    reversed = x[::-1]
    if reversed == x:
        print(True)
    else:
        print(False)


data = input().split(", ")
for element in data:
    palindrome_or_not(element)