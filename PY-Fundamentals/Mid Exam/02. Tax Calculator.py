data = input().split(">>")
valid_types = ["family", "heavyDuty", "sports"]
total_collected = 0
price_sheet = {
    "family": 50,
    "heavyDuty": 80,
    "sports": 100
}

for el in data:
    current_car = el.split()
    if current_car[0] not in valid_types:
        print("Invalid car type.")
        continue
    car_type = current_car[0]
    years_used = int(current_car[1])
    cars_kilometer = int(current_car[2])

    if car_type == "family":
        calc = price_sheet["family"] - (years_used * 5) + ((cars_kilometer // 3000) * 12)
    elif car_type == "heavyDuty":
        calc = price_sheet["heavyDuty"] - (years_used * 8) + ((cars_kilometer // 9000) * 14)
    elif car_type == "sports":
        calc = price_sheet["sports"] - (years_used * 9) + ((cars_kilometer // 2000) * 18)

    total_collected += calc
    print(f"A {car_type} car will pay {calc:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_collected:.2f} euros in taxes.")
