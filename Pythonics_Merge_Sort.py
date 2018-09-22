# Imports:

import random
import time
import matplotlib.pyplot as plt


# Functions:

def divide(array):

    if len(array) <= 1:  
        return array

    half = len(array) // 2
    left = divide(array[:half])
    right = divide(array[half:])

    return merge_sort(left, right)

def merge_sort(left, right):

    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


# Testing functions:

def create_cards(num_cards):
    cards = list(range(num_cards, 0, -1))
    #random.shuffle(cards)
    return(cards)

def worst_case_time(set_cards):
    start = time.time()
    divide(cards)
    measure_time = time.time()-start
    #print("Worst case time: " + "{0:.9f}".format(measure_time) + " seconds")
    return measure_time


# Testing runtime:

worst_time_in_sec = []
number_of_cards = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for number_cards in range(10, 10000, 100):
    cards = create_cards(number_cards)
    time_in_sec = worst_case_time(cards)
    worst_time_in_sec.append(time_in_sec)
    

# Plotting:

plt.plot(range(10, 10000, 100), worst_time_in_sec)
plt.xlabel("Number cards")
plt.ylabel("Worst runtime in seconds")
plt.title("Insertion sort algorithm")
plt.show()