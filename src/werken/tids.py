import base62
import random


MAX_ID = base62.decode("zzzzzzzzzz")
MIN_ID = 0


def id_from_int(value):
    if value < MIN_ID:
        raise ValueError("id must not be negative")
    if value > MAX_ID:
        raise ValueError(
            f"id too large, "
            f"maximum is {MAX_ID} or the resulting {base62.encode(MAX_ID)}")
    return f"{base62.encode(value)!s:>010}"


def random_id():
    return id_from_int(random.randint(0, MAX_ID))
