import random

def rnd_std_die():
    return rnd_die_val(1, 6)

def rnd_die_val(min_val, max_val):
    return random.randint(min_val, max_val)
