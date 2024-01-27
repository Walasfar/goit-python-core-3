# Home work III (1)

from datetime import datetime as dt # Імпортуємо модулі - as dt це псивдонім datetime

# Argument example: yyy-dd-mm
def get_days_from_today(enter_date): # Передаемо аргумент ввиді дати
    
    try: # Провіряємо введену дату
        
        user_date = dt.strptime(enter_date, "%Y-%m-%d") # Змінна з датою, якщо дата введена неправильно - вона йде в блок except
        now = dt.today() # Согоднішній день
        delta_days = now - user_date # Скільки днів пройшло або ще не настало
    
    except ValueError: # Якщо try не розібрав дату то виведеться це повідомлення
        print("The entered event date is not suitable", ValueError)
        
    return delta_days.days # Повертаємо кількість днів


num = get_days_from_today("2024-01-27") # Присвоюємо змінній num дні, які вернула наша функція

print(num) # Вивід
