import random

def do_one_experiment():
    resultStr = ''
    while True:
        HorT = random.randint(0, 1)
        if HorT == 0:
            resultStr += 'H'

        else:
            resultStr += 'T'
            break
    print(resultStr)
do_one_experiment()