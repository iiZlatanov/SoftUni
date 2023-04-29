import re

data = input()
pattern = r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b"

names = re.findall(pattern, data)

print(" ".join(names))
