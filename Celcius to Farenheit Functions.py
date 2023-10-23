def convert_c_to_f():
    c = float(input("What is the tempature in celsius? "))
    f = c*(9/5)+32
    print(f'{c} degrees in celsius is {f} degrees in farenheit')

def convert_f_to_c():
    f = float(input("What is the tempature in farenheit? "))
    c = (f-32)*(5/9)
    print(f'{f} degrees in farenheit is {c} degrees in celcius')
choice = input('What unit of tempature do you have? F or C: ')
choice = choice.capitalize()
if choice == 'F':
    convert_f_to_c()
else:
    convert_c_to_f()