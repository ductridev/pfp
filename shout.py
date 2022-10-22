from os import getcwd

CURRENT_DIR = getcwd() + '/assets'

def ex71():
    print('Read text from file')
    file_name = str(input('Enter a file name: '))
    try:
        file = open(CURRENT_DIR + '/' + file_name, 'rt')
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()
    except IOError:
        print('Error: %s does not apper o exist at directory: %s' %(file_name, CURRENT_DIR))
        
def ex72():
    print('Find text in specific file')
    file_name = str(input('Enter a file name: '))
    try:
        file = open(CURRENT_DIR + '/' + file_name, 'rt')
        lines = file.readlines()
        _float = 0
        count_lines = 0
        for line in lines:
            if line.startswith('X-DSPAM-Confidence: '):
                _float += float(line[20:])
                count_lines += 1
        print('Average spam confidence: %f'%(_float/count_lines))
        file.close()
    except IOError:
        print('Error: %s does not apper o exist at directory: %s' %(file_name, CURRENT_DIR))