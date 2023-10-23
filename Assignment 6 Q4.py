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
    return resultStr

def do_a_thousand_experiments():
    total_heads = 0
    total_tails = 0
    count = 0

    while count < 1000:
        count += 1
        result = do_one_experiment()
        total_heads += result.count('H')
        total_tails += result.count('T')
        print(result, end='')
    print(f'\nTotal heads: {total_heads} and total tails: {total_tails}')

do_a_thousand_experiments()