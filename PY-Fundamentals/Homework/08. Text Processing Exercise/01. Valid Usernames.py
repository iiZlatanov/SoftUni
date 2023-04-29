data = input().split(", ")
valid_usernames = []

for username in data:
    if 2 < len(username) < 17:
        flag = True
        for char in username:
            if char.isdigit() is not True and char.isalpha() is not True and char != "-" and char != "_":
                flag = False
                break
        if flag is True:
            valid_usernames.append(username)

print("\n".join(valid_usernames))
