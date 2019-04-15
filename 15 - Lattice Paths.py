import math

dimension = (20, 20)

def lattice((x, y)):
    return (math.factorial(x + y)) / (math.factorial(x) * math.factorial(y))

print(lattice(dimension))
