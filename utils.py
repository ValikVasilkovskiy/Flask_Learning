import string
import random


def id_generator(size=10, chars=string.ascii_letters):
    for i in str(size):
        if i not in string.digits and i != '-':
            return 'Size must be integer'
    if int(size) <= 0:
        return 'Enter size > 0'

    return ''.join(random.choice(chars) for _ in range(int(size)))
