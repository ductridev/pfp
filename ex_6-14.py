_str = 'X-DSPAM-Confidence:0.8475'

list_str = _str.split(':')
print('%s: %f' %(list_str[0], float(list_str[1])))