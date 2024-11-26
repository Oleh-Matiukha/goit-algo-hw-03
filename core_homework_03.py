# Task 1.
from datetime import datetime

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date,"%Y-%m-%d")
        current_date = datetime.today()
        days_delta = current_date - user_date
        return days_delta.days
    except ValueError:
        print("Format is not correct")

date = input("Write the date in the format yyyy-mm-dd: ")
days_left = get_days_from_today(date)
print(days_left)


# Task 2.
import random

def get_numbers_ticket(min, max, quantity):
    numbers = list()
    if min >= 1 and max <= 1000 and quantity <= max and (max - min) >= quantity:
        return sorted(random.sample(range(min,max),k=quantity))
    else:
        return numbers

lottery_numbers = get_numbers_ticket(10, 15, 9)
print("Ваші лотерейні числа:", lottery_numbers)


# Task 3
import re

def normalize_phone(phone_number):
    clear_number = re.sub(r'\D', '', phone_number)
    if not clear_number.startswith('+'):
        if clear_number.startswith('380'):
            cleaned_number = "+" + clear_number
        else:
            cleaned_number = "+38" + clear_number
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)