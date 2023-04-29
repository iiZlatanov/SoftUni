budget = float(input())
price_for_1kg_flour = float(input())

number_of_cozonacs = 0
colored_eggs = 0
# recipe : 1 pack of eggs 1kg flour 0.250ml milk

price_for_a_pack_of_eggs = price_for_1kg_flour * 0.75
price_for_a_liter_of_milk = (price_for_1kg_flour + price_for_1kg_flour * 0.25) / 4

while True:
    budget -= price_for_a_pack_of_eggs
    budget -= price_for_a_liter_of_milk
    budget -= price_for_1kg_flour
    if budget < 0:
        budget += price_for_a_pack_of_eggs
        budget += price_for_a_liter_of_milk
        budget += price_for_1kg_flour
        break
    number_of_cozonacs += 1
    colored_eggs += 3
    if number_of_cozonacs % 3 == 0:
        colored_eggs -= number_of_cozonacs - 2

print(f"You made {number_of_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")