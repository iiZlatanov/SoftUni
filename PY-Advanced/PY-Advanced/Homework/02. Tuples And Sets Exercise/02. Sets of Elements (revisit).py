n, m = [int(x) for x in input().split()]

set_1 = {int(input()) for _ in range(n)}
set_2 = {int(input()) for _ in range(m)}

print(*set_1.intersection(set_2), sep="\n")
