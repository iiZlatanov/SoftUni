cards = str(input()).split()
number_of_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

for j in range(number_of_shuffles):

    left_cards = []
    right_cards = []
    if j == 0:
        shuffled_cards = top_card.split()
    half = len(cards) // 2

    for index in range(1, half):
        if j == 0:
            left_cards.append(cards[index])
        else:
            left_cards.append(shuffled_cards[index])

    for index in range(half, len(cards) - 1):
        if j == 0:
            right_cards.append(cards[index])
        else:
            right_cards.append(shuffled_cards[index])
    if j != 0:
            shuffled_cards = top_card.split()
    for index in range(len(right_cards)):
        shuffled_cards.append(right_cards[0])
        right_cards.pop(0)
        shuffled_cards.append(left_cards[0])
        left_cards.pop(0)

    shuffled_cards.append(bottom_card)
print(shuffled_cards)