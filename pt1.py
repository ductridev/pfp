import os
import uuid
import json
import random
import math
from json.decoder import JSONDecodeError
import threading
import time

CHIP_BUY_PRICE = 11
CHIP_SELL_PRICE = 10
ASSETS_DIR = os.getcwd() + '/assets/'

class Casino():
    def __init__(self):
        self.mac_address = self.getMac_address()
        self.username = self.getUsername()
        self.money, self.chips = self.userWallet()
        print('Starting background task...')
        self.daemon = threading.Thread(target=self.backgroundService, daemon=True, name='JSON Files Async')
        self.daemon.start()
        
    def backgroundService(self):
        
        while True:
            fUsers = open(ASSETS_DIR + 'users.json')
            fWallets = open(ASSETS_DIR + 'wallets.json')
            
            try:
                usersData = json.load(fUsers)
                walletsData = json.load(fWallets)
                
                fUsers.close()
                fWallets.close()
            except:
                usersData = []
                walletsData = []
                
            fUsers = open(ASSETS_DIR + 'users.json', 'w')
            fWallets = open(ASSETS_DIR + 'wallets.json', 'w')
            
            for idx, obj in enumerate(usersData):
                if obj['mac_address'] == self.mac_address:
                    usersData.pop(idx)
            usersData.append({'mac_address': self.mac_address, 'username': self.username})
            fUsers.write(json.dumps(usersData, indent=4))
            
            for idx, obj in enumerate(walletsData):
                if obj['mac_address'] == self.mac_address:
                    walletsData.pop(idx)
            walletsData.append({'mac_address': self.mac_address, 'money': self.money, 'chips': self.chips})
            fWallets.write(json.dumps(walletsData, indent=4))
            
            fUsers.close()
            fWallets.close()
            
            time.sleep(0.1)
        
    def getMac_address(self):
        return ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    
    def changeUsername(self, newUsername):
        self.username = newUsername
        
    def getUsername(self):
        try:
            f = open(ASSETS_DIR + 'users.json')
            data = json.load(f)
            f.close()
        except:
            f = open(ASSETS_DIR + 'users.json', 'w+')
            f.write('')
            f.close()
            
        try:
            f = open(ASSETS_DIR + 'users.json')
            data = json.load(f)
            f.close()
            
            for idx, obj in enumerate(data):
                if obj['mac_address'] == self.getMac_address():
                    username = obj['username']
                    return username
    
        except JSONDecodeError:
            username = str(input('We cannot recognize you, so maybe you are a new player. Please enter your name: '))
            return username
        
    def userWallet(self):
        try:
            f = open(ASSETS_DIR + 'wallets.json')
            data = json.load(f)
            f.close()
        except:
            f = open(ASSETS_DIR + 'wallets.json', 'w+')
            f.write('')
            f.close()
                
        try:  
            f = open(ASSETS_DIR + 'wallets.json')
            data = json.load(f)
            f.close()
            for idx, obj in enumerate(data):
                if obj['mac_address'] == self.getMac_address():
                    money = obj['money']
                    chips = obj['chips']
                    return money, chips
        except JSONDecodeError:
            money = 1000
            chips = 0
            return money, chips
        
    def buyChips(self):
        moneyGiven = int(input('Enter number of money you want to give us: '))
        maxChipsCanBuy = math.floor(moneyGiven / 11)
        print('Maximum chips you can buy: %i' % (maxChipsCanBuy))
        numChipsBuy = int(input('Enter number chips you want to buy: '))
        if numChipsBuy > 0 and numChipsBuy <= maxChipsCanBuy:
            self.money -= numChipsBuy * CHIP_BUY_PRICE
            self.chips += numChipsBuy
            print('You have bought %i chip(s) successful' % (numChipsBuy))
            print('Withdraw to you the leftover cash: $%i' % ( moneyGiven - numChipsBuy * CHIP_BUY_PRICE))
        else:
            print('Invalid number chips to buy!')
            
    def sellChips(self):
        numChipsSell = int(input('Enter number chips you want to sell: '))
        if numChipsSell > 0 and numChipsSell > self.chips:
            self.money += numChipsSell * CHIP_SELL_PRICE
            self.chips -= numChipsSell
            print('You have sold %i chip(s) successful' % (numChipsSell))
        elif numChipsSell <= 0:
            print('You have entered invalid chips!')
        else: 
            print('Insufficient chips!')
            
    def dice(self):
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        return dice1, dice2
        
    def crapsGame(self):
        print('''
Craps Game rule:
    - Roll a pair of fair six-sided dice.
    - If you roll a 7 or 11, you win!
    - If you roll a 2, 3, or 12, you lose.
Otherwise
    - Record what you've rolled. Let this sum be k; also known as your point.
    - If you rolled a point, continue rolling the pair of dice until you get either your point (k) or a
    sum of seven on the two dice.
    - If k comes up first, you win!
    - If 7 comes up first, you lose.
              ''')
        chosenNum = 0
        _ = input("Press enter to roll the dice ")
        dice1, dice2 = self.dice()
        sumOfDice = dice1 + dice2
        
        print('Total of 2 dices is : %i' % (sumOfDice))
        
        if sumOfDice == 7 or sumOfDice == 11:
            print("Congratulations! You won!")
            self.chips += 1
        
        elif sumOfDice == 2 or sumOfDice == 3 or sumOfDice == 12:
            print("You lost \nTry again next time")
            self.chips -= 1
            
        else:
            while True:
                dice1, dice2 = self.dice()
                sumOfDice = dice1 + dice2
                
                if chosenNum == 0:
                    chosenNum = sumOfDice
                    continue
                    
                print('Total of 2 dices is : %i' % (sumOfDice))
                if sumOfDice == chosenNum:
                    print("Congratulations! You won!")
                    self.chips += 1
                    
                    break
                
                elif sumOfDice == 7:
                    print("You lost, \nTry again next time")
                    self.chips -= 1
                    
                    break
            
    def arupGame(self):
        print('''
Arup Game rule:
    - Roll a pair of dice.
    - If you roll a sum of 11 or 12, you win.
    - If you roll a sum of 2, you lose.
Otherwise
    - Record what you've rolled. Let this sum be k; also known as your point.
    - Roll one more time. If this roll exceeds your point(k), you win!
    - If this roll is the same as your point(k) or lower, you lose.
              ''')
        chosenNum = 0
        _ = input("Press enter to roll the dice ")
        dice1, dice2 = self.dice()
        sumOfDice = dice1 + dice2
        
        print('Total of 2 dices is : %i' % (sumOfDice))
        
        if sumOfDice == 11 or sumOfDice == 12:
            print("Congratulations! You won!")
            self.chips += 1
        
        elif sumOfDice == 2:
            print("You lost, \nTry again next time")
            self.chips -= 1
        else:
            while True:
                dice1, dice2 = self.dice()
                sumOfDice = dice1 + dice2
                
                if chosenNum == 0:
                    chosenNum = sumOfDice
                    continue
                    
                print('Total of 2 dices is : %i' % (sumOfDice))
                if sumOfDice > chosenNum:
                    print("Congratulations! You won!")
                    self.chips += 1
                    
                    break
                
                elif sumOfDice <= chosenNum:
                    print("You lost \nTry again next time")
                    self.chips -= 1
                    
                    break   
            
    def report(self):
        print('Report of your wallet: \nMoney: %i\nChips: %i' % (self.money, self.chips))
        
    def help(self):
        print('''
These input will be accepted and send you to specific area!
    a - Arup's Game of Dice Section
    b - Buy Chips Section
    c - Craps Game Section
    s - Sell Chips Section
    r - Report Section
    q - Quit Casino
    h - Help Section
For example: Where do you want to go? h -> We are directing you to Help Section
              ''')
        
if __name__ == '__main__':
    print('''
             ______                       __                            _______               __      __                           
            /      \                     /  |                          /       \             /  |    /  |                          
            /$$$$$$  |  ______    _______ $$/  _______    ______        $$$$$$$  | __    __  _$$ |_   $$ |____    ______   _______  
            $$ |  $$/  /      \  /       |/  |/       \  /      \       $$ |__$$ |/  |  /  |/ $$   |  $$      \  /      \ /       \ 
            $$ |       $$$$$$  |/$$$$$$$/ $$ |$$$$$$$  |/$$$$$$  |      $$    $$/ $$ |  $$ |$$$$$$/   $$$$$$$  |/$$$$$$  |$$$$$$$  |
            $$ |   __  /    $$ |$$      \ $$ |$$ |  $$ |$$ |  $$ |      $$$$$$$/  $$ |  $$ |  $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |
            $$ \__/  |/$$$$$$$ | $$$$$$  |$$ |$$ |  $$ |$$ \__$$ |      $$ |      $$ \__$$ |  $$ |/  |$$ |  $$ |$$ \__$$ |$$ |  $$ |
            $$    $$/ $$    $$ |/     $$/ $$ |$$ |  $$ |$$    $$/       $$ |      $$    $$ |  $$  $$/ $$ |  $$ |$$    $$/ $$ |  $$ |
            $$$$$$/   $$$$$$$/ $$$$$$$/  $$/ $$/   $$/  $$$$$$/        $$/        $$$$$$$ |   $$$$/  $$/   $$/  $$$$$$/  $$/   $$/ 
                                                                                /  \__$$ |                                        
                                                                                $$    $$/                                         
                                                                                $$$$$$/                                          
          ''')
    print('Welcome to Casino Python!')
    print('This casino is built based on Python.')
    casino = Casino()
    while True:
        casino.help()
        option = str(input('Where do you want to go? '))
        
        match option:
            case 'a':
                print("We are directing you to Arup's Game of Dice Section")
                casino.arupGame()
            case 'b':
                print('We are directing you to Buy Chips Section')
                casino.buyChips()
            case 'c':
                print('We are directing you to Craps Game Section')
                casino.crapsGame()
            case 's':
                print('We are directing you to Sell Chips Section')
                casino.sellChips()
            case 'r':
                print('We are directing you to Report Section')
                casino.report()
            case 'q':
                print('We are directing you to the door of Casino')
                break
            case default:
                print('We are directing you to Help Section')