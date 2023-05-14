total = 0

for _ in range(int(input())):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if (0.01 <= price_per_capsule <= 100.00) and (1 <= days <= 31) and (1 <= capsules_needed_per_day <= 2000):
        current_price = price_per_capsule * days * capsules_needed_per_day
        total += current_price
        print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total:.2f}")
