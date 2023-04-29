data_countries = input().split(", ")
data_capitals = input().split(", ")
result = {}

for iteration in range(len(data_countries)):
    result[data_countries[iteration]] = data_capitals[iteration]

print("\n".join(f"{key} -> {value}" for key, value in result.items()))
