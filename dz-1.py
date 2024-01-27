# Home work III (1)

from datetime import datetime as dt 


def get_days_from_today(enter_date):
    
    try: # Провіряємо введену дату
        
        user_date = dt.strptime(enter_date, "%Y-%m-%d")
        now = dt.today() 
        delta_days = now - user_date
    
    except ValueError as e: # Якщо try не розібрав дату то виведеться це повідомлення
        
        print("The entered event date is not suitable", e)
        return
        
    return delta_days.days # Повертаємо кількість днів


num = get_days_from_today("2024-01-27")

print(num)
