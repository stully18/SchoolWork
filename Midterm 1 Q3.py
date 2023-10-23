limit = int(input('What number to stop at? '))
int = 0
i = 0
while int < limit:
    int = 2**i
    i += 1
    if int > limit:
        break
    print(int, end=',')