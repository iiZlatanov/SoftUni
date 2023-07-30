price_ratings = [int(x) for x in input().split(", ")]
entry_point_index = int(input())
cheap_or_expensive = input()
entry_point_item_price = price_ratings[entry_point_index]
left_sum = 0
right_sum = 0

for el in price_ratings[0:entry_point_index]:
    if el < entry_point_item_price and cheap_or_expensive == "cheap":
        left_sum += el
    elif el >= entry_point_item_price and cheap_or_expensive == "expensive":
        left_sum += el
for el in price_ratings[entry_point_index + 1 ::]:
    if el < entry_point_item_price and cheap_or_expensive == "cheap":
        right_sum += el
    elif el >= entry_point_item_price and cheap_or_expensive == "expensive":
        right_sum += el


if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
