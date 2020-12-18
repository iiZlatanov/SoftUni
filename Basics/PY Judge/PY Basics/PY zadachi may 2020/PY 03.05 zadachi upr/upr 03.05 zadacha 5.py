rent_for_kids_party = float(input())
cake = rent_for_kids_party * 20 / 100
drinks = cake - (cake * 0.45)
animator = 1 / 3 * rent_for_kids_party
total = rent_for_kids_party + cake + drinks + animator
print(total)

