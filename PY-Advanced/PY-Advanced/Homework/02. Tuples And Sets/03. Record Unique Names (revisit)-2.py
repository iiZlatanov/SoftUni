n = int(input())
names = []

for _ in range(n):
    name = input()
    names.append(name)

print("\n".join(set(names)))
