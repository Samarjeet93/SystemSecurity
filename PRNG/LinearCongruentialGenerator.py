#Linear Congruential Generator
# Uses 4 parameters i.e. seed, multiplier, increment and modulus
import math



def nextRand(seed,multiplier,increment,modulus):
    seed = ((multiplier * seed )+ increment) % modulus
    return seed

inp = input("Enter the seed :")
seed = int(inp)

mult = input("Enter the multiplier :")
multiplier = int(mult)

inc = input("Enter the increment :")
increment = int(inc)

mod = input("Enter the modulus :")
modulus = math.pow(2,int(mod))

for n in range(0,20):
    nextseed = nextRand(seed,multiplier,increment,modulus)
    print(nextseed);
    seed = nextseed