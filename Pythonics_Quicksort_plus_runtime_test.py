import random
import time
import matplotlib.pyplot as plt

def quicksort(input_list):
    """Implementation of the quicksort algorithm.
    
    Args:
        input_list: A list consisting of integers.
    Return:
        A sorted list.
    """
    left = []
    right = []
    pivot = []
    if len(input_list) <= 1:
        return input_list
    else:
        pivot_number = input_list[-1]
        for card in input_list:
            if card < pivot_number:
                left.append(card)
            elif card == pivot_number:
                pivot.append(card)
            else:
                right.append(card)
        left = quicksort(left)
        right = quicksort(right) 
        return left + pivot + right
    
# These functions are testing the runtime of the quicksort algorythm.

def create_cards(n):
    """Creats a list of cards and shuffles it.
    
    Args:
        n: The number of integers that should be in the list.
    Returns:
        A list of n integers.
    """
    if type(n) != int:
        print('Please use an integer for n!')
        return 
    if n <= 1:
        print('Please use a positive integer for n!')
        return
    cards = list(range(1,n+1))
    random.shuffle(cards)     
    return(cards)

def avg_time(n_iteration, n_cards):        
    """Returns the average runtime of the quicksort algorythm.
    
    Args:
        n_iterations: The number of iterations.
        n_cards: The number of cards.
    Returns:
        average_time: The average runtime in seconds.
    """
    measure_time = []
    for i in range(0, n_iteration):
        cards = create_cards(n_cards)
        start = time.time()
        quicksort(cards)
        measure_time.append(time.time()-start)
    average_time = sum(measure_time)/len(measure_time)
    return(average_time)

# One sorting test and the runtime test will be executed.

unordered_test_list = [3, 5, 133, -3, 5, 777, 1, 0]
print(unordered_test_list)
print(quicksort(unordered_test_list))
print("Please wait some time for the runtime test... It's worth it!")
time_cards = []
number_cards = []
for n_cards in range(10, 10000, 100):
    time_in_sec = avg_time(10, n_cards)
    time_cards.append(time_in_sec)
    number_cards.append(n_cards)
    
# The results of the test will be plotted in the following. 
    
plt.plot(number_cards, time_cards)
plt.xlabel("Number of cards")
plt.ylabel("Average runtime in seconds")
plt.title("Quicksort algorithm runtime")
plt.show()

