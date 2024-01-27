from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    reminder_list = []
    for user in users:
        now = datetime.today().date()
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday = birthday.replace(year=now.year)

        if birthday < now: # Якщо пройшов встановлюємо слідующий рік
            birthday = birthday.replace(year=now.year + 1)

        until_the_birthday = birthday - now # Різниця дат
        
        if until_the_birthday.days <= 7: # Умова при якій буде виводить дні на тиждень вперед
            reminder = {'name': user['name'], 'congratulation_date': None} # Шаблон словника
            weekday = birthday.isoweekday() # День тижня

            match weekday:
                case 6: # Якщо субота + 2 дні
                    after_weekend = birthday + timedelta(days=2)
                    reminder['congratulation_date'] = after_weekend.isoformat()
                
                case 7: # Неділя + 1 день
                    after_weekend = birthday + timedelta(days=1)
                    reminder['congratulation_date'] = after_weekend.isoformat()

                case _:
                    reminder['congratulation_date'] = birthday.isoformat()
            
            reminder_list.append(reminder) # Добавляємо дату

    return reminder_list # Вертаємо список


users = [
    {"name": "Olek Smith", "birthday": "2024.01.20"},
    {"name": "Fedor Smith", "birthday": "2024.01.22"},
    {"name": "Jane Smith", "birthday": "2024.01.27"},
    {"name": "Ivan Smith", "birthday": "2024.01.29"},
    {"name": "Sasha Smith", "birthday": "2024.02.03"},
    {"name": "Olena Smith", "birthday": "2024.02.04"},
    {"name": "Olena Smith", "birthday": "2025.02.04"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

for reminder in upcoming_birthdays:
    print(reminder)
