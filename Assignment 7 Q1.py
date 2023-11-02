import random
def random_list(n):
    my_list = []
    while len(my_list) < n:
        x = random.randint(1,100)
        if x in my_list:
            pass
        else:
            my_list.append(x)
    return my_list
L = random_list(10)
print(L)
