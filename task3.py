import re

def normalize_phone(phone_number):
   fixed_number= re.sub(r"[^\+\d+]", "", phone_number)
   if fixed_number.startswith("+38"):
      return fixed_number
   elif fixed_number.startswith("38"):
      return "+"+fixed_number
   elif fixed_number.startswith("+"): 
      return fixed_number.replace("+", "+38")
   else: return "+38"+fixed_number

raw_numbers = [
    "+067\\t123 4567",
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
