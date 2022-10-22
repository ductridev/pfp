#Ex2:
def Ex_2():
    
    print("Exercise 2:\n ")
    dic_days = dict()
    fname = input("Enter file name: ")
    
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print("File cannot be opened:", fname)
        exit()

    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != "From":
            continue
        else:
            if words[2] not in dic_days:
                dic_days[words[2]] = 1
            else:
                dic_days[words[2]] += 1

    print(dic_days)
Ex_2()

#Ex3:
def Ex_3():
    
    print("\nExercise 3:\n ")
    dic_add = dict()
    fname = input("Enter file name: ")
    
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print("File cannot be opened:", fname)
        exit()

    for line in fhand:
        words = line.split()
        if len(words) < 2 or words[0] != "From":
            continue
        else:
            if words[1] not in dic_add:
                dic_add[words[1]] = 1
            else:
                dic_add[words[1]] += 1

    print(dic_add)
Ex_3()

#Ex4:
def Ex_4():
    
    print("\nExercise 4:\n ")
    dic_add = dict()
    maximum = 0
    maximum_address = ''
    fname = input("Enter file name: ")
    
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print("File cannot be opened:", fname)
        quit()

    for line in fhand:
        words = line.split()
        if len(words) < 2 or words[0] != "From":
            continue

        if words[1] not in dic_add:
            dic_add[words[1]] = 1
        else:
            dic_add[words[1]] += 1

    for address in dic_add:
        if dic_add[address] > maximum:
            maximum = dic_add[address]
            maximum_address = address

    print(maximum_address, maximum)
Ex_4()

#Ex5:
def Ex_5():

    print("\nExercise 5:\n ")
    file_name = input("Enter file name: ")
    lines = [line.strip('\n') for line in open(file_name, 'r')
        if line.startswith("From ")]
    fr_dict = {}

    for line in lines:
        line = line.split()
        email = line[1]
        domain = email.split("@")[1]
        fr_dict[domain] = fr_dict.get(domain, 0) + 1

    print (fr_dict)
Ex_5()