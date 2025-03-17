from random import choice
from words import NOUN, ADJECTIVES, FLOWER, ELEMENTUM, GEMS

def gen_name():
    adj = choice(ADJECTIVES)
    nnoun = NOUN
    nnoun.extend(FLOWER)
    nnoun.extend(GEMS)
    # nnoun.extend(ELEMENTUM)
    noun1 = choice(nnoun).title()
    noun2 = choice(nnoun).title()
    return f"{adj}{noun1}-{noun2}"


if __name__ == '__main__':
    for _ in range(20):
        print(gen_name())
