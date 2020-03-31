import random

def get_exp(starter):
    b = [[0,0,0],[0,0,0],[0,0,0]]
    x = random.randrange(3)
    y = random.randrange(3)
    b[x][y] = starter
    return b

