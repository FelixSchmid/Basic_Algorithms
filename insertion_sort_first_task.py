def insertion_sort_increasing (cards):
    for j in range (1,len(cards)):
        key = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > key:
            cards[i+1] = cards[i]
            i = i - 1
        cards[i + 1]= key
    return cards

cards=[5,8,4,6,3,9,1,2,7]
print(cards)
insertion_sort_increasing(cards)
print(cards)
