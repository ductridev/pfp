def ex1():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hours > 40:
        hours = 40 + ((hours - 40 ) * 1.5)
    else:
        pass
    print('Pay: %.1f' % (hours*rate))
def ex2():
    hours = input('Enter Hours: ')
    try:
        hours = float(hours)
        rate = input('Enter Rate: ')
        try:
            rate = float(rate)
        except ValueError as e:
            print('Error, please enter numeric input')
    except ValueError as e:
        print('Error, please enter numeric input')
def ex3():
    print('Enter `stop` as score to stop!')
    while True:
        score = input('Enter Score: ')
        try:
            if score == 'stop':
                print('Stopped!')
                break
            else:
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