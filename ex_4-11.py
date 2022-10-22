def ex4():
    print('D')
def ex5():
    print('D')
def ex6():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    computepay(hours=hours, rate=rate)
def ex7():
    print('Enter `stop` as score to stop!')
    while True:
        score = input('Enter Score: ')
        if score == 'stop':
            print('Stopped!')
            break
        else:
            computegrade(score=score)
        
def computepay(hours, rate):
    if hours > 40:
        hours = 40 + ((hours - 40 ) * 1.5)
    else:
        pass
    print('Pay: %.1f' % (hours*rate))

def computegrade(score):
    try:
        score = float(score)
        if score > 1.0:
            print('Bad Score')
        else:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
    except ValueError as e:
        print('Bad Score')
        
ex7()