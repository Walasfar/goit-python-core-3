# Home work IV

import re

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


def normalize_phone(phone_number):
    pattern = r"[\D+]"
    ph_number = re.sub(pattern, "", phone_number)
    structure_number = len(ph_number)
    match structure_number:
        case 13:
            return ph_number
        case 12:
            return "+" + ph_number
        case 10:
            return "+38" + ph_number

normal_numers = [normalize_phone(num) for num in raw_numbers]

print(normal_numers)
