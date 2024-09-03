def cards_to_money(cards):
    money = 0
    cards = list(map(int, cards))
    for i in range(M):
        money += cards[i] * 10 ** (M - 1 - i)
    return money

cards = ['1', '5', '2', '4', '8']
M = len(cards)
print(cards_to_money(cards))

cards.append(123)
print(cards)