pours = int(input())
current_filled_capacity = 0

for i in range(1, pours + 1):
    lets_pour = int(input())
    if lets_pour > 255:
        print("Insufficient capacity!")
    if lets_pour <= 255:
        current_filled_capacity += lets_pour
        if current_filled_capacity > 255:
            print("Insufficient capacity!")
            current_filled_capacity -= lets_pour

print(current_filled_capacity)