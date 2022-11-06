from random import sample


def gen_code() -> str:
    numbers = '0123456789'
    password = ''.join(sample(numbers, 6))
    return password
