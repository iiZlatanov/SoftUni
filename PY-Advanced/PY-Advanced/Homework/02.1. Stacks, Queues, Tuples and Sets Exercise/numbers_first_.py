set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])

for _ in range(int(input())):
    data = input().split()
    command = data[0] + data[1]
    if command == "CheckSubset":
        print(set_1.issubset(set_2) or set_2.issubset(set_1))
    else:
        sequence = data[2:]
        if command == "AddFirst":
            for el in sequence:
                set_1.add(int(el))
        elif command == "AddSecond":
            for el in sequence:
                set_2.add(int(el))
        elif command == "RemoveFirst":
            for el in sequence:
                if int(el) in set_1:
                    set_1.discard(int(el))
        elif command == "RemoveSecond":
            for el in sequence:
                if int(el) in set_2:
                    set_2.discard(int(el))

print(f"{', '.join(str(x) for x in sorted(set_1))}\n"
      f"{', '.join(str(x) for x in sorted(set_2))}")
