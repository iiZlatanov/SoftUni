import re

input_data = int(input())
regex = r"\|([A-Z]{4,})+\|:#([A-Za-z]+)\s{1}([A-Za-z]+)#"

for x in range(input_data):
    print_message = input()
    matches = re.findall(regex, print_message)
    if matches:
        for match in matches:
            title = match[1] + " " + match[2]
            print(f"{match[0]}, The {title}")
            print(f">> Strength: {len(match[0])}")
            print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
