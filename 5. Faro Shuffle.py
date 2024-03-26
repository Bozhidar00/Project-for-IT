def faro_shuffle(deck, shuffles):
    deck = deck.split()
    deck_length = len(deck)

    for _ in range(shuffles):
        shuffled_deck = []
        for i in range(deck_length // 2):
            shuffled_deck.append(deck[i])
            shuffled_deck.append(deck[i + deck_length // 2])
        deck = shuffled_deck

    return deck


cards = input().strip()
shuffles = int(input().strip())

result = faro_shuffle(cards, shuffles)

print(result)
