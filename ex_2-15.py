from turtle import heading, width


def ex2():
    name = str(input('Enter your name: '))
    print('Hello %s' % name)
def ex3():
    hours = float(input('Enter Hour: '))
    rate = float(input('Enter Rate: '))
    print('Pay: %.2f' % (hours*rate))
def ex4():
    width = float(input('width = '))
    height = float(input('height = '))
    print('width//2 %.2f' % (width//2))
    print('width/2.0 %.2f' % (width/2.0))
    print('height/3 %.2f' % (height/3))
    print('1 + 2 * 5 %i' % (1 + 2 * 5))
def ex5():
    celsius = float(input('Enter Celsius: '))
    print('Celsius -> Fahrenheit: %f -> %f' % (celsius, celsius*(9/5) + 32 ))