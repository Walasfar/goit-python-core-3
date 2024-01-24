# Home work 2 in module 3 GoIT Python Core

import random

def get_numbers_ticket(min, max, quantity):
    list_of_numbers = random.sample(range(min, max), quantity)
    list_of_numbers.sort()
    return list_of_numbers

print(get_numbers_ticket(1, 48, 6))
