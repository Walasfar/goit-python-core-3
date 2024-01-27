# Home work 2 in module 3 GoIT Python Core

import random

def get_numbers_ticket(min_number, max_number, quantity):
    
    if min_number >= 1 and max_number <= 1000: # Числа мають бути більше 0 і мін рівно 1000
        # Завдяки random гереруємо список з  різними унікальними числами.
        list_of_numbers = random.sample(range(min_number, max_number), quantity)
        list_of_numbers.sort() # Сортуємо числа.
        return list_of_numbers # Повертаємо список з числами.
    
    else: # If numbers range bad provided
        print("Введено неправильний діапазон!")

print(get_numbers_ticket(1, 1000, 6))
