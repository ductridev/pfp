from asyncio import constants
from operator import truediv
import random
from collections import Counter
import uuid
import json

class SlotMachine:
    def __init__(self, money, mac_address):
        self.result = []
        self.money = money
        self.mac_address = mac_address
    
    def randomNcheck(self):
        self.money -= 0.25
        self.result = []
        for x in range(3):
            self.result.append(random.randint(0,9))
        print('The slot machine shows %s.\n' %("".join([str(i) for i in self.result])))
        self.result = dict(Counter(self.result))
        for x in self.result:
            if(self.result.get(x) == 2):
                self.money += 0.5
                print('You win 50 cents.\n')
                print('You have $%s.\n'%(self.money))
                return
            elif(self.result.get(x) == 3):
                self.money += 10
                print('You win the big prize, $10,00!\n')
                print('You have $%s.\n'%(self.money))
                return
            else:
                continue
        print("Sorry you don't win anything.\n")
        print('You have $%s.\n'%(self.money))
            
    def saveGame(self):
        self.saveMoney()
        print("Your game had saved")
    
    def cashOut(self):
        self.saveMoney()
        print("Thank you for playing! You end with $%s" % (self.money))
        
    def saveMoney(self):
        try:
            f = open('money.json')
            data = json.load(f)
            f.close()
        except:
            data = []
            
        for idx, obj in enumerate(data):
            if obj['mac_address'] == mac_address:
                data.pop(idx)
                
        f = open("money.json", "w")
        data.append({'mac_address': self.mac_address, 'money': self.money})
        f.write(json.dumps(data, indent=4))
        f.close()
        
if __name__ == "__main__":
    print('''
        :'######::'##::::::::'#######::'########::::'##::::'##::::'###:::::'######::'##::::'##:'####:'##::: ##:'########:
        '##... ##: ##:::::::'##.... ##:... ##..::::: ###::'###:::'## ##:::'##... ##: ##:::: ##:. ##:: ###:: ##: ##.....::
        ##:::..:: ##::::::: ##:::: ##:::: ##::::::: ####'####::'##:. ##:: ##:::..:: ##:::: ##:: ##:: ####: ##: ##:::::::
        . ######:: ##::::::: ##:::: ##:::: ##::::::: ## ### ##:'##:::. ##: ##::::::: #########:: ##:: ## ## ##: ######:::
        :..... ##: ##::::::: ##:::: ##:::: ##::::::: ##. #: ##: #########: ##::::::: ##.... ##:: ##:: ##. ####: ##...::::
        '##::: ##: ##::::::: ##:::: ##:::: ##::::::: ##:.:: ##: ##.... ##: ##::: ##: ##:::: ##:: ##:: ##:. ###: ##:::::::
        . ######:: ########:. #######::::: ##::::::: ##:::: ##: ##:::: ##:. ######:: ##:::: ##:'####: ##::. ##: ########:
        :......:::........:::.......::::::..::::::::..:::::..::..:::::..:::......:::..:::::..::....::..::::..::........::
    ''')
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    money = 0
    exist = False
    try:
        f = open('money.json')
        data = json.load(f)
        f.close()
        for idx, obj in enumerate(data):
            if obj['mac_address'] == mac_address:
                money = obj['money']
                exist = True
        if exist == False:
            money = 10
    except:
        money = 10
    
    if money >= 0.25:
        slotMachine = SlotMachine(money, mac_address)
        while True:
            print('Choose one of the following menu options:\n')
            print('1) Play the slot machine.\n')
            print('2) Save game.\n')
            print('3) Cash out.\n')
            option = input()
            match int(option):
                case 1:
                    slotMachine.randomNcheck()
                case 2:
                    slotMachine.saveGame()
                case 3:
                    slotMachine.cashOut()
                    break