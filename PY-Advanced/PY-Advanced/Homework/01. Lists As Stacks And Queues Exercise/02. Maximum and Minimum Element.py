number_of_queries = int(input())
stack = []

for _ in range(number_of_queries):
    query = input()
    if len(query) > 1:
        query = query.split()
        stack.insert(0, int(query[1]))
    else:
        if len(stack) > 0:
            if query == "2":
                stack.pop()
            elif query == "3":
                print(max(stack))
            else:
                print(min(stack))

stack = list(map(str, stack))
print(", ".join(stack))
