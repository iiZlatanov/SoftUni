energy = int(input())
won_battles = 0

while True:
    data = input()

    if data != "End of battle":
        distance = int(data)
        if energy >= distance:
            energy -= distance
            won_battles += 1
            if not won_battles % 3:
                energy += won_battles
        else:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
            break
    else:
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        break
