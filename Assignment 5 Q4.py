n1 = 0
n2 = 1
count = 0
sum = 0
while count < 30:
    count += 1
    n1 = n2
    n2 = sum
    sum = n1 + n2
    print(sum, end=',')