import random

def calculate_pi_mc(N):
    M = 0

    for i in range(N):
        x = random.random()
        y = random.random()

        if x**2 + y**2 < 1:
            M += 1

    pi = 4 * M / N

    return pi
print(calculate_pi_mc(1000))
print(calculate_pi_mc(1000000))
print(calculate_pi_mc(10000000))