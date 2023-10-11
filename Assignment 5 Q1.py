i = 0
count = 0

while count < 30:
    number = 2 ** i
    i += 1
    count += 1
    if count < 29:
        print(number, end=", ")
    else:
        print(number, end="")
