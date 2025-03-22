import random
from roguelike_main import walls


def random_square():
    tall = random.int(100, 300)
    long = random.int(100, 300)
    pos_tall = 500 - tall
    pos_long = 500 - long
    pos_tall /= 2
    pos_long /= 2
    walls(long, tall, pos_long, pos_tall)
