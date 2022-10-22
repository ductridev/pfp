def q1():
    number = int(input('Enter number: '))
    number_list = []
    sum = 0
    for i in range(0, number):
        sum += i+1
        number_list.append(str(i + 1))
        print(' '.join(number_list))
    print('Sum is: %i' % (sum))


def q2():
    number = int(input('Enter number elements of list: '))
    _list = []
    str_list = []
    digits_count = 0
    for i in range(0, number):
        ele = int(input('Number %i: ' % (i + 1)))
        digits_count += len(str(ele))
        _list.append(ele)
    print('')
    for ele in _list:
        if ele % 5 == 0 and ele < 150:
            print(ele)
        elif ele % 5 != 0:
            print('%i is not devided for 5' % (ele))
        elif ele > 150:
            print('%i is not greater than 150. Skipping...' % (ele))
            pass
        elif ele > 500:
            print('%i is not greater than 500. Stopping...' % (ele))
            break
    print('')
    print('Total digits are: %i' % (digits_count))
    print('')
    for i in range(0, len(_list)):
        str_list.append(str(_list[len(_list) - (i+1)]))
    print('Reversed list: %s' % (' '.join(str_list)))


def q3():
    original_str = str(input('Original string is: '))
    print('Middle four chars are: %s' % (original_str[4:-4]))
    print('')
    
    str_1 = str(input('First string: '))
    str_2 = str(input('Second string: '))
    
    combined_str = str_1[:int(len(str_1)/2)] + str_2 + str_1[int(len(str_1)/2):]
    print('Combined string: %s' % (combined_str))
    print('')
    
    combined_str = str_1[0] + str_2[0] + str_1[int(len(str_1)/2)] + str_2[int(len(str_2)/2)] + str_1[int(len(str_1))-1] + str_2[int(len(str_2))-1]
    print('New string: %s' % (combined_str))

    _str = str(input('Original string need to arrange: '))
    upperStr = ''
    lowerStr = ''
    for i in _str:
        if i.isupper():
            upperStr += i
        elif i.lower():
            lowerStr += i
    print('%s'%(lowerStr+upperStr))
    print('')
    
    mixedString = str(input('Input string= '))
    digits = 0
    chars = 0
    symbols = 0
    for i in mixedString:
        if i.isalpha():
            chars += 1
        elif i.isdigit():
            digits += 1
        else:
            symbols += 1
    print('Total counts of chars, digits, and symbold')
    print('Chars= %i, Digits= %i, Symbols= %i' %(chars, digits, symbols))
    
def q4():
    str_1 = str(input('Original string: '))
    int_str = ''
    str_wout_symbols = ''
    for i in str_1:
        if i.isdigit():
            int_str += i
            str_wout_symbols += i
        elif i.isalpha():
            str_wout_symbols += i
        elif i == ' ':
            if str_wout_symbols[len(str_wout_symbols) - 1] != ' ':
                str_wout_symbols += i
    print(int_str)
    print(str_wout_symbols)
    print('')
    
    number_ele = int(input('Number elements of list: '))
    str_list = []
    str_list_wout_empty = []
    for i in range(0, number_ele):
        str_list.append(str(input('String number %i: '%(i+1))))
    print('')
    
    print('Original list of string')
    print(str_list)
    for ele in str_list:
        if ele != '':
            str_list_wout_empty.append(ele)
    print('')
    
    print('After removing empty strings')
    print(str_list_wout_empty)
    print('')
    
    str_1 = str(input('Original string: '))
    str_1_list = str_1.split('-')
    print('Displaying each substring')
    for ele in str_1_list:
        print(ele)