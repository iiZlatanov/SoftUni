number_of_people = int(input())
capacity = int(input())

result = number_of_people // capacity
if number_of_people % capacity != 0:
    result += 1
print(result)