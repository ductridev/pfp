def Ex_4():
    
    print("Excercise 4: ")
    fname = input("Enter file name: ")
    fh = open(fname)
    lst = list()
    
    for line in fh:
        words= line.split()
        for word in words:   
            if word not in lst:
                lst.append(word)
                lst.sort()
    
    print (lst)
Ex_4()

def Ex_5():
    
    print("Question 5: ")
    fhand = open('mbox-short.txt')
    count = 0
    
    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From':
            continue
        print(words[1])
        count += 1
    
    print('There were %d lines in the file with From as the first word' % count)
Ex_5()   

def Ex_6():
    
    print("Question 6: ")
    my_list = []
    
    while True:
        number = 0.0
        input_number = input('Enter a number: ').lower()
        
        if input_number == 'done':
            break

        try:
            number = float(input_number)
        except ValueError:
            print('Invalid input')
            quit()

        my_list.append(input_number)

    if my_list:
        print('Maximum: ', max(my_list) or None)
        print('Minimum: ', min(my_list) or None)
Ex_6()