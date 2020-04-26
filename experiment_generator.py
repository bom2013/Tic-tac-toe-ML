import random

#This function create "experiment"(start board)
def get_exp(starter):
    b = [[0,0,0],[0,0,0],[0,0,0]]
    x = random.randrange(3)
    y = random.randrange(3)
    b[x][y] = starter
    return b

