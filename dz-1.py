# Home work III (1)

from datetime import datetime, timedelta

# Argumet example: str '2020-10-09'
def get_days_from_today(date):
    now = datetime.today() # Time now
    try:
        entered_date = datetime.strptime(date, "%Y-%m-%d")  # Convert to object
        different = now - entered_date
        result = different.days # Deys left
        return print(result) # Print for terminal.
    except ValueError:
        print("I don't understand your data: You must enter valid date template!")

    

get_days_from_today('2020-01-23') # Past
get_days_from_today('2050-01-24') # Future
get_days_from_today('2024-01"23') # Invalid data argumet
