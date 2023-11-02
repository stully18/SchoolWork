def factor3(n):
    factors = []
    for a in range(1, n+1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a*b*c == n:
                    factors.append((a,b,c))
    return factors
print(factor3(6))