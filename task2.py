import random

def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<=1000 and min<=quantity<=max:
        result = random.sample(range(min,max),quantity)
        result.sort()
        return result
    else:
        return []

