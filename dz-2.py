# Home work 2 in module 3 GoIT Python Core

import random

def get_numbers_ticket(min_tickets, max_tickets, quantity):
    if min_tickets >= 1 and max_tickets <= 1000:
        list_of_numbers = random.sample(range(min_tickets, max_tickets), quantity) # Create list of random uniq numbers
        list_of_numbers.sort() # sort
        return list_of_numbers
    else: # If numbers range bad provided
        print("Задано неправельний діапазон чисел!")

print(get_numbers_ticket(1, 1000, 6))
