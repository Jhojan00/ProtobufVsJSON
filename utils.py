import time
from typing import Callable
from datetime import timedelta
from random import randint

from faker import Faker

fake = Faker()


def get_object():
    title = " ".join(fake.words(nb=3, unique=True))
    description = fake.sentence()
    time_base = fake.date_time()
    time_start = time_base.strftime("%Y-%m-%d %H:%M:%S")
    time_end = (time_base + timedelta(days=randint(1, 10))).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    price = randint(10, 1000)
    url = fake.url()

    return {
        "title": title,
        "description": description,
        "time_start": time_start,
        "time_end": time_end,
        "price": price,
        "url": url,
    }


def get_dummies(amount: int):
    while amount > 0:
        amount -= 1
        yield get_object()
