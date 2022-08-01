import random


def set_debt(obj):
    reducion_value = random.randint(100, 10000)
    obj.debt = max(obj.debt - reducion_value, 0)