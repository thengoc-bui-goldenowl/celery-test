from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task


@shared_task(name="sum_two_numbers")
def add(x, y):
    for i in range(50000):
        print(i)
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)