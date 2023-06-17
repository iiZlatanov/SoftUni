from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges_list = [int(x) for x in input().split()]
flag = False

while tools and substances:
    tool = tools.popleft()
    substance = substances[-1]
    searched_challenge = tool * substance
    if searched_challenge in challenges_list:
        challenges_list.remove(searched_challenge)
        substances.pop()
    else:
        tool += 1
        tools.append(tool)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

    if not challenges_list:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        flag = True
        break


if not flag:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if challenges_list:
    print(f"Challenges: {', '.join(str(el) for el in challenges_list)}")
