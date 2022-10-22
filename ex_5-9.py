def ex1():
    numbers = []
    while True:
        raw_input = input('Enter a number: ')
        if raw_input == 'done':
            total = 0
            count = len(numbers)
            for x in numbers:
                total += x
            print('%f %f %f' %(total, count, total/count))
            break
        else:
            try:
                number = float(raw_input)
                numbers.append(number)
                
            except ValueError as e:
                print('Invalid Input')
def ex2():
    numbers = []
    while True:
        raw_input = input('Enter a number: ')
        if raw_input == 'done':
            total = 0
            count = len(numbers)
            maximum = 0
            minimum = 0
            for x in numbers:
                total += x
                
                if maximum == 0:
                    maximum = x
                elif x > maximum:
                    maximum = x
                    
                if minimum == 0:
                    minimum = x
                elif x < minimum:
                    minimum = x
                    
            print('%f %f %f %f' %(total, count, maximum, minimum))
            break
        else:
            try:
                number = float(raw_input)
                numbers.append(number)
                
            except ValueError as e:
                print('Invalid Input')
ex2()