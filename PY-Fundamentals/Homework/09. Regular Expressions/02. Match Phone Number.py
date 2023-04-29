import re

pattern = r"(^|(?<=\s_))[A-Za-z0-9]+(?=[\s\.])"

data = input()

result = re.findall(pattern, data)
print(",".join(result))
