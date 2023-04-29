lost_fights = int(input())
helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield_count = 0

for current_loss in range(1, lost_fights + 1):
    if current_loss % 2 == 0:
        expenses += helm_price
    if current_loss % 3 == 0:
        expenses += sword_price
    if current_loss % 2 == 0 and current_loss % 3 == 0:
        expenses += shield_price
        broken_shield_count += 1

expenses += (broken_shield_count // 2) * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")