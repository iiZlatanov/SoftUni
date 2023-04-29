fire_data = input().split("#")
amount_of_water = int(input())
total_fire = 0
print("Cells:")

for fire in fire_data:
    support_list = fire.split(" = ")
    for data in support_list:
        data_in_int = 0
        if data == "High" or data == "Medium" or data == "Low":
            data_in_height = data
        if data != "High" and data != "Medium" and data != "Low":
            data_in_int = int(data)
        if data_in_height == "High" and 81 <= data_in_int <= 125 or data_in_height == "Medium" and 51 <= data_in_int <= 80 or data_in_height == "Low" and 1 <= data_in_int <= 50:
            if amount_of_water >= data_in_int:
                amount_of_water -= data_in_int
                total_fire += data_in_int
                print(f" - {data_in_int}")

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")