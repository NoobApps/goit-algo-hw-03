import re

numslist=["    +38(050)123-32-34","     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   "]

def normalize_phone(phone_number):
    pattern=r"[^0-9]"
    phone_number=re.sub(pattern,"",phone_number)
    return ("+380"+phone_number[-10:])

for num in numslist:
    print(normalize_phone(num))