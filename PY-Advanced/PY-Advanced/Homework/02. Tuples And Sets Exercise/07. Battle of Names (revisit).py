number_of_iterations = int(input())
odd_set = set()
even_set = set()

for x in range(number_of_iterations):
    data = input()
    odd_or_even = 0
    for letter in data:
        odd_or_even += ord(letter)

    result = odd_or_even // (x + 1)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(odd_set) == sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.union(even_set))}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.difference(even_set))}")
elif sum(odd_set) < sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.symmetric_difference(even_set))}")
