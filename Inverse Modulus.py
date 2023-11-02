x = 0
n = int(input('What is the base number? '))
m = int(input('What is the modulus? '))
while True:
    x += 1
    if ((x * n) % m) == 1:
        print(x)
        break