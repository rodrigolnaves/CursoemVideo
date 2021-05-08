from random import randint
for c in range(2, 51, 2):
    o = randint(31, 37)
    print('\033[{}m{}\033[m'.format(o, c), end=' ')