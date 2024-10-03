import random

def get_number_tickets(min, max, quantity):
    arr=[]
    try:
        arr=random.sample(range(min, max), quantity)
        arr.sort()
        return arr
    except:
        return arr
    
print(get_number_tickets(8,1, 3))