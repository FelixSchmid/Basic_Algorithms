def insort(cards):
    for j in range (1,len(cards)):
        key = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > key:
            cards[i+1] = cards[i]
            i = i - 1
        cards[i + 1]= key
    return cards