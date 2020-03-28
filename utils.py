from random import uniform, randrange, randint, shuffle
from math import sqrt


def generateNewReal(mn, mx):
    return uniform(mn, mx)

def generateNewInteger(mn, mx):
    return randrange(mn, mx)

def euclideanDistance(a, b):
    return sqrt((b[0]-a[0])*(b[0]-a[0])+(b[1]-a[1])*(b[1]-a[1]))

def generatePermutation(mn, mx):
    perm = [i for i in range(mn, mx)]
    pos1 = randint(0, mx - 1)
    pos2 = randint(0, mx - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    shuffle(perm)
    return perm

def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val