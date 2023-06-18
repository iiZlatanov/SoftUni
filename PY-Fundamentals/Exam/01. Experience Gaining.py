experience_needed = int(input())
total_battles = int(input())
gained_xp = 0
amount_of_battles_count = 0

for x in range(total_battles):
    if gained_xp >= experience_needed:
        print(f"Player successfully collected his needed experience for {amount_of_battles_count} battles.")
        break

    current_battle_xp = int(input())
    amount_of_battles_count += 1

    if not amount_of_battles_count % 15:
        current_battle_xp += current_battle_xp * 0.05
    elif not amount_of_battles_count % 5:
        current_battle_xp -= current_battle_xp * 0.1
    elif not amount_of_battles_count % 3:
        current_battle_xp += current_battle_xp * 0.15

    gained_xp += current_battle_xp

    if gained_xp >= experience_needed:
        print(f"Player successfully collected his needed experience for {amount_of_battles_count} battles.")
        break

if gained_xp < experience_needed:
    print(f"Player was not able to collect the needed experience, {experience_needed - gained_xp:.2f} more needed.")
