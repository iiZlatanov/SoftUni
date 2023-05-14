corrupted = [",", ".", "_"]

for _ in range(int(input())):
    string_data = input()
    flag = True

    for cr in corrupted:
        if cr in string_data:
            flag = False
    if flag is True:
        print(f"{string_data} is pure.")
    else:
        print(f"{string_data} is not pure!")
