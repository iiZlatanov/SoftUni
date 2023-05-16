from collections import deque
bees = deque(int(x) for x in input().split())
nectar_data = [int(x) for x in input().split()]
operands = deque(input().split())
honey_made = 0


def operation(current_operand, nectar, bee):
    if current_operand == "+":
        return abs(bee + nectar)
    elif current_operand == "-":
        return abs(bee - nectar)
    elif current_operand == "*":
        return abs(bee * nectar)
    elif current_operand == "/":
        return abs(bee / nectar)


while True:
    if bees and nectar_data:
        if nectar_data[-1] >= bees[0]:
            honey_made += operation(operands.popleft(), nectar_data.pop(), bees.popleft())
        elif nectar_data[-1] < bees[0]:
            nectar_data.pop()
    else:
        break

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")
if nectar_data:
    print(f"Nectar left: {', '.join(str(el) for el in nectar_data)}")
