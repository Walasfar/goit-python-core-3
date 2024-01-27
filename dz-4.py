from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    reminder_list = []
    for user in users:
        now = datetime.today().date()
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        until_the_birthday = now - birthday
        

        if birthday < now:
            continue
        
        elif until_the_birthday.days < 7:
            reminder = {'name': user['name'], 'congratulation_date': None}
            weekday = birthday.isoweekday()

            match weekday:
                case 6:
                    after_weekend = birthday + timedelta(days=2)
                    reminder['congratulation_date'] = after_weekend.isoformat()
                
                case 7:
                    after_weekend = birthday + timedelta(days=1)
                    reminder['congratulation_date'] = after_weekend.isoformat()
                
                case _:
                    reminder['congratulation_date'] = birthday.isoformat()
                    
            reminder_list.append(reminder)

    return reminder_list


users = [
    {"name": "Olek Smith", "birthday": "2024.01.20"},
    {"name": "Fedor Smith", "birthday": "2024.01.22"},
    {"name": "Jane Smith", "birthday": "2024.01.27"},
    {"name": "Ivan Smith", "birthday": "2024.01.29"},
    {"name": "Sasha Smith", "birthday": "2024.02.03"},
    {"name": "Olena Smith", "birthday": "2024.02.04"},
]

upcoming_birthdays = get_upcoming_birthdays(users)

for reminder in upcoming_birthdays:
    print(reminder)
    
print(upcoming_birthdays)
