import random
ranInt = random.randint(1,1000000000 )
digit = int(input('Which digit would you like removed? ')) - 1
Digit = digit + 1
ranIntStr = str(ranInt)
print(ranIntStr)
print(ranIntStr[0:digit] + ranIntStr[Digit:] )