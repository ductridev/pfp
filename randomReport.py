import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# words = int(input('Enter words require: '))
words = 20
report_str = ''
for i in range(0, words):
    report_tmp = random.choices(letters, k=3)
    report_tmp += random.choices(numbers, k=2)
    report_tmp += random.choices(symbols, k=1)
    random.shuffle(report_tmp)
    report_str_tmp = ''.join(report_tmp)
    report_str += report_str_tmp + ' '
    
print(report_str)