import math

digits = 4


def nextRand(seed):
    n = str(seed * seed);
    while len(n) < (digits * 2):
        n = "0" + n
    start = math.floor(digits / 2);
    end = start + digits;
    seed = int(n[start:end]);
    return seed


inp = input("Enter the seed :")
seed = int(inp)

for n in range(0,20):
    nextseed = nextRand(seed)
    print(nextseed);
    seed = nextseed