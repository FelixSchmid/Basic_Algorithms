
# coding: utf-8

# In[41]:


# Imports:


import random
import time
import matplotlib.pyplot as plt


# Functions:


def create_cards(num_cards):
    cards = list(range(num_cards, 0, -1))
    #random.shuffle(cards)
    return(cards)

def sorting(cards):
    for j in range(1, len(cards)):
        key = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > key:
            cards[i+1] = cards[i]
            i -= 1
        cards[i+1]=key
    return(cards)

def worst_case_time(set_cards):
    start = time.time()
    sorting(cards)
    measure_time = time.time()-start
    print("Worst case time: " + "{0:.9f}".format(measure_time) + " seconds")
    return measure_time



# Execution:


worst_time_in_sec = []
number_of_cards = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]

for number_cards in range(11):
    cards = create_cards(number_of_cards[number_cards])
    time_in_sec = worst_case_time(cards)
    worst_time_in_sec.append(time_in_sec)
    


# Plotting:


plt.plot(number_of_cards, worst_time_in_sec)
plt.xlabel("Number cards")
plt.ylabel("Worst runtime in seconds")
plt.title("Insertion sort algorithm")
plt.show()

