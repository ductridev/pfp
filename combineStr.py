aStr = str(input('First String: '))
bStr = str(input('Second String: '))

def combineStr(aStr, bStr):
    print('Combined String:', ' '.join([aStr, bStr]))
    print('Combined String: %s' %(' '.join([aStr, bStr])))
    print('Combined String: %s %s' %(aStr, bStr))
    print('Combined String: {} {}'.format(aStr, bStr))
    print(f'Combined String: {aStr} {bStr}')
    
combineStr(aStr=aStr, bStr=bStr)