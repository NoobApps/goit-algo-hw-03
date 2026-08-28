import re

def normalize_phone(phone_number):
    pattern=r"[^0-9]"
    phone_number=re.sub(pattern,"",phone_number)
    return ("+38"+phone_number[-10:])

