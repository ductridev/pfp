import random

def generate():
    return random.randint(0, 100)

if __name__ == "__main__":
    print('''        
                        ,---.                    ,--,--'.         ,-,-.             .           
                        |  -'  . . ,-. ,-. ,-.   `- |   |-. ,-.   ` | |   . . ,-,-. |-. ,-. ,-. 
                        |  ,-' | | |-' `-. `-.    , |   | | |-'     | |-. | | | | | | | |-' |   
                        `---|  `-' `-' `-' `-'    `-'   ' ' `-'    ,' `-' `-' ' ' ' `-' `-' '   
                        ,-.|                                                                   
                        `-+'                                                                   
          ''')
    num = generate()
    print('Welcome to Guess The Number! Please select level to start!')
    print('(1) Easy - Unlimited guesses')
    print('(2) Normal - 20 guesses')
    print('(3) Hard - 15 guesses')
    print('(4) Super Hard - 10 guesses')
    print('(5) Insane - 5 guesses')
    timeGuess = 0
    while True:
        level = int(input('Enter level: '))
        if level == 1:
            print('Selected level 1 - Easy')
            print('You have unlimited guesses')
            timeGuess = 0
            break
        elif level == 2:
            print('Selected level 2 - Normal')
            timeGuess = 20
            break
        elif level == 3:
            print('Selected level 3 - Hard')
            timeGuess = 15
            break
        elif level == 4:
            print('Selected level 4 - Super Hard')
            timeGuess = 10
            break
        elif level == 5:
            print('Selected level 5 - Insane')
            timeGuess = 5
            break
        else:
            print('Incorrect level!')
    if timeGuess == 0:
        while True:
            guessNum = int(input('Guess the number: '))
            if guessNum < num:
                print('Your guess number is smaller than that number!')
            elif guessNum > num:
                print('Your guess number is bigger than that number!')
            else:
                print('''
                      [..      [..                       [..        [..                   
                       [..    [..                        [..        [..                   
                        [.. [..      [..    [..  [..     [..   [.   [..   [..    [.. [..  
                          [..      [..  [.. [..  [..     [..  [..   [.. [..  [..  [..  [..
                          [..     [..    [..[..  [..     [.. [. [.. [..[..    [.. [..  [..
                          [..      [..  [.. [..  [..     [. [.    [.... [..  [..  [..  [..
                          [..        [..      [..[..     [..        [..   [..    [...  [..
                                                                                            
                      ''')
                print('Correct! The number is %i'%(num))
                break
    else:
        correct = False
        for x in range(0, timeGuess):
            print('You have %i guesses left' % (timeGuess - x))
            guessNum = int(input('Guess the number: '))
            if guessNum < num:
                print('Your guess number is smaller than that number!')
            elif guessNum > num:
                print('Your guess number is bigger than that number!')
            else:
                correct = True
                print('''
                      [..      [..                       [..        [..                   
                       [..    [..                        [..        [..                   
                        [.. [..      [..    [..  [..     [..   [.   [..   [..    [.. [..  
                          [..      [..  [.. [..  [..     [..  [..   [.. [..  [..  [..  [..
                          [..     [..    [..[..  [..     [.. [. [.. [..[..    [.. [..  [..
                          [..      [..  [.. [..  [..     [. [.    [.... [..  [..  [..  [..
                          [..        [..      [..[..     [..        [..   [..    [...  [..
                                                                                            
                      ''')
                print('Correct! The number is %i'%(num))
                break
        if correct == False:
            print('''
                      [..      [..                       [..                                 
                       [..    [..                        [..                                 
                         [.. [..      [..    [..  [..     [..         [..     [....    [..    
                           [..      [..  [.. [..  [..     [..       [..  [.. [..     [.   [.. 
                           [..     [..    [..[..  [..     [..      [..    [..  [... [..... [..
                           [..      [..  [.. [..  [..     [..       [..  [..     [..[.        
                           [..        [..      [..[..     [........   [..    [.. [..  [....             
                ''')
            print('You have run out of guesses')